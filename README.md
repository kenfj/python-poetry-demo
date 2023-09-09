# Python Poetry Demo

* as of Sep 2023: python 3.11 poetry 1.6.1
* [Setup Python](#setup-python)
* [Setup Poetry](#setup-poetry)
* [setup project](#setup-project)
* [manage packages](#manage-packages)
* [Run FastAPI](#run-fastapi)
* [Run PyTest](#run-pytest)

## Setup Python

* https://github.com/pyenv/pyenv#homebrew-in-macos

```bash
# brew install or upgrade pyenv
brew update
brew install pyenv
brew upgrade pyenv

pyenv --version
# pyenv 2.3.26

pyenv install -l | grep 3.11
pyenv install 3.11
pyenv global 3.11

pyenv versions
#   system
# * 3.11.5 (set by ~/.pyenv/version)

python --version
# Python 3.11.5
```

## Setup Poetry

* https://python-poetry.org/docs/

```bash
export POETRY_HOME=/opt/poetry
export PATH="$POETRY_HOME/bin:$PATH"

curl -sSL https://install.python-poetry.org | POETRY_HOME=/opt/poetry python3 -

poetry --version
# Poetry (version 1.6.1)

poetry completions zsh > ~/.zfunc/_poetry
```

* update .zshrc

```bash
export PYTHONDONTWRITEBYTECODE=1

export POETRY_HOME=/opt/poetry
export PATH="$POETRY_HOME/bin:$PATH"
fpath+=~/.zfunc
autoload -Uz compinit && compinit
```

## Setup Project

```bash
poetry new poetry-demo --src
cd poetry-demo

poetry config --list

poetry config virtualenvs.in-project true
# in ~/Library/Application\ Support/pypoetry/config.toml
poetry config virtualenvs.in-project true --local
# in poetry.toml

poetry env info
poetry env list

# create .venv
poetry env use 3.11
```

## Manage Packages

```bash
poetry add requests
poetry show
poetry remove requests

# install from poetry.lock
poetry install

poetry update --dry-run
poetry update

poetry self update

poetry run python -V
# Python 3.11.5
poetry shell

poetry check
# All set!
```

## Run FastAPI

* https://qiita.com/XPT60/items/deac8d6155da58afbb6f

```bash
poetry add fastapi uvicorn

# add src/main.py

# maybe you don't need this
# export PYTHONPATH="./src:${PYTHONPATH}"

poetry run uvicorn main:app --reload

curl http://127.0.0.1:8000/
# {"msg":"Hello World"}

# OpenAPI docs
# http://localhost:8000/docs
```

## Run PyTest

```bash
poetry add pytest pytest-cov httpx --group dev

# add tests/test_main.py

poetry run pytest
poetry run pytest --cov=src -v
poetry run pytest --cov=src -v --cov-report=html

python -m http.server -d ./htmlcov 8001
# http://localhost:8001/
```
