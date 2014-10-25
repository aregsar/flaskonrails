from flask import Blueprint, g, current_app, url_for
from flask import render_template, request, abort, jsonify
from flask.ext.login import current_user
###this bluprint is registered in the module app.blueprints.py
res = Blueprint('company',__name__)
###this bluprint is registered in the module app.blueprints.py

"""
uncomment not_found function for blueprint specific error handling
app_errorhandler is special function for blueprint error handleing
use the standard errorhandler function in the app.py module for
application wide error hanlding
"""
# @res.app_errorhandler(404)
# def not_found(e):
#     return render_template("company/404.html")

"""
uncomment abort function for route for testing the app_errorhandler(404)
"""
# @res.route('/abort')
# def abort():
#     abort(404)

@res.route('/about')
def about():
    return render_template("company/about.html")


