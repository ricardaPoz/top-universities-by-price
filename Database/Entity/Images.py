from Database.Entity.Base import Base
from sqlalchemy.orm import relationship

from sqlalchemy import Integer, String, Column, ForeignKey


class Images(Base):
    __tablename__ = "images"
    id = Column(Integer, primary_key=True)
    url = Column(String(256), nullable=False)
    higher_education_id = Column(Integer, ForeignKey("higher_education.id"))
    higher_education = relationship("HigherEducation", back_populates="image")
