from flask import Flask
from . import settings
from .views import bp
from flask_manage_webpack import FlaskManageWebpack


def create_app(config_object=None):
    """Create application factory, as explained here: http://flask.pocoo.org/docs/patterns/appfactories/.

    :param config_object: The configuration object to use.
    """
    app = Flask(__name__.split(".")[0])

    if config_object:
        app.config.from_object(config_object)
    else:
        app.config.from_object(settings.Dev)

    # Register Extension
    manage_webpack = FlaskManageWebpack()
    manage_webpack.init_app(app)

    app.register_blueprint(bp)

    return app
