from Database.Entity.Base import Base
from sqlalchemy_serializer import SerializerMixin
from werkzeug.security import generate_password_hash, check_password_hash

from flask_login import UserMixin 

from sqlalchemy import (
    Integer,
    String,
    Column,
    PrimaryKeyConstraint,
    UniqueConstraint,
)


class User(Base, SerializerMixin, UserMixin):
    __tablename__ = "users"

    serialize_only = (
        "id",
        "user_name",
    )

    id = Column(Integer, primary_key=True)
    user_name = Column(String(256), nullable=False)
    password = Column(String(256), nullable=False)

    __table_args__ = (UniqueConstraint("user_name"),)

    def __repr__(self) -> str:
        return "<{}:{}>".format(self.id, self.user_name)

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def chech_password(self, password):
        return check_password_hash(self.password, password)
    
    def is_authenticated(self):
        return True
    
    def is_active():
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return str(self.id)
