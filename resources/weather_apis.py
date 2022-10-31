from flask import request
from flask_restful import Resource
from managers.weather_apis import WeatherApisManager

from utils.decorators import validate_schema
from schemas.request.weather_apis import WeatherApiCreateSchema
from schemas.response.weather_apis import WeatherApisResponseSchema

class ListCreateWeatherApis(Resource):
    def get(self):
        weather_apis = WeatherApisManager.get_all()
        schema = WeatherApisResponseSchema()
        return schema.dump(weather_apis, many=True)

    # @validate_schema(WeatherApiCreateSchema)
    # def post(self):
    #     weather_api = 
    #     return
