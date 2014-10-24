from responders import home
from responders import company
from responders import account


#optionally use this function to add application routing rules in a single location
#all the application routes can be specified here instead of using attribute routing
#or you can use a combination of both
def add_url_rules(app):
    """
    #examples:
    #home.res.add_url_rule('/',view_func=home.index) #url_for('home.index')
    #home.res.add_url_rule('/', endpoint='index',view_func=home.index) #url_for('home.index')
    #home.res.add_url_rule('/', endpoint='uniquename_per_blueprint',view_func=home.index) #url_for('home.uniquename_per_blueprint')
    #post.res.add_url_rule('/posts/<id>', view_func=post.index, defaults={'id': None}, methods=['GET','POST'])
    #post.res.add_url_rule('/posts/<id>', endpoint='index',view_func=post.index, defaults={'id': None}, methods=['GET','POST'])

    #notes:
    #view_func is the actual responder function prefixed by the blueprint name
    #endpoint if specified can be any unique name per bluepring.
    #Generally the responder function name is used.
    #if the endpoint is not specified then it defaults to the responder function name
    #you can explicitly name the endpoint the same as the responder function name
    #to get the same url_for('home.index')
    #home.res.add_url_rule('/', endpoint='index',view_func=home.index)
    #you can explicitly name the endpoint something other then the responder function name
    #but then you must use that name in url_for('home.dashboard') to get URL
    #Note this will override the default endpoint and url_for('home.index') will not resolve anymore
    #home.res.add_url_rule('/', endpoint='dashboard',view_func=home.index)
    """
    # uncomment to use instead of or in combination with attribute based url routes
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
    # account.res.add_url_rule('/account/<id>', view_func=account.details)
    # account.res.add_url_rule('/password/forgot', view_func=account.forgot_password_form)
    # account.res.add_url_rule('/password/forgot', view_func=account.forgot_password_form, methods=['POST'])
    # account.res.add_url_rule('/password/reset', view_func=account.reset_password_form)
    # account.res.add_url_rule('/password/reset', view_func=account.reset_password_form, methods=['POST'])
    # account.res.add_url_rule('/account/<id>/edit/email', view_func=account.edit_email_form)
    # account.res.add_url_rule('/account/<id>/edit/email', view_func=account.edit_email_form, methods=['POST'])
    # account.res.add_url_rule('/account/<id>/edit/email', view_func=account.edit_settings_form)
    # account.res.add_url_rule('/account/<id>/edit/email', view_func=account.edit_settings_form, methods=['POST'])





