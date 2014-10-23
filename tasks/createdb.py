
#utility module for recreating database in development
from app.app import create_app
app = create_app()
with app.app_context():
    from models.user import User
    from plugins import db
    print db
    db.drop_all()
    db.create_all()


