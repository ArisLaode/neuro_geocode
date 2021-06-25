from os import getenv

from dotenv import load_dotenv

load_dotenv()

SECRET_KEY = getenv('API_KEY_YANDEX', None)