from .Controller import ControllerDataBase
from Database.Entity.Specialitet import Specialitet
from sqlalchemy.orm import Session
import json


class ControllerSpecialitet(ControllerDataBase):
    def __init__(self, engine):
        self.__engine = engine
        self.__check_list = [
            "name",
            "form",
            "code",
            "division",
            "profile",
        ]

    def get(self, id: int):
        session = Session(bind=self.__engine)
        specialitet = session.query(Specialitet).get(id)
        session.close()
        return specialitet

    def all(self):
        session = Session(bind=self.__engine)
        specialitets = session.query(Specialitet).all()
        session.close()
        return specialitets

    def add(self, **params: dict):
        is_parameter_check = self._parameter_check(
            self.__check_list, {k: v for k, v in params.items() if v != None}
        )
        is_validation = self._validation_check(**params)
        if is_parameter_check[0] and is_validation[0]:
            session = Session(bind=self.__engine)
            specialitet = Specialitet(
                education_id=params.get("education_id"),
                name=params.get("name"),
                form=params.get("form"),
                code=params.get("code"),
                division=params.get("division"),
                profile=params.get("profile"),
            )
            session.add(specialitet)
            session.commit()
            session.close()

            return {
                "success": True,
            }
        else:
            return {
                "success": False,
                "error": "Invalid data format",
                "options": is_parameter_check[1] if not is_parameter_check[0] else is_validation[1],

            }

    def delete(self, id: int):
        session = Session(bind=self.__engine)
        specialitet = session.query(Specialitet).get(id)
        session.delete(specialitet)
        session.commit()
        session.close()
        return {
            "success": True,
        }

    def update(self, id: int, **params: dict):
        is_validation = self._validation_check(**params)
        if is_validation[0]:
            session = Session(bind=self.__engine)
            session.query(Specialitet).filter(Specialitet.id == id).update(params)
            session.commit()
            session.close()
        else:
            return {
                "success": False,
                "error": "Invalid data format",
                "options": is_validation[1],
            }

    def all_to_json(self):
        session = Session(bind=self.__engine)
        specialitets = session.query(Specialitet).all()
        specialitets_dict = [specialitet.to_dict() for specialitet in specialitets]
        session.close()
        return json.dumps(specialitets_dict, ensure_ascii=False)
