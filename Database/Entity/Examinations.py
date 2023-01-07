from sqlalchemy import (
    Integer,
    String,
    Column,
    ForeignKey,
)
from sqlalchemy.orm import relationship

from Database.Entity.Base import Base


class Examinations(Base):
    __tablename__ = "examinations"
    id = Column(Integer, primary_key=True)
    examinations = Column(String(256), nullable=False)
    specialitet_id = Column(Integer, ForeignKey("specialitets.id"))
    specialitet = relationship("Specialitet", back_populates="examinations")
