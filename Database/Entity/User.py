from ..Utilities.create_table import Base
from sqlalchemy import (
    Integer,
    String,
    Column,
    PrimaryKeyConstraint,
    UniqueConstraint,
)


class User(Base):
    __tablename__ = "users"
    id = Column(Integer)
    user_name = Column(String(256), nullable=False)
    password = Column(String(256), nullable=False)
    role = Column(String(256), nullable=False)

    __table_args__ = (
        PrimaryKeyConstraint("id", name="user_pk"),
        UniqueConstraint("user_name"),
    )
