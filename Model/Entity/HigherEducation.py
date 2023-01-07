from .Education import Education


class HigherEducation(Education):
    def __init__(self) -> "HigherEducation":
        self.__field_names: list[str] = [
            "detailedInformation",
            "urlLogo",
            "abbreviation",
            "name",
            "coast",
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
        self.__field_values[0] = "https://tabiturient.ru/vuzu/" + self.__field_values[0]
        self.__field_values[4] = int(self.__field_values[4].replace(" ", ""))

    def to_dict(self) -> dict:
        return dict(zip(self.__field_names, self.__field_values))
