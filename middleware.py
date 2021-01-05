from starlette.middleware import Middleware
from starlette.middleware.authentication import AuthenticationMiddleware
from auth.basic_auth import BasicAuthBackend

middleware = [
    Middleware(AuthenticationMiddleware, backend=BasicAuthBackend())
]