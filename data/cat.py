import sqlalchemy
from data.db_session import SqlAlchemyBase


class cat(SqlAlchemyBase):
    __tablename__ = 'cat'

    category = sqlalchemy.Column(sqlalchemy.String, nullable=False, primary_key=True)
    category_new = sqlalchemy.Column(sqlalchemy.String, nullable=False)
