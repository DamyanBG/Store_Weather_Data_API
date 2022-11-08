from db import db
from models.weather_prediction import WeatherPredictionModel


class WeatherPredictionManager:
    @staticmethod
    def create(prediction_data):
        weather_prediction_data = WeatherPredictionModel(**prediction_data)
        db.session.add(weather_prediction_data)
        db.session.commit()
        return weather_prediction_data
