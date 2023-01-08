from Database.Entity.Base import Base
from sqlalchemy_serializer import SerializerMixin
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


class PassingGrades(Base, SerializerMixin):
    __tablename__ = "passing_grades"
    id = Column(Integer, primary_key=True)
    grades = Column(String(256), nullable=False)
    specialitet_id = Column(Integer, ForeignKey("specialitets.id"))
