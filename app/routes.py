from views import home
from views import company
from views import account


#optionally use this function to add application routing rules in a single location
#all the application routes can be specified here instead of using attribute routing
#or you can use a combination of both
def add_url_rules():
    #home.mod.add_url_rule('/', endpoint='index',view_func=home.index)
    #company.mod.add_url_rule('/', endpoint='index',view_func=company.index)
    #url_for('home.index')
    #url_for('company.index')
    pass
    #examples:
    #view_func is the actual view function prefixed by the blueprint
    #endpoint can be any unique name per bluepring. Generally the view function name is used.
    #home.mod.add_url_rule('/', endpoint='index',view_func=home.index)
    #post.mod.add_url_rule('/posts/<id>', endpoint='index',view_func=post.index, defaults={'id': None}, methods=['GET','POST'])


    #
    #list all bluprint mapped routes
    #print home.mod.url_map
