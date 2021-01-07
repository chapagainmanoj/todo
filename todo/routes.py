from starlette.routing import Mount
from ariadne.asgi import GraphQL
from .schema import schema
from settings import DEBUG

routes = [
    Mount('/api/todo', GraphQL(schema, debug=DEBUG)),
]