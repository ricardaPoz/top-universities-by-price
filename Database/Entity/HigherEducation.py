from sqlalchemy import (
    Integer,
    String,
    Column,
    PrimaryKeyConstraint,
    UniqueConstraint,
)
from sqlalchemy.orm import relationship
from sqlalchemy_serializer import SerializerMixin

from Database.Entity.Base import Base


class HigherEducation(Base, SerializerMixin):
    __tablename__ = "higher_education"
    serialize_rules = (
        "-specialitet.higher_education",
        "-image.higher_education",
        "-specialitet.examinations",
        "-specialitet.passing_grades",
    )
    serialize_only = (
        "id",
        "name",
        "coast",
        "abbreviation",
        "detailed_information",
        "image",
    )

    id = Column(Integer)
    name = Column(String(256), nullable=False)
    coast = Column(Integer(), nullable=False)
    abbreviation = Column(String(100), nullable=False)
    detailed_information = Column(String(256), nullable=False)
    specialitet = relationship("Specialitet", backref="higher_education")
    image = relationship("Images", backref="higher_education")
    __table_args__ = (
        PrimaryKeyConstraint("id", name="higher_education_pk"),
        UniqueConstraint("name"),
    )
