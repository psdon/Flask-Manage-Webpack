from flask import Flask

from . import settings
from .extensions import manage_webpack
from .views import bp


def create_app(config_object=None):
    """Create application factory, as explained here: http://flask.pocoo.org/docs/patterns/appfactories/.

    :param config_object: The configuration object to use.
    """
    app = Flask(__name__)

    if config_object:
        app.config.from_object(config_object)
    else:
        app.config.from_object(settings.Dev)

    # Register Extension
    manage_webpack.init_app(app)

    # Register Blueprint
    app.register_blueprint(bp)

    return app
