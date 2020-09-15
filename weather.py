import requests #библиотека работающая с запросами
import settings

# пишем функцию запроса погоды,
# создаем и использем словарь с нужными нам параметрами и нужным городом
def weather_by_city(city_name):
    weather_url = "http://api.worldweatheronline.com/premium/v1/weather.ashx"
    params = {
        "key": settings.API_KEY,
        "q": city_name,
        "format": "json",
        "num_of_days": 1,
        "lang": "ru",
    }
    result = requests.get(weather_url, params=params) # получаем результат запроса и заисываем его в переменную
    weather = result.json() # приводим результат к формату json
    # Если есть нужная нам информация - возвращаем её, иначе False
    if 'data' in weather:
        if 'current_condition' in weather['data']:
            try:
                return weather['data']['current_condition'][0]
            except(IndexError, TypeError):
                return False
    return False

if __name__ == "__main__":
    print(weather_by_city('Moscow,Russia'))
