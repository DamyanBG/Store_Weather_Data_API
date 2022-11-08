from schemas.bases import BaseWeatherPredictionSchema
from marshmallow import fields


class WeatherPredictionResponseSchema(BaseWeatherPredictionSchema):
    created_on = fields.DateTime()
