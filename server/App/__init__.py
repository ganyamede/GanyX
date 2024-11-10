from flask import Flask
from .routes import auth_bp

def create_app():
    app = Flask(__name__)

    app.register_blueprint(auth_bp, url_prefix='/api/')

    return app


