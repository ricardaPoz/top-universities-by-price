from .Controller import ControllerDataBase
from Database.Entity.User import User
from sqlalchemy.orm import Session
import json


class ControllerUser(ControllerDataBase):
    def __init__(self, engine):
        self.__engine = engine

    def get(self, id: int) -> User:
        session = Session(bind=self.__engine)
        user = session.query(User).get(id)
        session.close()
        return user

    def all(self) -> list[User]:
        session = Session(bind=self.__engine)
        users = session.query(User).all()
        session.close()
        return users

    def add(self, **params: dict):
        is_validation = self._validation_check(**params)
        if is_validation[0]:
            session = Session(bind=self.__engine)
            user_name = params.get("user_name")
            password = params.get("password")
            user = User(user_name=user_name)
            user.set_password(password)
            session.add(user)
            session.commit()
            session.close()
            return {
                "success": True,
            }
        else:
            return {
                "success": False,
                "error": "Invalid data format",
                "options": is_validation[1],
            }

    def delete(self, id: int):
        session = Session(bind=self.__engine)
        user = session.query(User).get(id)
        session.delete(user)
        session.close()
        return {
            "success": True,
        }

    def update(self, id: int, **params: dict):
        session = Session(bind=self.__engine)
        password = params.get("password")
        is_validation = True if len(password.strip()) else False
        if is_validation:
            user: User = session.query(User).get(id)
            user.set_password(password)
            session.commit()
            session.close()
            return {
                "success": True,
            }
        else:
            return {"success": False, "error": "Invalid data format"}

    def all_to_json(self):
        session = Session(bind=self.__engine)
        users = session.query(User).all()
        users_json = [user.to_dict() for user in users]
        session.close()
        return json.dumps(users_json, ensure_ascii=False)
