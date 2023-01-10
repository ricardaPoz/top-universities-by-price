from Database.Entity import *
from sqlalchemy.orm import Session
from Model.HTTPClient.HTTPClient import HTTPClient
from Model.Parsing.ParserHigherEducation import ParserHigherEducation
from Model.Parsing.ParseSpecialitet import ParseSpecialitet
import Utilities.Config as app_conf
import json


class Controller:
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
        print(f"Вуз {education.name} добавлено {len(db_specialitets)}")

    def __all_higher_educations(self, session):
        higher_educations = session.query(HigherEducation.HigherEducation).all()
        higher_educations = higher_educations
        return higher_educations

    def get_all_higher_educations(self) -> str:
        session = Session(bind=self.__engine)

        higher_educations = self.__all_higher_educations(session)
        higher_educations = higher_educations[:4]

        response = [education.to_dict() for education in higher_educations]

        session.close()
        return json.dumps(
            response,
            ensure_ascii=False,
            indent=4,
        )
    
    def get_all_higher_educations_chart(self) -> str:
        session = Session(bind=self.__engine)
        
        higher_educations = self.__all_higher_educations(session)
        higher_educations = higher_educations

        response = [{
            "coast": education.coast,
            "abbreviation": education.abbreviation
        } for education in higher_educations]

        session.close()
        return json.dumps(response, ensure_ascii=False, indent=4)

    def get_all_specialitets_for_higher_education(self, id_higher_education) -> str:
        session = Session(bind=self.__engine)

        higher_education = (
            session.query(HigherEducation.HigherEducation)
            .where(HigherEducation.HigherEducation.id == id_higher_education)
            .first()
        )

        specialitets: list[Specialitet.Specialitet] = higher_education.specialitet

        return json.dumps(
            [specialitet.to_dict() for specialitet in specialitets],
            ensure_ascii=False
        )

    def delete_higher_education(self, id_higher_education):
        session = Session(bind=self.__engine)

        higher_education = (
            session.query(HigherEducation.HigherEducation)
            .where(HigherEducation.HigherEducation.id == id_higher_education)
            .first()
        )

        session.delete(higher_education)
        session.commit()

    def delete_specialitet(self, id_specialitet):
        session = Session(bind=self.__engine)

        specialitet = (
            session.query(Specialitet.Specialitet)
            .where(Specialitet.Specialitet.id == id_specialitet)
            .first()
        )

        session.delete(specialitet)
        session.commit()

    def delete_examination(self, id_examination):
        session = Session(bind=self.__engine)

        examination = (
            session.query(Examinations.Examinations)
            .where(Examinations.Examinations.id == id_examination)
            .first()
        )

        session.delete(examination)
        session.commit()

    def delete_passing_grade(self, id_passing_grades):
        session = Session(bind=self.__engine)

        passing_grade = (
            session.query(PassingGrades.PassingGrades)
            .where(PassingGrades.PassingGrades.id == id_passing_grades)
            .first()
        )

        session.delete(passing_grade)
        session.commit()

    def add_user(self, user_name, password):
        session = Session(bind=self.__engine)

        session.add()
        session.commit()
