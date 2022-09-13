FROM python:3.10 as requirements-stage

WORKDIR /tmp

RUN pip install poetry

COPY pyproject.toml poetry.lock* /tmp/

RUN poetry export -f requirements.txt --output requirements.txt --without-hashes

FROM python:3.10

WORKDIR /

RUN mkdir -p /data
COPY ../data /data

WORKDIR /code

COPY --from=requirements-stage /tmp/requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY src /code/app

COPY start.sh /code/start.sh
RUN chmod +x /code/start.sh

CMD ["/code/start.sh"]