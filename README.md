<!-- omit in toc -->
# pirogramming-14th-django

피로그래밍 14기 Django Playground

<!-- omit in toc -->
## Table of Contents
- [Requirements](#requirements)
- [Installation](#installation)
- [Run](#run)

## Requirements

- Python 3.7+
- [Pipenv](https://github.com/pypa/pipenv)

## Installation

```sh
# macos, linux
export PIPENV_VENV_IN_PROJECT="enabled"

# windows
SET PIPENV_VENV_IN_PROJECT="enabled"

# installation
pipenv install --dev --three
```

## Run

```sh
# need migrate
pipenv run server/manage.py migrate

# run
pipenv run server/manage.py runserver 0.0.0.0:8000
```
