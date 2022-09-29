# import re
import email
from datetime import datetime, timedelta
from typing import Optional
from fastapi import Depends, HTTPException, status, APIRouter
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt
from pydantic import BaseModel
from sqlalchemy.orm import Session

import db
from functions import find_user_pass
from logout import user_login, user_logout

login_router = APIRouter()
logout_router = APIRouter()

SECRET_KEY = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
ALGORITHM = "HS256"


class Token(BaseModel):
    access_token: str
    refresh_token: str


class AuthUser(BaseModel):
    username: str
    password: str


class LogoutUser(BaseModel):
    email: str


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    email: Optional[str] = None


class UserBase(BaseModel):
    email: str
    is_active: Optional[bool] = None
    logout: Optional[bool] = None
    password: bool


class UserInDB(UserBase):
    password: str


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


def get_user(user_email: str):
    """
    :param user_email: User Email
    """

    password, is_active, is_logout, resource_id = find_user_pass(user_email)

    return UserInDB(
        resource_id=resource_id,
        email=user_email,
        diable=is_active,
        password=password,
        logout=is_logout,
    )


def authenticate_user(user_email: str, password: str, database: Session):
    password, is_active, logout = find_user_pass(user_email, database=database)

    return UserInDB(

        email=user_email,
        diable=is_active,
        password=password,
        logout=logout,
    )


def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    """
    This function is use to create access token

    @param data: Data required to for jwt creation
    @type data: Dict
    @param expires_delta: expiry time
    @type expires_delta: timedelta
    @return: encoded token
    @rtype: str
    """
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


async def get_current_user(token: str = Depends(oauth2_scheme)):
    """

    @param token: token is used to check credentials
    @type token: str
    @return: user object
    @rtype: object
    """
    payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
    email: str = payload.get("sub")
    if email is None:
        return {"email id not found"}
    token_data = TokenData(email=email)
    user = get_user(user_email=token_data.email)

    if user is None:
        return {"user not found"}


async def get_current_active_user(current_user: UserBase = Depends(get_current_user)):
    """

    @param current_user: User Object
    @type current_user: Object
    @return: User Object
    @rtype: Object
    """
    if current_user.disabled:
        data = "\n User Email {} , Disabled User".format(str(current_user.email))
    if current_user.logout:
        return current_user


@login_router.post("", response_model=Token)
async def login_for_access_token(form_data: AuthUser, database: Session = Depends(db.get_db)):
    user = authenticate_user(form_data.username, form_data.password, database=database)
    if not user:
        return {"user not found"}
    user_login(database=database, user_email=user.email)
    access_token_expires = timedelta(minutes=60)
    access_token = create_access_token(
        data={"sub": user.email}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}


@logout_router.post("/logout")
async def logout_endpoint(current_user: UserBase = Depends(get_current_active_user)):
    if not current_user:
        return {"wrong credentials"}
    user_logout(current_user.email)

    return {"message": "success"}
