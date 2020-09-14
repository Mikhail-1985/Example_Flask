from flask import Flask
from weather import weather_by_city

app = Flask(__name__)

@app.route("/")
def index():
    weather = weather_by_city('Moscow,Russia')
    if weather:
        return f"Сейчас на улице {weather['temp_C']}, но ощущается как {weather['FeelsLikeC']}"
    else:
        return "Погода недоступна"

if __name__ == "__main__":
    app.run(debug=True)