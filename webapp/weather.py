import requests #библиотека работающая с запросами

from flask import current_app

# пишем функцию запроса погоды,
# создаем и использем словарь с нужными нам параметрами и нужным городом
def weather_by_city(city_name):
    weather_url = current_app.config['WEATHER_URL']
    params = {
        "key": current_app.config['WEATHER_API_KEY'],
        "q": city_name,
        "format": "json",
        "num_of_days": 1,
        "lang": "ru",
    }
    try:
        result = requests.get(weather_url, params=params) # получаем результат запроса и заисываем его в переменную
        result.raise_for_status() # обработка ошибок 4** и 5**
        weather = result.json() # приводим результат к формату json
        # Если есть нужная нам информация - возвращаем её, иначе False
        if 'data' in weather:
            if 'current_condition' in weather['data']:
                try:
                    return weather['data']['current_condition'][0]
                except(IndexError, TypeError):
                    return False
    except (requests.RequestException, ValueError):
        print('Сетевая ошибка')
        return False
    return False

if __name__ == "__main__":
    print(weather_by_city(current_app.config['WEATHER_DEFAULT_CITY']))
