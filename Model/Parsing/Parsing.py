from abc import abstractclassmethod, ABC


class Parsing(ABC):
    @abstractclassmethod
    def parse(self):
        pass
