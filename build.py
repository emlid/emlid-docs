import yaml
import sys
import os

from jinja2 import Template, Environment, FileSystemLoader, select_autoescape



class Builder:
        def __init__(self, conf_path):
                self.templates_path = "./docs/templates/"
                self.env = Environment(
                        loader=FileSystemLoader(self.templates_path),
                        autoescape=select_autoescape(["html", "md"]))
                self.data = {}
                with open(conf_path, "r") as conf:
                        try:
                                self.data = yaml.safe_load(conf)
                        except yaml.YAMLError as exc:
                                if hasattr(exc, 'problem_mark'):
                                        mark = exc.problem_mark
                                        print("Invalid syntax")

        def render_template(self, destination, template_name):
                template = self.env.get_template(template_name)
                with open(self.data["docs_dir"] + "/"  + destination, "w") as dest:
                        dest.write(template.render(self.data))

        def render_all_templates(self):
                for dest, temp in self.data["templates"].items():
                        self.render_template(dest, temp)
if __name__ == "__main__":                        
    renderer = Builder(sys.argv[1])
    renderer.render_all_templates()
