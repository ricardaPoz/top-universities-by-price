from ..Utilities.create_table import Base
from sqlalchemy import (
    Table,
    Index,
    Integer,
    String,
    Column,
    Text,
    PrimaryKeyConstraint,
    UniqueConstraint,
    ForeignKeyConstraint,
)

class Specialitet(Base):
    __tablename__ = "specialitets"
    