import base64
import binascii
from starlette.authentication import (
    AuthenticationBackend, BaseUser, AuthCredentials, UnauthenticatedUser
)

class AuthenticatedUser(BaseUser):
    def __init__(self, id, username):
        self.id = id
        self.username = username

    @property
    def is_authenticated(self):
        return True

    @property
    def display_name(self) -> str:
        return self.username

class BasicAuthBackend(AuthenticationBackend):
    async def authenticate(self, request):
        user = UnauthenticatedUser()
        if "Authorization" not in request.headers:
            return 

        auth = request.headers["Authorization"]
        try:
            scheme, credentials = auth.split()
            if scheme.lower() != 'basic':
                return
            decoded = base64.b64decode(credentials).decode("ascii")
        except (ValueError, UnicodeDecodeError, binascii.Error) as exc:
            raise AuthenticationError('Invalid basic auth credentials')

        username, _, password = decoded.partition(":")

        verified_user = authenticaticate_user(username, password)
        if (verified_user):
            user = AuthenticatedUser(verified_user.id, verified_user.username)
        return AuthCredentials(["authenticated"]), user