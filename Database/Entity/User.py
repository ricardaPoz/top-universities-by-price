from Database.Entity.Base import Base
from sqlalchemy_serializer import SerializerMixin

from sqlalchemy import (
    Integer,
    String,
    Column,
    PrimaryKeyConstraint,
    UniqueConstraint,
)

# role = Column(String(256), nullable=False)


class User(Base, SerializerMixin):
    __tablename__ = "users"
    id = Column(Integer)
    user_name = Column(String(256), nullable=False)
    password = Column(String(256), nullable=False)

    __table_args__ = (
        PrimaryKeyConstraint("id", name="user_pk"),
        UniqueConstraint("user_name"),
    )
