from flask import Flask


def create_app():
    app = Flask(" ".join(__name__.split(".")[0].split("_")).title())

    print(app.name)

    return app
