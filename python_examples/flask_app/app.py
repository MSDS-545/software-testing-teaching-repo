from flask import Flask, jsonify, request
from python_examples.flask_app.service import greeting


def create_app() -> Flask:
    app = Flask(__name__)

    @app.get("/health")
    def health():
        return jsonify(status="ok")

    @app.get("/api/greeting")
    def api_greeting():
        name = request.args.get("name", "")
        try:
            message = greeting(name)
        except ValueError as exc:
            return jsonify(error=str(exc)), 400
        return jsonify(message=message)

    return app


if __name__ == "__main__":
    create_app().run(debug=True)
