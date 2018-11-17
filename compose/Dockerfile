FROM python:3.6.6

ENV PYTHONUNBUFFERED 1
RUN mkdir /app 
WORKDIR /app
ADD requirement.txt /app/requirement.txt
RUN pip install -r /app/requirement.txt
ADD . /app/
