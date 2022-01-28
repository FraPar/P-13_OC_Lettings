# syntax=docker/dockerfile:1
FROM python:3.11.0a4-alpine3.15
MAINTAINER francois.parenti.gaming@gmail.com

ENV HOME=/

# create directory for the app user
RUN mkdir -p $HOME

# set work directory
WORKDIR $HOME


RUN pip install --upgrade pip
ADD requirements*.txt .
RUN pip install -r requirements.txt

EXPOSE 8000
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]