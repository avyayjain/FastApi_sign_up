from sqlalchemy import Column, String, Boolean
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = "postgresql://ez_api:somepwd123@localhost/ez_api_db"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
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

# import jwt
# from fastapi.security import OAuth2PasswordBearer
# from sqlalchemy.orm import sessionmaker
# from sqlalchemy import Boolean, Column, String
# from typing import Optional
# from pydantic import BaseModel
# from datetime import datetime, timedelta
# from sqlalchemy import dialects
# import jose
#
# SECRET_KEY = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
#
# # SQLALCHEMY_DATABASE_URL = "sqlite:///./sql_app.db"
# DB_CONNECTION_LINK = "postgresql://ez_api:somepwd123@localhost:5432/ez_api_db"
#
# engine = create_engine(
#     DB_CONNECTION_LINK, connect_args={"check_same_thread": False}
# )
# SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
#
# Base = declarative_base()
# oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")
#
#
# class User(BaseModel):
#     __tableName__ = "USERS"
#
#     email = Column(String, primary_key=True, Index=True)
#     password = Column(String)
#     is_ops = Column(Boolean)
#     is_active = Column(Boolean, Default=True)
#
#
# class Token(BaseModel):
#     access_token: str
#     token_type: str
#
#
# class TokenData(BaseModel):
#     username: Optional[str] = None
#
#
# class UserInDB(User):
#     hashed_password: str
#
#
# class AuthUser(BaseModel):
#     username: str
#     password: str
#
#
# class UserInDB(User):
#     hashed_password: str
#
#
# def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
#
#     to_encode = data.copy()
#     if expires_delta:
#         expire = datetime.utcnow() + expires_delta
#     else:
#         expire = datetime.utcnow() + timedelta(minutes=60)
#     to_encode.update({"exp": expire})
#     encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm="HS256")
#     return encoded_jwt
#
#
# def create_user(user_email: str, password: str, resource_id, disabled=False):
#     # con = sqlalchemy.di
#     # with DBConnection(DB_CONNECTION_LINK, False) as db:
#     user = User(
#         email_id=user_email,
#         disable=disabled,
#         logout=True,
#         resource_id=resource_id,
#         user_type="ops",
#     )
