from schemas.bases import BaseCurrentDataSchema
from marshmallow import fields


class CurrentDataResponseSchema(BaseCurrentDataSchema):
    created_on = fields.DateTime()
