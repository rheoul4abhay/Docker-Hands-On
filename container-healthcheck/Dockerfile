FROM python:3.9-slim

WORKDIR /app

COPY . .

RUN pip install flask

CMD ["python", "app.py"]

HEALTHCHECK CMD curl --fail http://localhost:5000/ || exit 1
