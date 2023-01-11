from .Controller import ControllerDataBase
from Database.Entity.PassingGrades import PassingGrades
from sqlalchemy.orm import Session
import json


class ControllerPassingGrades(ControllerDataBase):
    def __init__(self, engine):
        self.__engine = engine
        self.__check_list = ["grades", "specialitet_id"]

    def get(self, id: int):
        session = Session(bind=self.__engine)
        passing = session.query(PassingGrades).get(id)
        session.close()
        return passing

    def all(self):
        session = Session(bind=self.__engine)
        passings = session.query(PassingGrades).all()
        session.close()
        return passings

    def add(self, **params: dict):
        is_parameter_check = self._parameter_check(
            self.__check_list, {k: v for k, v in params.items() if v != None}
        )
        is_validation = self._validation_check(**params)
        if is_parameter_check[0] and is_validation[0]:
            session = Session(bind=self.__engine)
            passing = PassingGrades(
                grades=params.get("grades"), specialitet_id=params.get("specialitet_id")
            )
            session.add(passing)
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
        passing = session.query(PassingGrades).get(id)
        session.delete(passing)
        session.commit()
        session.close()
        return {
            "success": True,
        }

    def update(self, id: int, **params: dict):
        is_validation = self._validation_check(**params)
        if is_validation[0]:
            session = Session(bind=self.__engine)
            session.query(PassingGrades).filter(PassingGrades.id == id).update(params)
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
        passings = session.query(PassingGrades).all()
        passings_dict = [passing.to_dict() for passing in passings]
        session.close()
        return json.dumps(passings_dict, ensure_ascii=False)
