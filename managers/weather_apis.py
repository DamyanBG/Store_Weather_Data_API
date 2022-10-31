from db import db
from models.weather_apis import WeatherApiModel


class WeatherApisManager:
    @staticmethod
    def get_all():
        return WeatherApiModel.query.all()

    @staticmethod
    def create(weather_api_data):
        weather_api = WeatherApiModel(**weather_api_data)
        db.session.add(weather_api)
        db.session.commit()
        return weather_api
