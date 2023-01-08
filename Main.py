from Controller.Controller import Controller
from sqlalchemy.engine import URL
from sqlalchemy import create_engine
from flask import Flask
from flask import request
from flask_cors import CORS, cross_origin


app = Flask(__name__)



Engine = create_engine(url_object)
controller = Controller(Engine)


@app.route("/test", methods=["GET"])
@cross_origin(origin="*", headers=["Content-Type", "Authorization"])
def get_shared_interests():
    return controller.get_all_specialitets_for_higher_education(1)


if __name__ == "__main__":
    app.run(debug=True)
