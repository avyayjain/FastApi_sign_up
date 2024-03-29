import datetime

from sqlalchemy import create_engine, inspect
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker

from src.common.utils.constants import DB_CONNECTION_LINK, ASYNC_DB_CONNECTION_LINK


class CustomBaseModel:
    """ Generalize _init, __repr_ and to_json
        Based on the models columns """

    print_filter = ()

    def _repr_(self) -> str:
        """ Define a base way to print models
            Columns inside `print_filter` are excluded """
        return "%s(%s)" % (
            self._class.__name_,
            {
                column: value
                for column, value in self._to_dict().items()
                if column not in self.print_filter
            },
        )

    to_json_filter = ()

    @property
    def json(self) -> dict:
        """ Define a base way to jsonify models
            Columns inside `to_json_filter` are excluded """
        return {
            column: value if not isinstance(value, datetime.date) else value.isoformat()
            for column, value in self._to_dict().items()
            if column not in self.to_json_filter
        }

    def _to_dict(self) -> dict:
        """ This would more or less be the same as a `to_json`
            But putting it in a "private" function
            Allows to_json to be overriden without impacting _repr_
            Or the other way around
            And to add filter lists """
        return {
            column.key: getattr(self, column.key)
            for column in inspect(self._class_).attrs
        }


engine = create_engine(DB_CONNECTION_LINK)


class DBConnection:
    """SQLAlchemy database connection"""

    def __init__(self, expire_commit=None):
        self.expire_commit = expire_commit if expire_commit is None else True
        self.session = None

    def __enter__(self):
        self.session = sessionmaker(bind=engine, expire_on_commit=self.expire_commit)()
        return self.session

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.session.close()


async_engine = create_async_engine(
    ASYNC_DB_CONNECTION_LINK, future=True
)


class ASYNCDBConnection:
    """SQLAlchemy database connection"""

    def __init__(self, expire_commit=None):
        self.expire_commit = expire_commit
        self.session = None

    async def __aenter__(self):
        self.session = AsyncSession(bind=async_engine, expire_on_commit=self.expire_commit)
        return self.session

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        await self.session.close()


def engine_creator(user, passwd, hostname, dbname, dbtype):
    """Creates an sqlalchemy engine using the provided cred arguments"""
    return create_engine(
        "{dbtype}://{user}:{passwd}@{hostname}/{dbname}".format(
            dbtype=dbtype, user=user, passwd=passwd, hostname=hostname, dbname=dbname
        )
    )
