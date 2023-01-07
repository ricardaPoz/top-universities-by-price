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
    ForeignKey
)


class Specialitet(Base):
    __tablename__ = "specialitets"
    id = Column(Integer, primary_key=True)
    name = Column(String(256), nullable=False)
    form = Column(String(256), nullable=False)
    code = Column(String(10), nullable=False)
    division = Column(String(256), nullable=False)
    profile = Column(String(256), nullable=False)
    higher_education_id = Column(Integer, ForeignKey("higher_education.id"))
    higher_education = relationship("HigherEducation", back_populates="specialitet")
    examinations = relationship("Examinations", back_populates="specialitet")
    passing_grades = relationship("PassingGrades", back_populates="specialitet")

    
