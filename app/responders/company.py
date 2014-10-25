from flask import Blueprint, g, current_app, url_for
from flask import render_template, request, abort, jsonify
from flask.ext.login import current_user
#bluprint is registered in module app.blueprints.py
res = Blueprint('company',__name__)

@res.route('/about')
def about():
    return render_template("company/about.html")


