import os

from src.templates import config_template, html_template, css_template

def create_dir(path):

    directory = os.path.join(os.getcwd(), path)

    if not os.path.exists(directory):
        os.makedirs(directory)

def setup_project():

    name = input("\n\x1b[1mCreate a new project |\x1b[33m name: \x1b[0m")

    with open("ecsm.config.json", "w") as json_config:
        json_config.write(config_template(name))

    create_dir("src")
    create_dir("src/css")
    create_dir("public")
    create_dir(".output")
    create_dir(".output/css")

    with open("src/index.html", "w") as index_html:
        index_html.write(html_template(name))

    with open("src/css/main.css", "w") as main_css:
        main_css.write(css_template(name))

    print(f"\n\x1b[1m\x1b[33m[{name}]\x1b[0m\x1b[1m successfully\x1b[32m created\x1b[0m")

    print(f"\n\x1b[1m\x1b[33m[{name}]\x1b[0m\x1b[1m auto compiler\x1b[0m running...")