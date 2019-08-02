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
            if filename != "config_rtk.yml":
                data = yaml.safe_load(conf)
                template = env.get_template(sys.argv[1].split('/')[1])
                print(template.render(data))
        except yaml.YAMLError as exc:
                if hasattr(exc, 'problem_mark'):
                     mark = exc.problem_mark
                     print("Invalid syntax. Error at Line %s, Position %s" % (mark.line+1, mark.column+1))
