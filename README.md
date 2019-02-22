# Emlid docs

This is a repo containing all Emlid docs

# Dependencies

We use mkdocs to build the docs and Pipenv to manage the dependencies.

- python3
- python3-pip

# Building

```bash
git clone https://github.com/emlid/emlid-docs
pip3 install pipenv
cd emlid-docs
pipenv install
pipenv run mkdocs build -f <target>.yml -d <dir>
```

This will build the <target> and save the generated docs to <dir>.
