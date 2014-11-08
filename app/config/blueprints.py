from app.responders import home
from app.responders import company
from app.responders import account

#for each view blueprint you need to add corresponding blueprint registration here
def register_blueprints(app):
    app.register_blueprint(home.res)
    app.register_blueprint(company.res)
    app.register_blueprint(account.res)


    #print home.res.root_path


