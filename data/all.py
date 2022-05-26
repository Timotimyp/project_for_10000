import sqlalchemy
from data.db_session import SqlAlchemyBase


class all(SqlAlchemyBase):
    __tablename__ = 'all'

    category = sqlalchemy.Column(sqlalchemy.String, nullable=False, primary_key=True)
    position = sqlalchemy.Column(sqlalchemy.String, nullable=False)
