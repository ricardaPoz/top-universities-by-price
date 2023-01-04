from Parsing import Parsing
from Entity.Specialitet import Specialitet


class ParseSpecialitet(Parsing):
    def __init__(self, html: str) -> "ParseSpecialitet":
        self.__html = html

    def parse(self):
        ...
