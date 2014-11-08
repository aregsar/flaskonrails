from flask import Flask, g, url_for
from functools import wraps
from config import Config
from routes import add_url_rules
from blueprints import register_blueprints
from plugins import init_plugins

#does not work
#from app.models.user import User
#but this works
from models.user import User
#this does not work here but works from app.models.user module
#from app.models.account import Account
#but this works
from models.account import Account

def create_app():
    #
    #create the root application context
    aapp = Flask(__name__)

    #
    #configure application(before initializing plugins)
    aapp.config.from_object(Config)

    #
    #setup flask extensions
    init_plugins(aapp)

    #
    #add any aditional url routing rules (before registering blueprints)
    add_url_rules(aapp)

    #
    #register blueprints
    register_blueprints(aapp)

    #
    #install application wide request filters
    setup_request_filters(aapp)

    #
    #install application wide error handlers
    setup_app_error_handlers(aapp)

    #list mapped routes
    print aapp.url_map

    return aapp

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
    #for blueprint specific error hanldling
    @app.errorhandler(404)
    def not_found(e):
        return render_template("static/html/error/404.html"), 404


    @app.errorhandler(500)
    def internal_server_error(e):
        return render_template("static/html/error/500.html"), 500

