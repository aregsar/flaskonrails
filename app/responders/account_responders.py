from flask import Blueprint, render_template, g, current_app
from flask.ext.login import current_user
#bluprint is registered in module app.blueprints.py
res = Blueprint('account',__name__)


@res.route('/signout')
def signout():
    #TODO: Signout Current User
    return redirect(url_for('home.index'))

@res.route('/signin')
def signin():
        return render_template("account/signin.html")

@res.route('/account/signup')
def signup():
        return render_template("account/signup.html")

@res.route('/account/details')
def details():
        return render_template("account/details.html")

@res.route('/account/edit')
def edit():
        #form = EditAccountForm()
        #return render_template("account/edit.html",form=form)
        return render_template("account/edit.html")

@res.route('/password/forgot')
def forgot_password():
        return render_template("account/forgot_password.html")


@res.route('/password/reset')
def reset_password():
        return render_template("account/reset_password.html")


