FROM arm64v8/python:3

WORKDIR /usr/src/app

COPY prediction.py ./prediction.py
COPY requirements.txt ./requirements.txt
COPY wsgi.py ./wsgi.py

RUN pip install -r requirements.txt

EXPOSE 5000

CMD ["gunicorn", "--bind", "0.0.0.0:5000", "serer:app", "8080"]

