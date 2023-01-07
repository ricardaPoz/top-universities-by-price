from Database.Entity.Base import Base
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
    ForeignKey,
)


class PassingGrades(Base):
    __tablename__ = "passing_grades"
    id = Column(Integer, primary_key=True)
    grades = Column(String(256), nullable=False)
    specialitet_id = Column(Integer, ForeignKey("specialitets.id"))
    specialitet = relationship("Specialitet", back_populates="passing_grades")
