from abc import abstractclassmethod, ABC, abstractproperty


class Education(ABC):
    @abstractproperty
    def get_field_values(self) -> list[str]:
        pass

    @abstractproperty
    def get_field_names(self) -> list[str]:
        pass

    @abstractclassmethod
    def set_field_values(self):
        pass
