import os

basedir = os.path.abspath(os.path.dirname(__file__))
SQLALCHEMY_ECHO = False
SQLALCHEMY_TRACK_MODIFICATIONS = True

user = os.environ["POSTGRES_USER"]
password = os.environ["POSTGRES_PASSWORD"]
hostname = os.environ["POSTGRES_HOST"]
port = os.environ["POSTGRES_PORT"]
database = os.environ["POSTGRES_DB"] 

SQLALCHEMY_DATABASE_URI = (
    f"postgresql+psycopg2://{user}:{password}@{hostname}:{port}/{database}"
)
SQLALCHEMY_TRACK_MODIFICATIONS = False