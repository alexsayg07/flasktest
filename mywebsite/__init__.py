from flask import Flask
#from .config import BaseConfig
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager



db = SQLAlchemy()
DB_NAME = 'girlstocks.db'

def create_app() -> Flask:
    from .config import BaseConfig
    config = BaseConfig()
    app = Flask(__name__)
    # Want to store this elsewhere after development so that it is not easily accessed 
    app.config['SECRET_KEY'] = config.dev_secret_access_key
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    db.init_app(app)


    from .views import views
    from .auth import auth
    
    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')
    print("NOT Imported models")
    from .models import User, Note, Stock
    print("Imported models")
    with app.app_context():
        db.create_all()
        print("Created database")
    
    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))

    return app
