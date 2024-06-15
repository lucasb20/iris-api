from flask import Flask
from resources import bp
import os

def create_app():
    app = Flask(__name__)
    
    app.config['SECRET_KEY'] = os.getenv("SECRET_KEY") or 'dev'

    app.register_blueprint(bp)
    return app