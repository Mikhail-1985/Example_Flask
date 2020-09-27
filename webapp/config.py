import os


basedir = os.path.abspath(os.path.dirname(__file__)) #абсолютный путь до этой папки

WEATHER_DEFAULT_CITY = "Petersburg,Russia"
WEATHER_API_KEY = '296436667631461495570739201409'
WEATHER_URL = 'http://api.worldweatheronline.com/premium/v1/weather.ashx'
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, '..', 'webapp.db')