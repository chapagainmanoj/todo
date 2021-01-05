from starlette.config import Config
from pathlib import Path

config = Config('.env')

DATABASE_URL = config('DATABASE_URL')
BASE_DIR = Path(__file__).parent
DEBUG = config("DEBUG", cast=bool, default=True)