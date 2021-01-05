from starlette.applications import Starlette
from starlette.routing import Route, Mount
from starlette.middleware import Middleware
from starlette.middleware.authentication import AuthenticationMiddleware
from auth.basic_auth import BasicAuthBackend
from todo.schema import hello_gql
from auth.routes import routes as auth_routes
from todo.routes import routes as todo_routes
from db import database
import uvicorn


app_routes = [
    Mount('/graphql', hello_gql),
]
app_routes += auth_routes
app_routes += todo_routes

middleware = [
    Middleware(AuthenticationMiddleware, backend=BasicAuthBackend())
]

app = Starlette(
    debug=True, 
    routes=app_routes, 
    middleware=middleware,
    on_startup=[database.connect],
    on_shutdown=[database.disconnect]
    )

if __name__ == "__main__":
    uvicorn.run(app, host='0.0.0.0', port=8000)