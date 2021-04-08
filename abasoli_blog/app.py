from flask import Flask

from abasoli_blog.ext import configuration


def simple_app():
    app_name = __name__.split(".")[0]
    app = Flask(app_name)
    configuration.init_app(app)
    return app


def create_app():
    app = simple_app()
    configuration.load_extensions(app)
    return app
