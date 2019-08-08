import yaml
import sys
import os

from jinja2 import Template, Environment, FileSystemLoader, select_autoescape


env = Environment(
        loader=FileSystemLoader("templates/"),
        autoescape=select_autoescape(["html", "md"])
)

for filename in os.listdir("conf"):
    data = {}
    with open("conf/" + filename, "r") as conf:
        try:
            data = yaml.safe_load(conf)
            template = env.get_template("index_template.md")
            with open("docs/reach/" + filename.split("_")[1].split(".")[0] + "/index.md", "w") as dest:
                dest.write(template.render(data))
        except yaml.YAMLError as exc:
                if hasattr(exc, 'problem_mark'):
                     mark = exc.problem_mark
                     print("Invalid syntax. Error at Line %s, Position %s" % (mark.line+1, mark.column+1))
