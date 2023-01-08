from Database.Entity.Base import Base
from sqlalchemy.orm import relationship

from sqlalchemy import Integer, String, Column, ForeignKey
from sqlalchemy_serializer import SerializerMixin


class Images(Base, SerializerMixin):
    __tablename__ = "images"
    id = Column(Integer, primary_key=True)
    url = Column(String(256), nullable=False)
    higher_education_id = Column(Integer, ForeignKey("higher_education.id"))
