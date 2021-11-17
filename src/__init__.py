from flask import Flask

def create_app():
    app = Flask(__name__)

    @app.route("/")
    def base_route():
        return "this is a test"

    return app
