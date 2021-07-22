from flask import Flask
from flask_cors import CORS

from api.model.models import db
from api.routes.url_shortener_api import url_shortener_api
from api.routes.url_statistics_api import url_statistics_api

import logging

def create_app(config_filename):
    app = Flask(__name__)

    
    logging.getLogger('flask_cors').level = logging.DEBUG

    app.config.from_object(config_filename)

    CORS(app)
    app.register_blueprint(url_shortener_api, url_prefix='/short-url')
    app.register_blueprint(url_statistics_api, url_prefix='/stats')

    db.init_app(app)

    return app

if __name__ == '__main__':
    from argparse import ArgumentParser

    app = create_app('config')

    app.run(host='0.0.0.0')