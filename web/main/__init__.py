from flask import Flask
from web.main.config import config_by_name
from web.main.api.time import api

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config_by_name[config_name])
    app.register_blueprint(api, url_prefix='/')
    return app
