from starlette.authentication import (
    AuthenticationBackend, AuthenticationError, SimpleUser, UnauthenticatedUser,
    AuthCredentials
)
import base64
import binascii

class BasicAuthBackend(AuthenticationBackend):
    async def authenticate(self, request):
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
        # TODO: You'd want to verify the username and password here.
        return AuthCredentials(["authenticated"]), SimpleUser(username)

