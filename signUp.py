from fastapi import APIRouter, HTTPException, Depends
from pydantic import BaseModel
from pydantic import EmailStr
from sqlalchemy.orm import Session
from db import db
import functions

signUp_ops_router = APIRouter()
signUp_client_router = APIRouter()


class UserDetails(BaseModel):
    email: EmailStr
    password: str
    is_ops: bool
    is_active: bool
    is_logout: bool


@signUp_ops_router.post("/signUp_ops/")
def signup_ops(user_data: UserDetails, database: Session = Depends(db.get_db)):
    """add new user"""
    user = functions.check_user_exist(database, user_data.email)

    if user:
        raise HTTPException(status_code=409,
                            detail="Email already registered.")
    signup_obj = db.User(
        email=user_data.email,
        password=user_data.password,
        is_ops=True,
        is_active=True,
        is_logout=False
    )

    signedUp_user = functions.create_user(database, signup_obj)
    return {"status": "registered successfully",
            "data": signedUp_user}


@signUp_client_router.post("/signUp_client/")
def signup_client(user_data: UserDetails, database: Session = Depends(db.get_db)):
    """add new user"""
    user = functions.check_user_exist(database, user_data.email)

    if user:
        raise HTTPException(status_code=409,
                            detail="Email already registered.")
    signup_obj = db.User(
        email=user_data.email,
        password=user_data.password,
        is_ops=False,
        is_active=True,
        is_logout=False
    )
    signedUp_user = functions.create_user(database, signup_obj)
    return {"status": "registered successfully",
            "data": signedUp_user}
