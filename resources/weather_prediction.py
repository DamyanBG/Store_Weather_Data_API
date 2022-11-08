from flask import request
from flask_restful import Resource
from managers.weather_prediction import WeatherPredictionManager
from schemas.response.weather_prediction import WeatherPredictionResponseSchema


class CreatePrediction(Resource):
    def post(self):
        prediction_data = WeatherPredictionManager.create(request.get_json())
        schema = WeatherPredictionResponseSchema()
        return schema.dump(prediction_data), 201
