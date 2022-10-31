from marshmallow import fields

from schemas.bases import BaseWeatherApiSchema


class WeatherApisResponseSchema(BaseWeatherApiSchema):
    pk = fields.Integer(required=True)
    create_on = fields.DateTime(required=True)
