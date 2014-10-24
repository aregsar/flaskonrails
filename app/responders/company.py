from flask import Blueprint, render_template, g, current_app
from flask.ext.login import current_user
#bluprint is registered in module app.blueprints.py
res = Blueprint('company',__name__)


#uncomment app_errorhandler function for blueprint specific error handling
#app_errorhandler is special function for blueprint error handleing
#use the standard errorhandler function in the app.py module for
#application wide error hanlding
@res.app_errorhandler(404)
def not_found(e):
    return render_template("company/404.html")

#@res.route('/company')
def index():
        return "company"
        #abort(404)
        #return render_template("company/index.html")

#@res.route('/about')
def about():
        return render_template("company/about.html")


