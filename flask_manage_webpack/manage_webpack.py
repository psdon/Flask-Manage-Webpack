import json
import os

import requests
from flask import current_app


class FlaskManageWebpack:
    def __init__(self, app=None):
        self.app = app
        self.webpack_assets = {}

        if app is not None:
            self.init_app(app)

    def init_app(self, app):

        app.config.setdefault("MANAGE_WEBPACK_MANIFEST_PATH",
                              os.path.join(app.static_folder, "manifest.json"))
        app.config.setdefault("MANAGE_WEBPACK_ASSETS_URL", None)
        app.config.setdefault("MANAGE_WEBPACK_MANIFEST_URL", None)

        self._get_webpack_assets(app)
        if app.config.get("DEBUG", False):
            app.before_request(self._reload_webpack_assets)

        app.add_template_global(self.webpack_url_for)

    def _reload_webpack_assets(self):
        return self._get_webpack_assets(current_app)

    def _get_webpack_assets(self, app):
        manifest_path = app.config.get("MANAGE_WEBPACK_MANIFEST_PATH")
        external_manifest_url = app.config.get("MANAGE_WEBPACK_MANIFEST_URL")

        if external_manifest_url:
            self.webpack_assets = requests.get(external_manifest_url).json()
        else:
            try:
                with app.open_resource(manifest_path, "r") as manifest:
                    self.webpack_assets = json.load(manifest)
            except IOError:
                raise RuntimeError(
                    "MANAGE_WEBPACK_MANIFEST_PATH requires a valid manifest json file."
                )

    def webpack_url_for(self, file):

        if not self.webpack_assets:
            return "None"

        external_url = current_app.config.get("MANAGE_WEBPACK_ASSETS_URL")
        if external_url:
            return f"{external_url}{self.webpack_assets.get(file)}"

        return self.webpack_assets.get(file)
