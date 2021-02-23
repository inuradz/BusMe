FROM python:3

ADD hello.py .
ADD requirements.txt .

RUN pip install -r requirements.txt

ENV FLASK_APP hello.py

CMD ["flask", "run"]