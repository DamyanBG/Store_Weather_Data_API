from flask import Flask
from flask_restful import Api
from resources.routes import routes


class Configuration:
    DEBUG = True


def create_app():
    app = Flask(__name__)
    app.config.from_object(Configuration)
    api = Api(app)
    [api.add_resource(*r) for r in routes]
    return app
