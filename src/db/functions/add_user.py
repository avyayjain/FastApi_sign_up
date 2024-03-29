from src.common.utils.pwd_helper import get_password_hash
from src.db.database import Users
from src.db.errors import DataInjectionError, DatabaseErrors, DatabaseConnectionError
from src.db.utils import DBConnection


def create_user(user_email: str, password: str):
    """
    :param user_email: User Email
    :param password: User Password
    :return: None
    """
    try:
        with DBConnection(False) as db:
            try:
                user = Users(
                    # name=user_name,
                    email_id=user_email,
                    hashed_password=get_password_hash(password),

                )
                db.add(user)
                db.commit()
                return {"message": "user added successfully"}
            except Exception as e:
                print(e)
                raise DataInjectionError

    except DatabaseErrors:
        raise
    except Exception as e:
        print(e)
        raise DatabaseConnectionError
