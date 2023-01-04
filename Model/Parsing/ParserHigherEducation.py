from Parsing import Parsing
from Entity.HigherEducation import HigherEducation


class ParserHigherEducation(Parsing):
    def __init__(self, regex: str, html: str) -> "ParserHigherEducation":
        self.__regex = regex
        self.__html = html

    def parse(self) -> list[HigherEducation]:
        ...
