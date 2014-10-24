from flask import Blueprint, render_template, g, current_app
from flask.ext.login import current_user
#bluprint is registered in module app.blueprints.py
res = Blueprint('company',__name__)

@res.route('/about')
def about():
    return render_template("company/about.html")


