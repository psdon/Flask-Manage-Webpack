import click

from flask import current_app
from flask.cli import with_appcontext
from . import utils


@click.command()
@click.option('--app')
@with_appcontext
def init(app="app"):
    utils.init_webpack_config(app_name=app)
