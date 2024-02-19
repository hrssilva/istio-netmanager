FROM python:latest

WORKDIR /code

RUN pip install requests
RUN pip install kubernetes
RUN pip install sklearn
RUN pip install prometheus_client

COPY ./src/ ./

CMD python -u main.py