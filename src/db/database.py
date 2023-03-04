from sqlalchemy import (
    Column,
    String,
)
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Users(Base):
    __tablename__ = "user_info"

    email_id = Column(String, primary_key=True, nullable=False)
    hashed_password = Column(String, nullable=False)


