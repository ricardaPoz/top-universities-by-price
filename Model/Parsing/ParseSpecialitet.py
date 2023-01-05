from .Parsing import Parsing
from ..Entity.Specialitet import Specialitet
from bs4 import BeautifulSoup, ResultSet, Tag


class ParseSpecialitet(Parsing):
    def __init__(self, html: str) -> "ParseSpecialitet":
        self.__html = html

    def parse(self) -> list[Specialitet]:
        soup = BeautifulSoup(self.__html, "lxml")

        specialitets = []

        elements_headnap: ResultSet = soup.find_all("div", class_="headnap")
        for element_headnap in elements_headnap:
            element_tag: Tag = element_headnap

            name = element_tag.find(
                "b", attrs={"style": "text-transform:uppercase;"}
            ).contents[0]

            speciality = element_tag.find(
                "span", attrs={"style": "color:#8D8D8D;", "class": "font2"}
            ).contents[0]

            elements_mobpadd = element_tag.find_all("div", class_="mobpadd20-3")
            for element_mobpadd in elements_mobpadd:
                specialitet = Specialitet()

                element: Tag = element_mobpadd

                division_profile: ResultSet = element.find_all("span", class_="font2")
                division = division_profile[0].contents[1]
                profile = division_profile[1].contents[1]

                examinations: list[str] = [
                    examination.contents[0].replace("\n", "")
                    for examination in element.select(
                        'div[class="p10 font11"] > center > b'
                    )
                ]

                passing_grades = []

                for passing_score in element.select(
                    'table[class="cirfloat cirfloatmargin"] table[class="circ2 circ2unique"] td'
                ):
                    score = passing_score.find("b").contents[0]
                    training_form = passing_score.find("span", class_="font0").contents[
                        0
                    ]
                    passing_grades.append((score, training_form))

                specialitet.field_values = [
                    name,
                    speciality,
                    division,
                    profile,
                    examinations,
                    passing_grades,
                ]

                specialitets.append(specialitet)

        return specialitets
