from flask import Flask
from weather import weather_by_city

app = Flask(__name__)

#используем декоратор
@app.route("/")
def index():
    weather = weather_by_city('Moscow,Russia')
    if weather:
        weather_text = f"Сейчас на улице {weather['temp_C']}, ощущается как {weather['FeelsLikeC']}"
    else:
        weather_text = "Погода недоступна"
    return f"""
    <html>
        <head>
            <title>Прогноз погоды</title>
        </head>
        <body>
            <h1>{weather_text}</h1>
        </body>
    </html>
    """
#запускаем приложение используя дебаг=Тру(можно оставить пустые скобки и ничего не использовать)
if __name__ == "__main__":
    app.run(debug=True)