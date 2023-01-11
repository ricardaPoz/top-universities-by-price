from .Controller import ControllerDataBase
from Database.Entity.Examinations import Examinations
from sqlalchemy.orm import Session
import json


class ControllerExaminations(ControllerDataBase):
    def __init__(self, engine):
        self.__engine = engine
        self.__check_list = ["examinations", "specialitet_id"]

    def get(self, id: int):
        session = Session(bind=self.__engine)
        examination = session.query(Examinations).get(id)
        session.close()
        return examination

    def all(self):
        session = Session(bind=self.__engine)
        examinations = session.query(Examinations).all()
        session.close()
        return examinations

    def add(self, **params: dict):
        is_parameter_check = self._parameter_check(
            self.__check_list, {k: v for k, v in params.items() if v != None}
        )
        is_validation = self._validation_check(**params)
        if is_parameter_check[0] and is_validation[0]:
            session = Session(bind=self.__engine)
            examination = Examinations(
                examinations=params.get("examinations"),
                specialitet_id=params.get("specialitet_id"),
            )
            session.add(examination)
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
        examination = session.query(Examinations).get(id)
        session.delete(examination)
        session.commit()
        session.close()
        return {
            "success": True,
        }

    def update(self, id: int, **params: dict):
        is_validation = self._validation_check(**params)
        if is_validation[0]:
            session = Session(bind=self.__engine)
            session.query(Examinations).filter(Examinations.id == id).update(params)
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
        examinations = session.query(Examinations).all()
        examinations_dict = [examinat.to_dict() for examinat in examinations]
        session.close()
        return json.dumps(examinations_dict, ensure_ascii=False)
