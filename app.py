from flask import request, abort

from app_config import app
from api import api
import sys
from util import cPrint


@app.before_request
def before_request():
    """
    Used to do authentication for following methods:
    - POST
    - PUT
    - UPDATE
    - DELETE
    """
    protected_methods = [
        "POST",
        "PUT",
        "UPDATE",
        "DELETE"
    ]
    if request.method in protected_methods and "localhost" not in request.origin:
        abort(405)


@app.after_request
def after_request(response):
    """
    Simple after_request implementation.
    Supports pre-flight requess.
    """
    custom_headers = {}

    if request.method == "OPTIONS":
        # Pre-flight options request
        custom_headers = {
            "Access-Control-Allow-Origin": "http://localhost:3000",
            "Access-Control-Allow-Headers": 'Content-Type, Accept, Origin',
            "Access-Control-Allow-Methods": "GET, POST, PUT, UPDATE, DELETE, OPTIONS",
        }
    else:
        # Standard request
        custom_headers = {
            # "Access-Control-Allow-Origin": "http://localhost:3000",
            # "Accept": "*/*",
            # "Content-type": 'application/json, text/html; charset=utf-8',
            "Access-Control-Allow-Origin": "http://localhost:3000",
            "Access-Control-Allow-Headers": 'Content-Type, Accept, Origin',
            "Access-Control-Allow-Methods": "GET, POST, PUT, UPDATE, DELETE, OPTIONS",
        }

    response.headers = {**response.headers, **custom_headers}

    return response


app.register_blueprint(api)


if __name__ == '__main__':
    app.run()
