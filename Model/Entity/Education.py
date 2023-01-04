from abc import abstractclassmethod, ABC, abstractproperty


class Education(ABC):
    @abstractproperty
    def field_values(self) -> list[str]:
        pass

    @abstractproperty
    def field_names(self) -> list[str]:
        pass

    @field_values.setter
    @abstractproperty
    def field_values(self, field_values: list[str]):
        pass
