from Database.Entity.config import Base
from sqlalchemy.orm import relationship
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
    abbreviation = Column(String(100), nullable=False)
    detailed_information = Column(String(256), nullable=False)
    specialitet = relationship("Specialitet", back_populates="higher_education")
    
    __table_args__ = (
        PrimaryKeyConstraint("id", name="higher_education_pk"),
        UniqueConstraint("name"),
    )
