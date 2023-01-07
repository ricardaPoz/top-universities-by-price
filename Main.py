from Controller.Controller import Controller
from sqlalchemy.engine import URL
from sqlalchemy import create_engine
from time import perf_counter


url_object = URL.create(
    "mysql+pymysql",
    username="19-IAS.PozdnyakovSY",
    database="19-IAS_PozdnyakovSY",
    password="UqO!D@vYUcEx2g%}",
    host="s2.kts.tu-bryansk.ru",
    port="3306",
)

Engine = create_engine(url_object)
c = Controller(Engine)
