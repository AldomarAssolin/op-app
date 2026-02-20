import os
from pathlib import Path


class BaseConfig:
    BASE_DIR = Path(__file__).resolve().parent.parent
    DATABASE_URL = os.getenv("DATABASE_URL", f"sqlite:///{BASE_DIR}/op_app.db")
    SECRET_KEY = os.getenv("SECRET_KEY", "dev-secret")


class DevConfig(BaseConfig):
    DEBUG = True


class ProdConfig(BaseConfig):
    DEBUG = False