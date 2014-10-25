from responders import home
from responders import company
from responders import account


#optionally use this function to add application routing rules in a single location
#all the application routes can be specified here instead of using attribute routing
#or you can use a combination of both
def add_url_rules(app):
    """
    #to generate reverse mapping for defined mappings, with the flask url_for function,
    #the general form is: url_for('blueprint.endpoint')

    #examples with and without explicit endpoint specified:

    #with mapping defined below you can use url_for('home.index') to generate URL '/'
    #defaults endpoint to "index"
    #home.res.add_url_rule('/', view_func=home.index)

    #with mapping defined below you can also use url_for('home.index') to generate URL '/'
    #explicit endpoint specified as "index"
    #home.res.add_url_rule('/', view_func=home.index, endpoint='index')

    #with mapping defined below you can use url_for('home.some_unique_name_for_home_blueprint') to generate URL '/'
    #home.res.add_url_rule('/', view_func=home.index, endpoint='any_unique_name_scoped_by_home_blueprint')

    #other examples with HTTP verbs and default parameters
    #post.res.add_url_rule('/posts/<id>', view_func=post.index, methods=['GET','POST'])
    #post.res.add_url_rule('/posts/<id>', view_func=post.index, defaults={'id': None})
    #post.res.add_url_rule('/posts/<id>', view_func=post.index, defaults={'id': None}, methods=['GET','POST'])
    #post.res.add_url_rule('/posts/<id>', endpoint='index',view_func=post.index, defaults={'id': None}, methods=['GET','POST'])
    """

    # uncomment below to use instead of or in combination with attribute based url routes
    # home.res.add_url_rule('/', view_func=home.index)
    # company.res.add_url_rule('/about', view_func=company.about)
    # account.res.add_url_rule('/signup', view_func=account.signup_form)
    # account.res.add_url_rule('/signup', view_func=account.signup, methods=['POST'])
    # account.res.add_url_rule('/signup', view_func=account.signup_form)
    # account.res.add_url_rule('/signup', view_func=account.signup, methods=['POST'])
    # account.res.add_url_rule('/signin', view_func=account.signin_form)
    # account.res.add_url_rule('/signin', view_func=account.signin, methods=['POST'])
    # account.res.add_url_rule('/account/notfound', view_func=account.notfound)
    # account.res.add_url_rule('/signout', view_func=account.signout)
    # account.res.add_url_rule('/account/<int:id>', view_func=account.details)
    # account.res.add_url_rule('/password/forgot', view_func=account.forgot_password_form)
    # account.res.add_url_rule('/password/forgot', view_func=account.forgot_password_form, methods=['POST'])
    # account.res.add_url_rule('/password/reset', view_func=account.reset_password_form)
    # account.res.add_url_rule('/password/reset', view_func=account.reset_password_form, methods=['POST'])
    # account.res.add_url_rule('/account/<int:id>/edit/email', view_func=account.edit_email_form)
    # account.res.add_url_rule('/account/<int:id>/edit/email', view_func=account.edit_email_form, methods=['POST'])
    # account.res.add_url_rule('/account/<int:id>/edit/email', view_func=account.edit_settings_form)
    # account.res.add_url_rule('/account/<int:id>/edit/email', view_func=account.edit_settings_form, methods=['POST'])





