from fastapi import APIRouter
from sqlalchemy.orm import Session

import db


def user_login(database: Session, user_email: str):
    """
    :param database:
    :param user_email: User Email
    :return: None
    """

    data = (
        database.query(db.User).filter(db.User.email == user_email).first()
    )
    if not data:
        return {"record not found"}
    db.logout = False
    database.commit()


def user_logout(database: Session, user_email: str):
    """

    :param database:
    :param user_email: User Email
    :return: None
    """
    data = (
        database.query(db.User).filter(db.User.email == user_email).first()
    )
    if not data:
        return {"record not found"}
    db.is_logout = True
    database.commit()
