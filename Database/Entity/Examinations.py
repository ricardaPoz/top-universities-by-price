from sqlalchemy import (
    Integer,
    String,
    Column,
    ForeignKey,
)

from Database.Entity.Base import Base
from sqlalchemy_serializer import SerializerMixin


class Examinations(Base, SerializerMixin):
    __tablename__ = "examinations"
    id = Column(Integer, primary_key=True)
    examinations = Column(String(256), nullable=False)
    specialitet_id = Column(Integer, ForeignKey("specialitets.id"))
