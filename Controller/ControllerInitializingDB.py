from Database.Entity import *
from sqlalchemy.orm import Session
from Model.HTTPClient.HTTPClient import HTTPClient
from Model.Parsing.ParserHigherEducation import ParserHigherEducation
from Model.Parsing.ParseSpecialitet import ParseSpecialitet
import Utilities.Config as app_conf


class ControllerInitializingDB:
    def __init__(self, engine):
        self.__engine = engine

    def create_all_tables(self):
        Base.Base.metadata.create_all(self.__engine)

    def fill_data_base(self):
        session = Session(bind=self.__engine)

        html = HTTPClient(app_conf.URL_PARSE).html()
        higher_education = ParserHigherEducation(app_conf.REGEX, html).parse()

        db_educations = []
        db_images = []
        for education in higher_education:
            db_education = HigherEducation.HigherEducation(
                name=education.field_values[3],
                coast=education.field_values[4],
                abbreviation=education.field_values[2],
                detailed_information=education.field_values[0],
                logo=education.field_values[1],
            )
            db_educations.append(db_education)

            session.add(db_education)
            session.flush()

            for image in education.field_values[5]:
                db_image = Images.Images(url=image, higher_education_id=db_education.id)
                db_images.append(db_image)

        session.add_all(db_images)

        for education in db_educations:
            self.__inser_specialitet(education, session)

        session.commit()

        session.close()

    def __inser_specialitet(
        self, education: HigherEducation.HigherEducation, session: Session
    ):
        html = HTTPClient(education.detailed_information, timeouth=200).html()
        specialitets = ParseSpecialitet(html).parse()

        db_specialitets = []
        for specialitet in specialitets:
            db_spec = Specialitet.Specialitet(
                name=specialitet.field_values[0],
                form=specialitet.field_values[1],
                code=specialitet.field_values[2],
                division=specialitet.field_values[3],
                profile=specialitet.field_values[4],
                higher_education_id=education.id,
            )
            session.add(db_spec)
            session.flush()

            db_exam = Examinations.Examinations(
                examinations=", ".join(specialitet.field_values[5]),
                specialitet_id=db_spec.id,
            )
            session.add(db_exam)

            for passing_grades in specialitet.field_values[6]:
                db_passing_grades = PassingGrades.PassingGrades(
                    grades=passing_grades[0] + " " + passing_grades[1],
                    specialitet_id=db_spec.id,
                )
                session.add(db_passing_grades)

        session.add_all(db_specialitets)
        print(f"?????? {education.name} ?????????????????? {len(db_specialitets)}")
