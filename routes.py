from starlette.routing import Route, Mount
from todo.schema import hello_gql
from auth.routes import routes as auth_routes
from todo.routes import routes as todo_routes

routes = [
    Mount('/graphql', hello_gql),
]
routes += auth_routes
routes += todo_routes

