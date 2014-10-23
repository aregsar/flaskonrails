from flask import Flask, g
from functools import wraps
from app.config import Config
from app.routes import add_url_rules
from app.blueprints import register_blueprints
from app.plugins import init_plugins


def create_app():
    #
    #create the root application context
    app = Flask(__name__)

    #
    #configure application(before initializing plugins)
    app.config.from_object(Config)

    #
    #setup flask extensions
    init_plugins(app)

    #
    #add any aditional url routing rules (before registering blueprints)
    add_url_rules()

    #
    #register blueprints
    register_blueprints(app)

    print app.url_map

    return app
