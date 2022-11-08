from db import db
from models.weather_prediction import WeatherPredictionModel
from datetime import datetime


class WeatherPredictionManager:
    @staticmethod
    def get_all():
        return WeatherPredictionModel.query.all()

    @staticmethod
    def get_by_day(day):
        return WeatherPredictionModel.query.filter(
            WeatherPredictionModel.prediction_for >= f"{day} 00:00",
            WeatherPredictionModel.prediction_for <= f"{day} 23:59",
        ).all()

    @staticmethod
    def get_by_day_range(start_day, end_day):
        return WeatherPredictionModel.query.filter(
            WeatherPredictionModel.prediction_for >= f"{start_day} 00:00",
            WeatherPredictionModel.prediction_for <= f"{end_day} 23:59",
        ).all()

    @staticmethod
    def create(prediction_data):
        weather_prediction_data = WeatherPredictionModel(**prediction_data)
        db.session.add(weather_prediction_data)
        db.session.commit()
        return weather_prediction_data
