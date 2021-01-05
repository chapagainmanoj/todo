from starlette.applications import Starlette

from routes import routes
from settings import DEBUG
from resources import database
from middleware import middleware


app = Starlette(
    debug=DEBUG, 
    routes=routes, 
    middleware=middleware,
    on_startup=[database.connect],
    on_shutdown=[database.disconnect]
    )