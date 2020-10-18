# Сайт с новостями о python

### Установка

1. Клонируйте репозиторий, создайте виртуальное окружение
2. Установите зависимости `pip install -r requirements.txt`
3. Создайте файл `settings.py` и создайте в нем переменные:
  ```
basedir = os.path.abspath(os.path.dirname(__file__))
REMEMBER_COOKIE_DURATION = timedelta(days=10)
WEATHER_DEFAULT_CITY = "Впишите Ваш город и страну"
WEATHER_API_KEY = 'Введите ваш ключ'
WEATHER_URL = 'http://api.worldweatheronline.com/premium/v1/weather.ashx'
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, '..', 'webapp.db')

SECRET_KEY = 'Создайте ваш секретный ключ'

SQLALCHEMY_TRACK_MODIFICATIONS = False
  ```