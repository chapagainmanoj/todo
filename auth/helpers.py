import base64
import hashlib, binascii, os
from .tables import users
from resources import database


def authentication_required(resolver):
    async def wrapper_func(source, info, **kwargs):
        request = info.context["request"]
        result = None
        # todo: else should throw error
        if request.user.is_authenticated:
            # kwargs["id"] = request.user.id
            result = await resolver(source, info, **kwargs)
        return result

    return wrapper_func

def hash_password(password):
    salt = hashlib.sha256(os.urandom(60)).hexdigest().encode('ascii')

    pwdhash = hashlib.pbkdf2_hmac('sha512', password.encode('utf-8'), 
        salt, 100000)
    pwdhash = binascii.hexlify(pwdhash)
    return (salt + pwdhash).decode('ascii')
 
def verify_password(stored_password, provided_password):
    salt = stored_password[:64]
    stored_password = stored_password[64:]

    pwdhash = hashlib.pbkdf2_hmac('sha512', 
        provided_password.encode('utf-8'), 
        salt.encode('ascii'), 
        100000)
    pwdhash = binascii.hexlify(pwdhash).decode('ascii')
    return pwdhash == stored_password

async def get_user(username):
    user = None
    query = users.select().where(users.c.username == username)
    result = await database.fetch_one(query)
    if result:
        user = {
            "id": result["id"],
            "username": result["username"],
            "password": result["password"]
        }
    return user

async def create_user(username, password):
    passwordhash = hash_password(password)
    query = users \
        .insert() \
        .values(
            username=username,
            password=passwordhash
        )
    result = await database.execute(query)
    if result:
        user = {
            "id": result,
            "username": username,
            "password": passwordhash
        }
    return user
    
async def login(username, password):
    try:
        user = await get_user(username)
        if user is None:
            return None
        import pdb; pdb.set_trace()
        if verify_password(user.get("password", None), password):
            return gen_token(username, password)
    except Exception as errors:
        pass
    return None

async def signup(username, password):
    try:
        user = await create_user(username, password)
        if user is None:
            return None
        await login(username, password)
    except Exception as errors:
        pass

# may be the approach should be different
async def authenticate_user(username, password):
    try:
        user = get_user(username)
        if user is None:
            return None
        if verify_password(user.get("password", None), password):
            return user
    except Exception as errors:
        pass
    return None

def gen_token(username, password):
    token = base64.b64encode(bytes(f'{username}:{password}', encoding='ascii')).decode('ascii')
    return token