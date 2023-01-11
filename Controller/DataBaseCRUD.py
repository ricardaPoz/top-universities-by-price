from .Controller import ControllerDataBase
from .ControllerUser import ControllerUser
from .ControllerHigherEducation import ControllerHigherEducation
from .ControllerImages import ControllerImages
from .ControllerSpecialitet import ControllerSpecialitet
from .ControllerExaminations import ControllerExaminations
from .ControllerPassingGrades import ControllerPassingGrades


class DataBaseCRUD:
    def __init__(self, controller_data_base: ControllerDataBase) -> None:
        self.__controller_data_base = controller_data_base

    def get(self, id: int):
        return self.__controller_data_base.get(id)

    def all(self):
        return self.__controller_data_base.all()

    def add(self, **params: dict):
        return self.__controller_data_base.add(**params)

    def delete(self, id: int):
        return self.__controller_data_base.delete(id)

    def update(self, id: int, **params: dict):
        return self.__controller_data_base.update(id, **params)

    def all_to_json(self):
        return self.__controller_data_base.all_to_json()
