import os
import dotenv

dotenv.load_dotenv()

SECRET_KEY = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 600
JWT_SUBJECT = "access"
JWT_ALGORITHM = "HS256"

DATABASE_PASS = os.getenv("DATABASE_PASS")
DATABASE_USER = os.getenv("DATABASE_USER")
DATABASE_DB = os.getenv("DATABASE_DB")
DATABASE_URL = os.getenv("DATABASE_URL")
#
# DB_CONNECTION_LINK = "postgres://{}:{}@{}/{}".format(
#     DATABASE_USER,
#     DATABASE_PASS,
#     DATABASE_URL,
#     DATABASE_DB,
# )

DB_CONNECTION_LINK = "postgresql://{}:{}@{}/{}".format(
    "postgres",
    "1234",
    "127.0.0.1:5432",
    "yeh_zindagi",
)

ASYNC_DB_CONNECTION_LINK = "postgresql+asyncpg://{}:{}@{}/{}".format(
    "postgres",
    "1234",
    "127.0.0.1:5432",
    "yeh_zindagi",
)