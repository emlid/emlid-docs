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
pipenv run mkdocs build -f <target>.yml -d <dir>
```

This will build the \<target\> and save the generated docs to \<dir\>.

You can also `pipenv run mkdocs serve -f <target>.yml` to take a look at the docs on your local machine.

# Generating markdown from templates

Template building script takes path to yaml file as an argument and rebuilds docs from every template associated with that file
```bash
cd emlid-docs
pipenv install
cd script
pipenv python render.py <target>
#example: pipenv run python ../reachrs.yml
```
