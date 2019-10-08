from build import Builder
import sys, os


if __name__ == "__main__":                        
    renderer = Builder(sys.argv[1])
    renderer.render_all_templates()
    os.system("mkdocs serve -f" + sys.argv[1])
