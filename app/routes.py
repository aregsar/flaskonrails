from responders import home
from responders import company
from responders import account


#optionally use this function to add application routing rules in a single location
#all the application routes can be specified here instead of using attribute routing
#or you can use a combination of both
def add_url_rules(app):


    #use url_for('home.index') to generate the reverse '/' URL
    home.res.add_url_rule('/', view_func=home.index)

    #you can explicitly name the endpoint the same as the responder function name
    #to get the same url_for('home.index')
    #home.res.add_url_rule('/', endpoint='index',view_func=home.index)

    #you can explicitly name the endpoint something other then the responder function name
    #but then you must use that name in url_for('home.dashboard') to get URL
    #Note this will override the default endpoint and url_for('home.index') will not resolve anymore
    #home.res.add_url_rule('/', endpoint='dashboard',view_func=home.index)

    company.res.add_url_rule('/company', view_func=company.index)

    #examples:
    #view_func is the actual responder function prefixed by the blueprint
    #endpoint if specified can be any unique name per bluepring.
    #Generally the responder function name is used.
    #if the endpoint is not specified then it defaults to the responder function name
    #home.res.add_url_rule('/',view_func=home.index) #url_for('home.index')
    #home.res.add_url_rule('/', endpoint='index',view_func=home.index) #url_for('home.index')
    #home.res.add_url_rule('/', endpoint='uniquename_per_blueprint',view_func=home.index) #url_for('home.uniquename_per_blueprint')
    #post.res.add_url_rule('/posts/<id>', view_func=post.index, defaults={'id': None}, methods=['GET','POST'])
    #post.res.add_url_rule('/posts/<id>', endpoint='index',view_func=post.index, defaults={'id': None}, methods=['GET','POST'])


