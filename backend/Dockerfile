FROM python:3.9-slim

WORKDIR /app

ENV PYTHONPATH="/app/src:${PYTHONPATH}"

COPY Pipfile Pipfile.lock* /app/

RUN pip install pipenv 
RUN pipenv install  --deploy --ignore-pipfile

COPY ./src /app/src
COPY ./tests /app/tests


EXPOSE 5000

CMD ["pipenv", "run", "python", "src/main.py"]