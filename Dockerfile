# syntax=docker/dockerfile:1
FROM python:3.11.0a4-alpine3.15
MAINTAINER francois.parenti.gaming@gmail.com

# set the working directory in the container
WORKDIR /django

# copy the dependencies file to the working directory
COPY requirements.txt /django

# install dependencies
RUN pip install -r requirements.txt

RUN pip install --upgrade pip
ADD requirements*.txt .
RUN pip install -r requirements.txt

# copy the content of the local src directory to the working directory
COPY . /django

EXPOSE 8000
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]