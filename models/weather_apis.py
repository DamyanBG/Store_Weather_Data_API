from sqlalchemy import func

from db import db


class WeatherApiModel(db.Model):
    __tablename__ = "weather_apis"

    pk = db.Column(db.Integer, primary_key=True)
    create_on = db.Column(db.DateTime, server_default=func.now())
    name = db.Column(db.String(100), nullable=False)
    api_url = db.Column(db.String(255), nullable=False)
