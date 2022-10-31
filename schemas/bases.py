from marshmallow import Schema, fields, validate


class BaseWeatherApiSchema(Schema):
    name = fields.String(required=True, validate=validate.Length(max=100))
    api_url = fields.String(required=True, validate=validate.Length(max=255))


class BaseCurrentDataSchema(Schema):
    place = fields.String(required=True, validate=validate.Length(max=255))
    temperature = fields.Float(required=True)