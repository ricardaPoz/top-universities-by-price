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


class Examinations(Base):
    __tablename__ = "examinations"
    id = Column(Integer, primary_key=True)
    examinations = Column(String(256), nullable=False)
    specialitet_id = Column(Integer, ForeignKey("specialitets.id"))
    specialitet = relationship("Specialitet", back_populates="examinations")
