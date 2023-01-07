from Database.Entity import *
from sqlalchemy.orm import Session, sessionmaker
from Model.HTTPClient.HTTPClient import HTTPClient
from Model.Parsing.ParserHigherEducation import ParserHigherEducation
from Model.Parsing.ParseSpecialitet import ParseSpecialitet


class Controller:
    def __init__(self, engine):
        self.__engine = engine

    def create_tables(self):
        config.Base.metadata.create_all(self.__engine)

    def get_education(self):
        html = HTTPClient("https://tabiturient.ru/vuzcost/").html()
        regex = r"(?ms)<a href=\"https://tabiturient\.ru/vuzu/(.*?)\".*?src=\"(.*?)\".*?<b>(.*?)<.*?<br>[^\t](.*?)<.*?<b>(.*?)<"

        educations = ParserHigherEducation(regex, html).parse()

        return educations

    def add_education(self):
        html = HTTPClient("https://tabiturient.ru/vuzcost/").html()
        regex = r"(?ms)<a href=\"https://tabiturient\.ru/vuzu/(.*?)\".*?src=\"(.*?)\".*?<b>(.*?)<.*?<br>[^\t](.*?)<.*?<b>(.*?)<"
        educations = ParserHigherEducation(regex, html).parse()
        
        session = Session(bind=self.__engine)

        db_educations = []

        for education in educations:
            db_education = HigherEducation.HigherEducation(
                name = education.field_values[3],
                coast = education.field_values[4],
                abbreviation = education.field_values[2],
                detailed_information = education.field_values[0],
            )
            db_educations.append(db_education)

        session.add_all(db_educations)
        session.commit()
        session.close()


        

    def add_specialitet(self):
        
        session = Session(bind=self.__engine)

        education = session.query(HigherEducation.HigherEducation).filter(HigherEducation.HigherEducation.id == 1).first()
        
        html = HTTPClient(education.detailed_information).html()
        specialitets = ParseSpecialitet(html).parse()


        for spec in specialitets:
            db_spec = Specialitet.Specialitet(
                name = spec.field_values[0],
                form = spec.field_values[1],
                code = spec.field_values[2],
                division = spec.field_values[3],
                profile = spec.field_values[4],
                higher_education_id = 1
            )

            session.add(db_spec)
            session.flush()
            
            db_exam = Examinations.Examinations(
                examinations = ", ".join(spec.field_values[5]),
                specialitet_id = db_spec.id
            )

            session.add(db_exam)

            session.commit()

        session.close()

            
            


        # html = HTTPClient("https://tabiturient.ru/vuzcost/").html()

