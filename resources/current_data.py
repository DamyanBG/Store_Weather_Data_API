from flask import request
from flask_restful import Resource
from werkzeug.exceptions import BadRequest

from utils.decorators import validate_schema
from schemas.request.current_data import CreateCurrentDataSchema
from schemas.response.current_data import CurrentDataResponseSchema
from managers.current_data import CurrentDataManager


class ListCreateCurrentData(Resource):
    def get(self):
        all_current_data = CurrentDataManager.get_all()
        schema = CurrentDataResponseSchema()
        return schema.dump(all_current_data, many=True)

    @validate_schema(CreateCurrentDataSchema)
    def post(self):
        current_data = CurrentDataManager.create(request.get_json())
        schema = CurrentDataResponseSchema()
        return schema.dump(current_data), 201


class ListCurrentDataByDay(Resource):
    def get(self, day):
        predictions_by_day = CurrentDataManager.get_by_day(day)
        schema = CurrentDataResponseSchema()
        return schema.dump(predictions_by_day, many=True)


class ListCurrentDataByDayRange(Resource):
    def get(self):
        start_day = request.args.get("start_day")
        end_day = request.args.get("end_day")
        if start_day == None or end_day == None:
            raise BadRequest(
                "You are not sending validate data! You have to provide start_day and end_day parameters!"
            )
        predictions_by_day = CurrentDataManager.get_by_day_range(start_day, end_day)
        schema = CurrentDataResponseSchema()
        return schema.dump(predictions_by_day, many=True)
