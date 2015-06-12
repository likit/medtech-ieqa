from flask import Flask, render_template
from flask.ext.bootstrap import Bootstrap
# from flask.mail import Mail
from flask.ext.login import LoginManager
from config import config
from flask_admin import Admin
from flask.ext.pymongo import PyMongo

bootstrap = Bootstrap()

login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.login'
mongo = PyMongo()

def create_app(config_name):

    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    bootstrap.init_app(app)
    login_manager.init_app(app)
    mongo.init_app(app)

    from adminpage.views import (MyAdminIndexView, HomeView,
                                            AdminResult1View)
    admin = Admin(name="My Admin",
            index_view=MyAdminIndexView(endpoint='admin'))

    admin.add_view(HomeView(name='App Home'))
    with app.app_context():
        admin.add_view(AdminResult1View(mongo.db.results,
                            name='Result1'))

    admin.init_app(app)

    # attach routes and custom error pages here
    from main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    from customer import customer as customer_blueprint
    app.register_blueprint(customer_blueprint, url_prefix='/customer')

    from auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint, url_prefix='/auth')

    return app
