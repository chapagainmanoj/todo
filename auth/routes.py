from starlette.routing import Route, Mount
from ariadne.asgi import GraphQL
from .views import Homepage
from .schema import schema
from settings import DEBUG

routes = [
    Route('/', Homepage),
    Mount('/auth', GraphQL(schema, debug=DEBUG)),
]