from sqlalchemy import Column, String, Boolean
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

import os
import dotenv

dotenv.load_dotenv()

DATABASE_PASS = os.getenv("DATABASE_PASS")
DATABASE_USER = os.getenv("DATABASE_USER")
DATABASE_DB = os.getenv("DATABASE_DB")
DATABASE_URL = os.getenv("DATABASE_URL")
DB_CONNECTION_LINK = "postgresql+asyncpg://{}:{}@{}/{}".format(
    DATABASE_USER,
    DATABASE_PASS,
    DATABASE_URL,
    DATABASE_DB,
)

engine = create_engine(DB_CONNECTION_LINK)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


class User(Base):
    __tablename__ = "USERS"

    email = Column(String, primary_key=True)
    password = Column(String, nullable=True)
    is_ops = Column(Boolean, nullable=True)
    is_active = Column(Boolean, nullable=True)
    is_logout = Column(Boolean, nullable=True)


def get_db():
    try:
        database = SessionLocal()
        yield database
    finally:
        database.close()


db = get_db()
Base.metadata.create_all(bind=engine)
