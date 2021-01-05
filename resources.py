import databases
import settings
from sqlalchemy import MetaData

metadata = MetaData()
database = databases.Database(settings.DATABASE_URL)