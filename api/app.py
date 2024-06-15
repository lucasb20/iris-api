from flask import Flask
from resources import MlpBlueprint
import os

def create_app():
    app = Flask(__name__)

    app.config["PROPAGATE_EXCEPTIONS"] = True
    app.config['SECRET_KEY'] = os.getenv("SECRET_KEY") or 'dev'

    app.register_blueprint(MlpBlueprint)
    return app