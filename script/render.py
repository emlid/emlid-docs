import yaml
import sys
import os

from jinja2 import Template, Environment, FileSystemLoader, select_autoescape



class TemplateRenderer:
        def __init__(self):
                self.conf_path = "../conf/"
                self.reach_path = "../docs/reach/"
                self.autopilot_path = "../docs/autopilots/"
                self.templates_path = "../templates/"
                self.env = Environment(
                        loader=FileSystemLoader(self.templates_path),
                        autoescape=select_autoescape(["html", "md"]))
        def render_template(self, template_name, conf_name):
                data = {}
                current_conf_path = self.conf_path + conf_name
                model_path = self.reach_path + conf_name.split(".")[0] + "/"
                template = self.env.get_template(template_name)

                with open(current_conf_path, "r") as conf:
                        try:
                                data = yaml.safe_load(conf)
                        except yaml.YAMLError as exc:
                                if hasattr(exc, 'problem_mark'):
                                    mark = exc.problem_mark
                                    print(f"Invalid syntax. Error at Line {mark.line+1}, Position {mark.column+1}, In {conf}")
                with open(model_path + template_name, "w") as dest:
                        dest.write(template.render(data))
                        

        def update_template(self, template_name):
               for conf_name in os.listdir(self.conf_path):
                       self.render_template(template_name, conf_name)
                
        def update_everything(self):
                for template_name in [file for file in os.listdir(self.templates_path) if os.path.isfile(self.templates_path + file)]:
                        self.update_template(template_name)


renderer = TemplateRenderer()
renderer.update_everything()
