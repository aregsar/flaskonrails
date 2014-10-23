from flask import Blueprint, render_template, g, current_app
from flask.ext.login import current_user
from forms.account.signup import SignupForm
from forms.account.search import SearchForm
#bluprint is registered in module app.blueprints.py
res = Blueprint('home',__name__)

@res.route('/')
def index():
    if current_user.is_authenticated():
        form = SearchForm()
        return render_template("home/dashboard.html",form=form)
    else:
        form = SignupForm()
        return render_template("account/signup.html",form=form)

