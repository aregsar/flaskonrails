import os
from flask import current_app

"""
single configuration class for all environments
defines all keys that will exist in all environments
(some keys may not be being used in some environments but that is OK)
The values for all keys are loaded from environment variables defined
in each environment.
A separate bash script that is not checked in to public
source control repo, should be created for each environment
which will set the environmet vars for that specific environment
"""
class ENV:
    @staticmethod
    def is_dev():
        return current_app.config['ENV'] == 'DEV'

class Config:
    #use bash commands env or printenv to show current env var settings
    #use os.environ.get('ENV_VAR_NAME') to raise exception for missing env var
    #use os.environ['ENV_VAR_NAME'] to return None default for missing env var
    #use bool(os.environ.get('ENV_VAR_NAME')) for True\False env vars
    #Flask or some of its extensions internaly use the following config var names:
    #so don't change their names as specified in this class
    #DEBUG, SECRET_KEY

    #example bash env var setting:
    #export MYAPP_ENV=DEV
    #ENV options : "DEV" or "TEST" or "STAGE" or "PROD"
    # ENV = os.environ.get('MYAPP_ENV')
    ENV="DEV"

    #example bash env var setting:
    #export MYAPP_DEBUG=True
    # DEBUG = bool(os.environ.get('MYAPP_DEBUG'))
    DEBUG=True

    #example bash env var setting:
    #export MYAPP_DEBUG_TB_INTERCEPT_REDIRECTS=False
    # DEBUG_TB_INTERCEPT_REDIRECTS = bool(os.environ.get('MYAPP_DEBUG_TB_INTERCEPT_REDIRECTS'))

    #secret key generation from python shell
    #import os
    #os.urandom(24)
    #\xbd3\xb3\xbcD\xe9)"H\xa1\x80\x05\xc6\xe8\xc0\xc4\xfd\x13%c\xe4\xc8oD

    #example bash env var setting:
    #export MYAPP_SECRET_KEY='\xbd3\xb3\xbcD\xe9)"H\xa1\x80\x05\xc6\xe8\xc0\xc4\xfd\x13%c\xe4\xc8oD'
    # SECRET_KEY = os.environ['MYAPP_SECRET_KEY']
    SECRET_KEY="secret"

    #example bash env var setting:
    #export MYAPP_SSL_DISABLE=False
    #SSL_DISABLE = bool(os.environ.get('MYAPP_SSL_DISABLE'))

    #SqlAlchemy looks for this specific app.config['SQLALCHEMY_DATABASE_URL']
    #DATABASE_URL must be used as the name of the env variable for the database
    #connection string, when using Heroku and\or Rails active record to connect
    #to the database
    #example bash env var setting:
    #export DATABASE_URL='postgres://localhost/myappdb'
    # SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']
    # SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    # SQLALCHEMY_RECORD_QUERIES = True
    #SQLALCHEMY_ECHO = True


