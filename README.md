# Emlid docs

This is a repo containing all Emlid docs

# Dependencies

We use mkdocs to build the docs and Pipenv to manage the dependencies.

- python3
- python3-pip

```bash
git clone https://github.com/emlid/emlid-docs
pip3 install pipenv
cd emlid-docs
pipenv install
```



# Editing docs with templates


## Updating docs after editing templates (Generating markdown)

Template building script takes path to .yml file as an argument and rebuilds docs from every template specified in .yml.
*This should be run after making any changes to templates.*
```bash
cd emlid-docs
pipenv run python build.py <target>
# Where <target> is .yml config file.
# example
pipenv run python build.py reachm-plus.yml 
```
## Adding new templates

To add new template you need to create a jinja2 template in **emlid-docs/docs/templates/** with .mdx extension and add an entry to "templates" section of one or several .yml config files in following format. 
```yaml
templates:  # <- this should already be in the file
    destination: '<template-name.mdx>'
```
Where destination is the name of the file in **docs_dir** (docs_dir is specified in each .yml file) directory, that is going to be rendered via template.

And template_name name is the name of the actual template file with .mdx extension that must be placed inside **emlid-docs/doc/templates** directory.

**Without these entries template will be ignored.**

# Generating HTML

```bash
cd emlid-docs
pipenv run mkdocs build -f <target>.yml -d <dir>
```

This will build the \<target\> and save the generated docs to \<dir\>.

You can also `pipenv run mkdocs serve -f <target>.yml` to take a look at the docs on your local machine.


