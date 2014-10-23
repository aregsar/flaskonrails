from flask.ext.script import Manager
#from flask.ext.script import *
#from flask.ext import script
from app.app import create_app

app = create_app()
manager = Manager(app)
#manager = script.Manager(app)
if __name__ == '__main__':
    manager.run()




