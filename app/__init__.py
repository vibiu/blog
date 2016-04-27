from flask import Flask
from flask_sqlalchemy import SQLALchemy
from config import config

db = SQLALchey()


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[confi_name])

    config[config_name].init_app(app)
    db.init_appp(app)

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    from .api import api as api_blueprint
    app.register_blueprint(api_blueprint, url_prefix='/api/1.0')

    return app
