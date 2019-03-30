# -*- coding: utf-8 -*-#

#-------------------------------------------------------------------------------
# Name:         main.py
# Description:  
# Author:       henrylee
# Date:         19-3-28
#-------------------------------------------------------------------------------

import logging.config

from os import path
import logging
from flask import Flask, Blueprint

import config

from api.restplus import api
from api.endpoints.products import ns as casper_products_namespace


app = Flask(__name__)
log_file_path = path.join(path.dirname(path.abspath(__file__)), 'log.conf')

logging.config.fileConfig(log_file_path)
log = logging.getLogger(__name__)


def configure_app(flask_app):
    flask_app.config['SERVER_NAME'] = config.FLASK_SERVER_NAME
    flask_app.config['SWAGGR_UI_DOC_EXPANSION'] = config.RESTPLUS_SWAGGR_UI_DOC_EXPANSION
    flask_app.config['RESTPLUS_VALIDATE'] = config.RESTPLUS_VALIDATE
    flask_app.config['RESTPLUS_MASK_SWAGGER'] = config.RESTPLUS_MASK_SWAGGER
    flask_app.config['ERROR_404_HELP'] = config.RESTPLUS_ERROR_404_HELP


def initialize_app(flask_app):
    configure_app(flask_app)
    blueprint = Blueprint('api', __name__, url_prefix='/api')
    api.init_app(blueprint)
    api.add_namespace(casper_products_namespace)
    flask_app.register_blueprint(blueprint)


def main(host, port):
    initialize_app(app)
    log.info(f'>>>> Starting development server at {host}:{str(port)}')
    app.run(debug=config.FLASK_DEBUG, host=host, port=port)


# If we're runing in stand alone mode, run the application
if __name__ == '__main__':
    main("localhost", 1111)
