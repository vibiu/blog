from flask import Flask, current_app
from flask_sqlalchemy import SQLAlchemy
from config import config
db = SQLAlchemy()


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])

    config[config_name].init_app(app)
    db.init_app(app)

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    from .api import api as api_blueprint
    app.register_blueprint(api_blueprint, url_prefix='/api/1.0')

    from .rest import rest as rest_blueprint
    app.register_blueprint(rest_blueprint, url_prefix='/rest')

    return app
