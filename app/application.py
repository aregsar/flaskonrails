from flask import Flask, g, url_for,render_template
from functools import wraps
from app.config.settings import Settings
from app.config.routes import add_url_rules
from app.config.blueprints import register_blueprints
from app.config.extensions import init_extensions


def create_app():
    #
    #create the root application context
    app = Flask(__name__)

    #
    #configure application(before initializing plugins)
    app.config.from_object(Settings)

    #
    #setup flask extensions
    init_extensions(app)

    #
    #add any aditional url routing rules (before registering blueprints)
    add_url_rules(app)

    #
    #register blueprints
    register_blueprints(app)

    #
    #install application wide request filters
    setup_request_filters(app)

    #
    #install application wide error handlers
    setup_app_error_handlers(app)

    #list mapped routes
    print app.url_map

    return app

def setup_request_filters(app):
    #sample:fires only once before the first request to the application
    #note: more than one method can be decorated with @app.before_first_request
    @app.before_first_request
    def app_before_first_request():
        pass

    #fires before every request
    #note: more than one method can be decorated with @app.before_request
    @app.before_request
    def app_before_request():
        print url_for('home.index')
        print url_for('company.about')
        print url_for('static',filename='favicon.ico')
        #pass

    #fires after every non aborted request
    #note: more than one method can be decorated with @app.after_request
    @app.after_request
    def app_after_req(response):
        current_user = getattr(g, 'current_user', None)
        if current_user is not None:
            print g.current_user
        return response

    #fires after every request, aborted or not
    #note: more than one method can be decorated with @app.teardown_request
    @app.teardown_request
    def app_teardown_request(exception):
        current_user = getattr(g, 'current_user', None)
        if current_user is not None:
            print g.current_user



def setup_app_error_handlers(app):
    #use the app_errorhandler function in specific xxx_responder.py modules
    #instead for blueprint specific error hanldling
    @app.errorhandler(404)
    def not_found(e):
        return app.send_static_file("html/errors/404.html")#, 404


    @app.errorhandler(500)
    def internal_server_error(e):
        return app.send_static_file("html/errors/500.html"), 500

