FROM python:3.7-slim

ENV APP_HOME /app
WORKDIR $APP_HOME
COPY . ./

RUN pip install FastAPI gunicorn uvicorn

CMD gunicorn --bind 0.0.0.0 app:app -w 4 -k uvicorn.workers.UvicornWorker