from flask import request
from flask_restful import Resource
from werkzeug.exceptions import BadRequest

from managers.weather_prediction import WeatherPredictionManager
from schemas.response.weather_prediction import WeatherPredictionResponseSchema
from schemas.request.weather_prediction import WeatherPredicitionRequestSchema
from utils.decorators import validate_schema


class ListCreatePrediction(Resource):
    def get(self):
        all_data = WeatherPredictionManager.get_all()
        schema = WeatherPredictionResponseSchema()
        return schema.dump(all_data, many=True)

    @validate_schema(WeatherPredicitionRequestSchema)
    def post(self):
        prediction_data = WeatherPredictionManager.create(request.get_json())
        schema = WeatherPredictionResponseSchema()
        return schema.dump(prediction_data), 201


class ListPredictionByDay(Resource):
    def get(self, day):
        predictions_by_day = WeatherPredictionManager.get_by_day(day)
        schema = WeatherPredictionResponseSchema()
        return schema.dump(predictions_by_day, many=True)


class ListPredictionsByDayRange(Resource):
    def get(self):
        start_day = request.args.get("start_day")
        end_day = request.args.get("end_day")
        if start_day == None or end_day == None:
            raise BadRequest(
                "You are not sending validate data! You have to provide start_day and end_day parameters!"
            )
        predictions_by_day = WeatherPredictionManager.get_by_day_range(
            start_day, end_day
        )
        schema = WeatherPredictionResponseSchema()
        return schema.dump(predictions_by_day, many=True)
