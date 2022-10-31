from utils.decorators import validate_schema
from schemas.request.current_data import CreateCurrentDataSchema

class CreateCurrentData:
    @validate_schema(CreateCurrentDataSchema)
    def create():
        return