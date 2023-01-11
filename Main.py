from Controller.DataBaseCRUD import (
    DataBaseCRUD,
    ControllerUser,
    ControllerHigherEducation,
    ControllerImages,
    ControllerSpecialitet,
    ControllerPassingGrades,
    ControllerExaminations,
)
from werkzeug.security import generate_password_hash, check_password_hash
from Controller.ControllerInitializingDB import ControllerInitializingDB
from sqlalchemy.engine import URL
from sqlalchemy import create_engine
from flask_login import LoginManager, login_manager, login_required, logout_user, login_user
from flask import Flask, request, render_template, redirect, url_for
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

application = Flask(__name__)
application.config['SECRET_KEY'] = 'a really really really really long secret key'
login_manager = LoginManager(application)
Engine = create_engine(url_object)

@login_manager.user_loader
def load_user(user_id):
    user = DataBaseCRUD(ControllerUser(Engine)).get(user_id)
    return user

@application.route("/higher_education", methods=['GET', 'POST'])
@login_required
def get_shared_interests():
    return DataBaseCRUD(ControllerHigherEducation(Engine)).all_to_json()

@application.route("/login", methods=["GET"])
def login():
    user = DataBaseCRUD(ControllerUser(Engine)).get(1)
    login_user(user, remember=True)
    return {
        "id": user.id,
        "user_name": user.user_name,
    }

@application.route('/logout')
@login_required
def logout():
    logout_user()
    return "user_logout"


@application.route("/higher_education_chart", methods=["GET"])
@login_required
def higher_education_chart():
    higher_educations = DataBaseCRUD(ControllerHigherEducation(Engine)).all_to_json()
    return render_template('SteppedAreaChart.html', utc_dt=higher_educations)

# @application.route('/')
# def hello():
#     higher_educations = controller.get_all_higher_educations_chart()
#     return render_template('ColumnChart.html', utc_dt=higher_educations)

if __name__ == "__main__":
    application.run(debug=True)