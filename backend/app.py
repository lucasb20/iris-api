from flask import Flask
from flask_smorest import Api
from resources import MlpBlueprint

def create_app():
    app = Flask(__name__)

    api = Api(app)

    api.register_blueprint(MlpBlueprint)

    return app