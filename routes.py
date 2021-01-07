from auth.routes import routes as auth_routes
from todo.routes import routes as todo_routes

routes = []
routes += auth_routes
routes += todo_routes

