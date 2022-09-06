## Install

- clone repository
- move to project dir: `cd ./localherobox-fullstack-engineer-quest/backend`
- depending on OS make sure you're using the Python 3.10 
- install or upgrade `pip` to latest version

`python3 -m pip install --user --upgrade pip`

- install virtual environment

`python3 -m pip install --user virtualenv`

- create virtual environment for project

`python3 -m venv .env`

- activate the virtual environment

`source .env/bin/activate`

- install [Poetry packet manager](https://python-poetry.org/)

`pip install poetry` 

## Build

Run docker build command:

```commandline
docker build -t lhb-backend:0.1.0 . --no-cache
```

## Lint
Activate virtual environment `source .env/bin/activate`.

Uses `mypy` to check type hints and `flake8` to check code style and existence of docstrings. 

```commandline
make lint
```
## Test

Activate virtual environment `source .env/bin/activate`.

Run with: 

```commandline
make test
```
## Run

Run in development mode:

```commandline
make run
```

or using Docker, to start just the Python backend using the image built before (see step #Build):

````commandline
docker run -p 8000:8000 --name lhb-backend lhb-backend:0.1.0
````

ADD MORE INFO AS NECESSARY
