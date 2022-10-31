from db import db

from models.current_data import CurrentDataModel


class CurrentDataManager:
    @staticmethod
    def create(current_data_data):
        current_data = CurrentDataModel(**current_data_data)
        db.session.add(current_data)
        db.session.commit()
        return current_data
