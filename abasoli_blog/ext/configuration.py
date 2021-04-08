from flask import Flask
from importlib import import_module
from os import getenv

from abasoli_blog.utils import path_handler
from config import config_selector


def load_extensions(app: Flask):
    abs_ext_path = path_handler.get_extension_absolute_path(app.name)
    relative_ext_path_in_python = path_handler.get_extension_python_path(app.name)
    file_list = path_handler.get_valid_file_list_gen(abs_ext_path)

    for file in file_list:
        module_path = f"{relative_ext_path_in_python}.{file}"
        module = import_module(module_path)
        module.init_app(app)


def init_app(app: Flask):
    config_type = getenv("FLASK_ENV")
    config_object = config_selector[config_type]
    app.config.from_object(config_object)
