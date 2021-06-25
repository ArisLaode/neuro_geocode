import logging
from flask import Blueprint, jsonify, request
from decimal import Decimal
from yandex_geocoder import Client
from config import SECRET_KEY

client = Client(SECRET_KEY)
logger = logging.getLogger(__name__)
app_yandex = Blueprint('app_yandex', __name__)


@app_yandex.route('/', methods=['GET'])
def index():

    return "This is an app yandex use yandex geocode"


@app_yandex.route('/v1/coordinates', methods=['POST'])
def coordinate():
    try:
        if request.method == 'POST':
            coordinates = request.form['coordinates']
            var_coordinates = client.coordinates(coordinates)
            text = str(var_coordinates)
            res_coord = text.replace('Decimal', 'coordinates')
            logging.basicConfig(
                filename="log/app.log", level=logging.INFO)
            logging.info(
                ' Result yandex maps coordinate : %s', str(res_coord))

            return jsonify(str(res_coord))
    except Exception:
        return 'coordinates not found!'


@app_yandex.route('/v1/address', methods=['POST'])
def address():
    try:
        if request.method == 'POST':
            decimal_one = request.form['decimal_one']
            decimal_two = request.form['decimal_two']
            address = client.address(
                Decimal(decimal_one), Decimal(decimal_two))
            logging.basicConfig(
                filename="log/app.log", level=logging.INFO)
            logging.info(
                ' Result yandex maps address : %s', '{}'.format(address))

        return address
    except Exception:
        return 'coordinates not found!'
