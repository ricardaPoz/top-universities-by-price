from .Controller import ControllerDataBase
from Database.Entity.HigherEducation import HigherEducation
from sqlalchemy.orm import Session
import json


class ControllerHigherEducation(ControllerDataBase):
    def __init__(self, engine):
        self.__engine = engine

    def get(self, id: int) -> HigherEducation:
        session = Session(bind=self.__engine)
        higher_education = session.query(HigherEducation).get(id)
        session.close()
        return higher_education

    def all(self) -> list[HigherEducation]:
        session = Session(bind=self.__engine)
        higher_educations = session.query(HigherEducation).all()
        session.close()
        return higher_educations

    def add(self, **params: dict):
        is_validation = self._validation_check(**params)
        if is_validation[0] is True:
            session = Session(bind=self.__engine)
            higher_education = HigherEducation(
                name=params.get("name"),
                coast=params.get("coast"),
                abbreviation=params.get("abbreviation"),
                detailed_information=params.get("detailed_information"),
                logo=params.get("logo"),
            )
            session.add(higher_education)
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
        higher_education = session.query(HigherEducation).get(id)
        session.delete(higher_education)
        session.close()
        return {
            "success": True,
        }

    def update(self, id: int, **params):
        is_validation = self._validation_check(**params)
        if is_validation[0]:
            session = Session(bind=self.__engine)
            session.query(HigherEducation).filter(HigherEducation.id == id).update(
                params
            )
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

    def all_to_json(self):
        session = Session(bind=self.__engine)
        higher_educations = session.query(HigherEducation).all()
        higher_educations_dict = [
            education.to_dict() for education in higher_educations
        ]
        session.close()
        return json.dumps(higher_educations_dict, ensure_ascii=False)
