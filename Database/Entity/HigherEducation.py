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


class HigherEducation(Base):
    __tablename__ = "higher_education"
    id = Column(Integer)
    name = Column(String(256), nullable=False)
    coast = Column(Integer(), nullable=False)
    abbreviation = Column(String(15), nullable=False)
    detailed_information = Column(String(256), nullable=False)

    __table_args__ = (
        PrimaryKeyConstraint("id", name="higher_education_pk"),
        UniqueConstraint("name"),
    )
