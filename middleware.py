from starlette.middleware import Middleware
from starlette.middleware.authentication import AuthenticationMiddleware
from auth.middleware import BasicAuthBackend

middleware = [
    Middleware(AuthenticationMiddleware, backend=BasicAuthBackend())
]