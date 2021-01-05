import databases
from starlette.config import Config
from sqlalchemy import MetaData

config = Config('.env')
DATABASE_URL = config('DATABASE_URL')

metadata = MetaData()
database = databases.Database(DATABASE_URL)