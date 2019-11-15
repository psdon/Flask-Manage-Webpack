from flask import Blueprint, render_template, after_this_request
import uuid

bp = Blueprint("main", __name__)


@bp.route("/")
def main():
    nonce = uuid.uuid4().hex + uuid.uuid1().hex

    @after_this_request
    def set_content_security_policy_headers(response):
        csp = f"script-src 'nonce-{nonce}'; " \
            f"style-src 'self';"
        response.headers.add('Content-Security-Policy', csp)
        return response

    return render_template("index.html", nonce=nonce)
