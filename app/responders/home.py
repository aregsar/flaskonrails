from flask import Blueprint, g, current_app, url_for
from flask import render_template, request, abort, jsonify
from flask.ext.login import current_user
#this bluprint is registered in the module app.blueprints.py
res = Blueprint('home',__name__)
#this bluprint is registered in the module app.blueprints.py


"""
It is recommended that you avoid adding other responders to this file
Consider adding other responder files for other resource types.
"""
@res.route('/')
def index():
    # if ENV.is_dev():
    #     pass
    return render_template("home/index.html")
    # if current_user.is_authenticated():
    #     return render_template("home/dashboard.html")
    # else:
    #     return render_template("home/index.html")




