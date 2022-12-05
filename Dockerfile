# pull official base image
FROM python:3.8

# set work directory
WORKDIR /seriesflix


# set environment variables
ENV LANG C.UTF-8
ENV LC_ALL C.UTF-8
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONFAULTHANDLER 1


# install dependencies
# RUN apt-get update && apt-get install -y --no-install-recommends gcc


RUN pip install --upgrade pip
RUN pip install pipenv
COPY Pipfile Pipfile.lock ./
RUN pipenv install --system


# copy project
COPY . .

