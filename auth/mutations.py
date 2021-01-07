from resources import database
from .helpers import login, signup

async def resolve_login(_, info, **kwargs):
    try:
        username = kwargs.get('username')
        password = kwargs.get('password')
        token = login(username, password)
        if token :
            payload = {
                "success": True,
                "token": token
            }
        else:
            payload = {
            "success": False,
            "errors": ["Incorrect username or password"]
            }

    except Exception as error:
        payload = {
            "success": False,
            "errors": [str(error)]
        }

    return payload

async def resolve_signup(_, info, **kwargs):
    try:
        username = kwargs.get('username')
        password = kwargs.get('password')
        token = signup(username, password)
        if token :
            payload = {
                "success": True,
                "token": token
            }
        else:
            payload = {
            "success": False,
            "errors": ["Couldn't create user."]
            }

    except Exception as error:
        payload = {
            "success": False,
            "errors": [str(error)]
        }

    return payload