from .Parsing import Parsing
from ..Entity.HigherEducation import HigherEducation
import re


class ParserHigherEducation(Parsing):
    def __init__(self, regex: str, html: str) -> "ParserHigherEducation":
        self.__regex = regex
        self.__html = html

    def parse(self) -> list[HigherEducation]:
        higher_educations: list[HigherEducation] = []
        elements = re.findall(self.__regex, self.__html)

        for element in elements:
            arr: list[str] = []
            for value in element:
                arr.append(value)
            education: HigherEducation = HigherEducation()
            education.field_values = arr
            higher_educations.append(education)

        return higher_educations
