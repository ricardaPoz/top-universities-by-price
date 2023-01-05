from .Education import Education


class Specialitet(Education):
    def __init__(self) -> "Specialitet":
        self.__field_names: list[str] = [
            "name",
            "speciality",
            "division",
            "profile",
            "examinations",
            "passing_grades",
        ]
        self.__field_values: list[str] = None

    @property
    def field_values(self) -> list[str]:
        return self.__field_values

    @property
    def field_names(self) -> list[str]:
        return self.__field_names

    @field_values.setter
    def field_values(self, field_values: list[str]):
        self.__field_values = field_values

    def to_dict(self) -> dict:
        return dict(zip(self.__field_names, self.__field_values))
