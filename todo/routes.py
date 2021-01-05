from starlette.routing import Route
from .views import list_todo, add_todo

routes = [
    Route("/todo", endpoint=list_todo, methods=["GET"]),
    Route("/todo", endpoint=add_todo, methods=["POST"]),
]