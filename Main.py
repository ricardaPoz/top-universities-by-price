from Controller.DataBaseCRUD import (
    DataBaseCRUD,
    ControllerUser,
    ControllerHigherEducation,
    ControllerImages,
    ControllerSpecialitet,
    ControllerPassingGrades,
    ControllerExaminations,
)

# from Controller.ControllerInitializingDB import ControllerInitializingDB
from sqlalchemy.engine import URL
from sqlalchemy import create_engine
from flask_login import LoginManager
from flask import Flask, request, render_template
from flask_cors import CORS, cross_origin
from Utilities.Config import DB_PARAMS

url_object = URL.create(
    DB_PARAMS.get("DBAPI"),
    username=DB_PARAMS.get("username"),
    database=DB_PARAMS.get("database"),
    password=DB_PARAMS.get("password"),
    host=DB_PARAMS.get("host"),
    port=DB_PARAMS.get("port"),
)

# application = Flask(__name__)
# login_manager = LoginManager(application)


# cors = CORS(application, resources={r"/get_shared_interests": {"origins": "*"}})
# application.config["CORS_HEADERS"] = "Content-Type"


Engine = create_engine(url_object)
all = DataBaseCRUD(ControllerHigherEducation(Engine)).delete(1)
x = 1


# x = controller.get_all_higher_educations()

# y = 1

# @application.route("/higher_education", methods=["GET"])
# @cross_origin(origin="*", headers=["Content-Type", "Authorization"])
# def get_shared_interests():
#     return controller.get_all_higher_educations_chart()

# @application.route('/')
# def hello():
#     higher_educations = controller.get_all_higher_educations_chart()
#     return render_template('ColumnChart.html', utc_dt=higher_educations)

# if __name__ == "__main__":
#     application.run(debug=True)
#    # x = controller.get_all_higher_education()
#     # return render_template('1.html', utc_dt=controller.get_all_higher_education())
