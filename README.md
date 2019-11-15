[![Build Status](https://travis-ci.org/psdon/Flask-Manage-Webpack.svg?branch=master)](https://travis-ci.org/psdon/Flask-Manage-Webpack)
[![PyPI](https://img.shields.io/pypi/v/Flask-Manage-Webpack)](https://pypi.org/project/Flask-Manage-Webpack)
<img src="https://flat.badgen.net/dependabot/psdon/Flask-Manage-Webpack?icon=dependabot" alt="Dependabot Badge" />

# What is Flask-Manage-Webpack?
A Flask extension that connect and manage your webpack generated assets.
`Flask-Manage-Webpack` reads a manifest.json file auto-generated by `webpack-manifest-plugin`, 
and out of the box it made possible to:
 
1. Import your assets via `webpack_url_for()` in your templates.
2. Browser caching via hash tagging.
3. Code splitting and dynamic import().
4. Compatible with Content-Security-Policy: `e.g. script-src: 'nonce-<random-value>`
5. Working with CDN, and static host provider such as `Netlify` 
for making your Webpack build process automated.
6. Extending the functionality by using Webpack.

### Quick start
**Install:** `pip install Flask-Manage-Webpack`

```python
from flask import Flask
from flask_manage_webpack import FlaskManageWebpack

app = Flask(__name__.split(".")[0])

# Register Extension
manage_webpack = FlaskManageWebpack()
manage_webpack.init_app(app)
```

**Initialize Webpack Config:** 
- Run `flask manage-webpack --app your_flask_app`
- It will generate config files for webpack.

**Run Webpack:** `npm start`

> For more info, checkout the demo app inside example folder.

### How to import assets in HTML?
**Import your main stylesheet to HTML:**

`<link rel="stylesheet" href="{{ webpack_url_for('main_css.css') }}">`

**Import your main JavaScript to HTML:**

`<script id="main_js" src="{{ webpack_url_for('main_js.js') }}"></script>`

**What about images, and other files?**
1. Put your images to `assets/img/` or to your preferred folder structure.
2. In HTML, import your image via relative path: `<img src="{{ webpack_url_for('img/something.jpg') }}">`


### Config Variables:
1. `MANAGE_WEBPACK_MANIFEST_PATH` defaults to `static/manifest.json`
2. `MANAGE_WEBPACK_ASSETS_URL`: Your static url domain name. Defaults to `None`
3. `MANAGE_WEBPACK_MANIFEST_URL`: Your absolute manifest.json url. This is useful if you wish to host you manifest.json file in a remote server,
 and if you like to automate your Webpack build process by hosting it to such service like `Netlify`. i.e.`https://example.com/manifest.json`
