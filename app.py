from flask import Flask
from api.api import app_yandex

app = Flask(__name__)
app.register_blueprint(app_yandex)
