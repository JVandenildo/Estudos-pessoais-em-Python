# this file turns the directory on a package
# anything inside this file will execute automatically when imported
from flask import Flask


def create_app():
    app = Flask(__name__)
    app.config["SECRET KEY"] = "eyiwgtngia DFGig"

    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix="/")
    app.register_blueprint(auth, url_prefix="/")

    return app
