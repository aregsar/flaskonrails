from flask import Blueprint, g, current_app, url_for
from flask import render_template, request, abort, jsonify
from flask.ext.login import current_user
#bluprint is registered in module app.blueprints.py
res = Blueprint('account',__name__)

signin_failed_message = "username or password was not valid. please try again"

@res.route('/account/notfound')
def notfound():
    return render_template("account/not_found.html")

@res.route('/signup')
def signup_form():
    form = SignupForm()
    return render_template("account/signup_form.html",form=form)

@res.route('/signup', methods=['POST'])
def signup():
    form = SignupForm()
    if form.validate_on_submit():
        user, signup_error = User.signup(form)
        if user:
            #AccountMailer.send_account_confirmation_email(current_app.config, user)
            return redirect(url_for('home.index'))
        flash(signup_error)
    return render_template("account/signup_form.html",form=form)

@res.route('/signin')
def signin_form():
    form = SigninForm()
    return render_template("account/signin_form.html",form=form)

@res.route('/signin', methods=['POST'])
def signin():
    form = SigninForm()
    if form.validate_on_submit():
        if User.signin(form):
            return redirect(url_for('home.index'))
        flash(signin_failed_message)
    return render_template("account/signin_form.html",form=form)

@res.route('/signout')
def signout():
    #User.signout()
    return redirect(url_for('home.index'))

@res.route('/account/<int:id>')
def details(id):
    user = User.Get(id)
    if not user:
        #return redirect(url_for('account.not_found'))
        return render_template("account/not_found.html")
    return render_template("account/details.html",user=user)



# @res.route('/password/forgot')
# def forgot_password_form():
#     return render_template("account/forgot_password_form.html")

# @res.route('/password/forgot', methods=['POST'])
# def forgot_password():
#     return render_template("account/forgot_password_form.html")

# @res.route('/password/reset')
# def reset_password_form():
#     return render_template("account/reset_password_form.html")

# @res.route('/password/reset', methods=['POST'])
# def reset_password():
#     return render_template("account/reset_password_form.html")

# @res.route('/account/<int:id>/edit/email')
# def edit_email_form():
#     return render_template("account/edit_email_form.html")

# @res.route('/account/<int:id>/edit/email', methods=['POST'])
# def edit_email():
#     return render_template("account/edit_email_form.html")

# @res.route('/account/<int:id>/edit/settings')
# def edit_settings_form():
#     return render_template("account/edit_settings_form.html")

# @res.route('/account/<int:id>/edit/settings', methods=['POST'])
# def edit_settings():
#     return render_template("account/edit_settings_form.html")





