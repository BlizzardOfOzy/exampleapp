FROM python:3-alpine

RUN pip install flask pymongo

COPY ./app.py .

CMD [ "flask", "run", "--host=0.0.0.0" ]