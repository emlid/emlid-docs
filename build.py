import yaml
import sys

from jinja2 import Template, Environment, FileSystemLoader, select_autoescape


data = {}
with open(sys.argv[1], "r") as conf:
    try:
        data = yaml.safe_load(conf)
    except yaml.YAMLError as exc:
            if hasattr(exc, 'problem_mark'):
                 mark = exc.problem_mark
                 print("Invalid syntax. Error at Line %s, Position %s" % (mark.line+1, mark.column+1))


env = Environment(
        loader=FileSystemLoader("templates/"),
        autoescape=select_autoescape(["html", "md"])
)

template = env.get_template("index_template.md")

print(template.render(data))
