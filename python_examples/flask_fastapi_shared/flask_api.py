from flask import Flask, jsonify, request
from python_examples.flask_fastapi_shared.domain import GreetingService


def create_app(service=None):
    app = Flask(__name__)
    service = service or GreetingService()

    @app.get("/api/greeting")
    def greeting():
        try:
            return jsonify(service.build(request.args.get("name", "")))
        except ValueError as exc:
            return jsonify(error=str(exc)), 400

    return app
