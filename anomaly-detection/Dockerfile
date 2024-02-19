FROM python:latest

RUN pip install requests
RUN pip install kubernetes
RUN pip install scikit-learn
RUN pip install prometheus-client
RUN pip install pandas

COPY ./app /app
WORKDIR /app

CMD [ "python main.py" ]
