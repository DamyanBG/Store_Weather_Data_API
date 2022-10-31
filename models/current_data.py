from sqlalchemy import func


from db import db


class CurrentDataModel(db.Model):
    __tablename__ = "current_data"

    pk = db.Column(db.Integer, primary_key=True)
    created_on = db.Column(db.DateTime, server_default=func.now())
    place = db.Column(db.String(255), nullable=False)
    temperature = db.Column(db.Float, nullable=False)
    weather_api_pk = db.Column(db.Integer, db.ForeignKey("weather_apis.pk"))
    weather_api = db.relationship("WeatherApiModel")
