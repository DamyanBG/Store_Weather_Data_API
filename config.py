from flask import Flask
from flask_restful import Api
from flask_migrate import Migrate
from resources.routes import routes
from decouple import config

from db import db


# class LocalStorageConfiguration:
#     DEBUG = True
#     TEST = True
#     SQLALCHEMY_DATABASE_URI = (
#         f"postgresql://{config('DB_USER_LOCAL')}:{config('DB_PASSWORD_LOCAL')}"
#         f"@{config('DB_HOST_LOCAL')}/{config('DB_NAME_LOCAL')}"
#     )


class RenderDatabaseConfiguration:
    DEBUG = True
    TEST = True
    SQLALCHEMY_DATABASE_URI = f"postgresql://{config('RENDER_USER')}:{config('RENDER_KEY')}@{config('RENDER_URL')}/{config('RENDER_DATABASE_NAME')}"


def create_app():
    app = Flask(__name__)
    app.config.from_object(RenderDatabaseConfiguration)
    api = Api(app)
    db.init_app(app)
    migrate = Migrate(app, db)
    [api.add_resource(*r) for r in routes]
    return app
