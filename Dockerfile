FROM python:3.9

COPY ./management /app

WORKDIR /app

RUN pip install -r requirements.txt

EXPOSE 8000

CMD ['python3', 'manage.py', 'runserver']