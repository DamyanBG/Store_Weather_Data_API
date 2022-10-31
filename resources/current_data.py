from flask import request
from flask_restful import Resource

from utils.decorators import validate_schema
from schemas.request.current_data import CreateCurrentDataSchema
from schemas.response.current_data import CurrentDataResponseSchema
from managers.current_data import CurrentDataManager


class CreateCurrentData(Resource):
    @validate_schema(CreateCurrentDataSchema)
    def post(self):
        current_data = CurrentDataManager.create(request.get_json())
        schema = CurrentDataResponseSchema()
        return schema.dump(current_data), 201
