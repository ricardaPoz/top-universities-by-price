from Controller.Controller import Controller
from sqlalchemy.engine import URL
from sqlalchemy import create_engine
from flask import Flask
from flask import request
from flask_cors import CORS, cross_origin



app = Flask(__name__)
cors = CORS(app, resources={r"/get_shared_interests": {"origins": "*"}})
app.config["CORS_HEADERS"] = "Content-Type"



Engine = create_engine(url_object)
controller = Controller(Engine)



@app.route("/higher_education", methods=["GET"])
@cross_origin(origin="*", headers=["Content-Type", "Authorization"])
def get_shared_interests():
    return controller.get_all_higher_education()


if __name__ == "__main__":
    app.run(debug=True)
