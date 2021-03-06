FROM python:3-alpine

RUN pip install flask pymongo prometheus-flask-exporter

COPY ./app.py .

COPY ./images ./static/images/

COPY ./templates ./templates/

CMD [ "flask", "run", "--host=0.0.0.0" ]