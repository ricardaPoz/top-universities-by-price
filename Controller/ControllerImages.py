from .Controller import ControllerDataBase
from Database.Entity.Images import Images
from sqlalchemy.orm import Session
import json


class ControllerImages:
    def __init__(self, engine):
        self.__engine = engine

    def get(self, id: int):
        session = Session(bind=self.__engine)
        image = session.query(Images).get(id)
        session.close()
        return image

    def all(self):
        session = Session(bind=self.__engine)
        images = session.query(Images).all()
        session.close()
        return images

    def add(self, **params: dict):
        is_validation = self._validation_check(**params)
        if is_validation[0]:
            session = Session(bind=self.__engine)
            image = Images(
                url=params.get("url"),
                higher_education_id=params.get("higher_education_id"),
            )

            session.add(image)
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
        image = session.query(Images).get(id)
        session.delete(image)
        session.close()
        return {
            "success": True,
        }

    def update(self, id: int, **params: dict):
        is_validation = self._validation_check(**params)
        if is_validation[0]:
            session = Session(bind=self.__engine)
            session.query(Images).filter(Images.id == id).update(params)
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
        images = session.query(Images).all()
        images_json = [image.to_dict() for image in images]
        session.close()
        return json.dumps(images_json, ensure_ascii=False)
