FROM python:3.9-slim

WORKDIR /app

COPY app/ .

RUN pip install -r requirements.txt

CMD ["flask", "run", "--host=0.0.0.0"]
