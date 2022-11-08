from db import db

from models.current_data import CurrentDataModel


class CurrentDataManager:
    @staticmethod
    def get_all():
        return CurrentDataModel.query.all()

    @staticmethod
    def get_by_day(day):
        return CurrentDataModel.query.filter(
            CurrentDataModel.created_on >= f"{day} 00:00",
            CurrentDataModel.created_on <= f"{day} 23:59",
        ).all()

    @staticmethod
    def get_by_day_range(start_day, end_day):
        return CurrentDataModel.query.filter(
            CurrentDataModel.created_on >= f"{start_day} 00:00",
            CurrentDataModel.created_on <= f"{end_day} 23:59",
        ).all()

    @staticmethod
    def create(current_data_data):
        current_data = CurrentDataModel(**current_data_data)
        db.session.add(current_data)
        db.session.commit()
        return current_data
