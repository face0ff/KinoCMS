# syntax=docker/dockerfile:1
FROM python:3.9

WORKDIR /kinoCMS/

# set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
RUN pip install --upgrade pip
# copy project
COPY . .
COPY ./requirements.txt .
RUN pip install -r requirements.txt
