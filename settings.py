from starlette.config import Config
from pathlib import Path

config = Config('.env')


BASE_DIR = Path(__file__).parent
DATABASE_URL = config('DATABASE_URL')
DEBUG = config("DEBUG", cast=bool, default=False)

# openssl rand -hex 32
SECRET_KEY=config("SECRET_KEY", cast=str, default='')