from starlette.routing import Route
from .views import Homepage

routes = [
    Route('/', Homepage)
]