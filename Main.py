from Controller.Controller import Controller
from sqlalchemy.engine import URL
from sqlalchemy import create_engine
from flask import Flask, request, render_template
from flask_cors import CORS, cross_origin


app = Flask(__name__)
cors = CORS(app, resources={r"/get_shared_interests": {"origins": "*"}})
app.config["CORS_HEADERS"] = "Content-Type"




Engine = create_engine(url_object)
controller = Controller(Engine)

# x = controller.get_all_higher_educations()

# y = 1

@app.route("/higher_education", methods=["GET"])
@cross_origin(origin="*", headers=["Content-Type", "Authorization"])
def get_shared_interests():
    return controller.get_all_higher_educations_chart()

@app.route('/')
def hello():
    higher_educations = controller.get_all_higher_educations_chart()
    return render_template('SteppedAreaChart.html', utc_dt=higher_educations)

if __name__ == "__main__":
    app.run(debug=True)
   # x = controller.get_all_higher_education()
    # return render_template('1.html', utc_dt=controller.get_all_higher_education())