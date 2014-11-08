from flask.ext.script import Manager
#from flask.ext.script import *
#from flask.ext import script

from app.application import create_app
#from app.config.application import create_app

app = create_app()
manager = Manager(app)
#manager = script.Manager(app)
if __name__ == '__main__':
    manager.run()




