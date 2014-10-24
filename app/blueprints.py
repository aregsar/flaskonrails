from responders import home
from responders import company
from responders import account

#for each view blueprint you need to add corresponding blueprint registration here
def register_blueprints(app):
    app.register_blueprint(home.res)
    app.register_blueprint(company.res)
    app.register_blueprint(account.res)


