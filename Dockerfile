FROM arm64v8/python:3

WORKDIR /usr/src/app

COPY irismodel.pkl ./irismodel.pkl
COPY prediction.py ./prediction.py
COPY requirements.txt ./requirements.txt
COPY server.py ./server.py

RUN pip install -r requirements.txt

EXPOSE 5000

CMD ["gunicorn", "--bind", "0.0.0.0:5000", "server:app"]

