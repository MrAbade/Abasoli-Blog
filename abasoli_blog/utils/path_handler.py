from os.path import abspath
from os import walk


def get_extension_absolute_path(app_name: str):
    extensions_path = abspath(f"{app_name}/ext")
    return extensions_path


def get_extension_python_path(app_name: str):
    extensions_path_in_python = f"{app_name}.ext"
    return extensions_path_in_python


def get_files_in_path(abs_path):
    _, _, file_list = next(walk(abs_path))
    return file_list


def get_valid_file_list_gen(abs_path):
    yield from (
        file.replace(".py", "")
        for file in get_files_in_path(abs_path)
        if "__init__" not in file
    )
