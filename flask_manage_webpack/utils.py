import os
import errno
import shutil


def copy(src, destination):
    try:
        shutil.copytree(src, destination)
    except OSError as e:
        # If the error was caused because the source wasn't a directory
        if e.errno == errno.ENOTDIR:
            shutil.copy(src, destination)
        else:
            print(f'assets folder initialized failed. {e}')


def init_webpack_config(app_name):

    edit_template = ["package.json",
                     "postcss.config.js",
                     "webpack.config.js"]

    current_path = os.path.dirname(os.path.abspath(__file__))
    template_path = os.path.join(current_path, "template")
    assets_path = os.path.join(template_path, "assets")

    for template in edit_template:
        # Prevent file overwrite
        if os.path.isfile(template) is False:
            with open(f"{template_path}/{template}", "rt") as file_in:
                with open(template, "wt") as file_out:
                    for line in file_in:
                        file_out.write(line.replace("app", app_name))
        else:
            print(f"{template} initialized failed. File exists.")

    copy(assets_path, f"{os.getcwd()}/assets")

