FROM python:3.9

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /src/
COPY requirements.txt /src/

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY . /src/