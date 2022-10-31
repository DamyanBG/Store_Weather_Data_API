from flask import Flask
from flask_restful import Api
from flask_migrate import Migrate
from resources.routes import routes
from decouple import config

from db import db


class Configuration:
    DEBUG = True
    TEST = True
    SQLALCHEMY_DATABASE_URI = (
        f"postgresql://{config('DB_USER')}:{config('DB_PASSWORD')}"
        f"@{config('DB_HOST')}/{config('DB_NAME')}"
    )


def create_app():
    app = Flask(__name__)
    app.config.from_object(Configuration)
    api = Api(app)
    db.init_app(app)
    migrate = Migrate(app, db)
    [api.add_resource(*r) for r in routes]
    return app
