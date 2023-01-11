from Database.Entity.Base import Base
from sqlalchemy.orm import relationship
from sqlalchemy_serializer import SerializerMixin

from sqlalchemy import (
    Integer,
    String,
    Column,
    ForeignKey,
)


class Specialitet(Base, SerializerMixin):
    __tablename__ = "specialitets"
    serialize_rules = (
        "-examinations.specialitet",
        "-passing_grades.specialitet",
    )
    id = Column(Integer, primary_key=True)
    name = Column(String(256), nullable=False)
    form = Column(String(256), nullable=False)
    code = Column(String(10), nullable=False)
    division = Column(String(256), nullable=False)
    profile = Column(String(256), nullable=False)
    higher_education_id = Column(
        Integer, ForeignKey("higher_education.id", ondelete="CASCADE")
    )
    examinations = relationship(
        "Examinations", backref="specialitet", passive_deletes=True
    )
    passing_grades = relationship(
        "PassingGrades", backref="specialitet", passive_deletes=True
    )
