from flask import Blueprint, render_template, g, current_app
from flask.ext.login import current_user
#bluprint is registered in module app.blueprints.py
res = Blueprint('account_v1',__name__)


@res.route('/signout')
def signout():
    #TODO: Signout Current User
    return redirect(url_for('home.index'))

@res.route('/signin')
def signin():
        return render_template("account/signin_form.html",form=form)

@res.route('/account/details')
def details():
        return render_template("account/details.html")








