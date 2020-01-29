from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail
from tfteamaker.config import Config

from flask_cors import CORS

from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

db = SQLAlchemy()

cors = CORS()

migrate = Migrate()

bcrypt = Bcrypt()

login_manager = LoginManager()
login_manager.login_view = 'users.login'
login_manager.login_message_category = 'info'

mail = Mail()


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)
    mail.init_app(app)

    cors.init_app(app)

    # for migrations
    migrate.init_app(app, db)

    from tfteamaker.users.routes import users
    from tfteamaker.posts.routes import posts
    from tfteamaker.main.routes import main
    from tfteamaker.errors.handlers import errors
    from tfteamaker.teams.routes import teams
    app.register_blueprint(users)
    app.register_blueprint(posts)
    app.register_blueprint(main)
    app.register_blueprint(errors)
    app.register_blueprint(teams)

    return app
