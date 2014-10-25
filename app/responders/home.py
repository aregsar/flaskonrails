from flask import Blueprint, g, current_app, url_for
from flask import render_template, request, abort, jsonify
from flask.ext.login import current_user
# from forms.account.signup import SignupForm
# from forms.account.search import SearchForm
#bluprint is registered in module app.blueprints.py
res = Blueprint('home',__name__)

#uncomment app_errorhandler function for blueprint specific error handling
#app_errorhandler is special function for blueprint error handleing
#use the standard errorhandler function in the app.py module for
#application wide error hanlding
@res.app_errorhandler(404)
def not_found(e):
    return render_template("company/404.html")

@res.route('/abort')
def abort():
    abort(404)

@res.route('/')
def index():
    # if ENV.is_dev():
    #     pass
    return render_template("account/signup.html")
    #return render_template("home/dashboard.html",form=form)
    # if current_user.is_authenticated():
    #     form = SearchForm()
    #     return render_template("home/dashboard.html",form=form)
    # else:
    #     form = SignupForm()
    #     return render_template("account/signup.html",form=form)




