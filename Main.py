from Controller.Controller import Controller
from sqlalchemy.engine import URL
from sqlalchemy import create_engine
from flask import Flask, request, render_template
from flask_cors import CORS, cross_origin
from Utilities.Config import DB_PARAMS


app = Flask(__name__)
cors = CORS(app, resources={r"/get_shared_interests": {"origins": "*"}})
app.config["CORS_HEADERS"] = "Content-Type"


url_object = URL.create(
    DB_PARAMS.get("DBAPI"),
    username=DB_PARAMS.get("username"),
    database=DB_PARAMS.get("database"),
    password=DB_PARAMS.get("password"),
    host=DB_PARAMS.get("host"),
    port=DB_PARAMS.get("port"),
)


Engine = create_engine(url_object)
controller = Controller(Engine)



@app.route("/higher_education", methods=["GET"])
@cross_origin(origin="*", headers=["Content-Type", "Authorization"])
def get_shared_interests():
    return controller.get_all_higher_educations_chart()

@app.route('/')
def hello():
    higher_educations = controller.get_all_higher_educations_chart()
    return render_template('ColumnChart.html', utc_dt=higher_educations)

if __name__ == "__main__":
    app.run(debug=True)
   # x = controller.get_all_higher_education()
    # return render_template('1.html', utc_dt=controller.get_all_higher_education())
