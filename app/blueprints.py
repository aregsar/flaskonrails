from views import home
from views import company
from views import account

#for each view blueprint you need to add corresponding blueprint registration here
def register_blueprints(app):
    app.register_blueprint(home.res)
    app.register_blueprint(company.mod)
    app.register_blueprint(account.mod)
