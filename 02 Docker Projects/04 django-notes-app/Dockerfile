# ----1. Build Stage-----
FROM python:3.9-slim AS builder

WORKDIR /app/backend

COPY requirements.txt .
RUN apt-get update \
    && apt-get upgrade -y \
    && apt-get install -y gcc default-libmysqlclient-dev pkg-config \
    && rm -rf /var/lib/apt/lists/*

# Install app dependencies
RUN pip install mysqlclient
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# ----2. Runtime Stage-----
FROM python:3.9-slim
WORKDIR /app/backend

# Install runtime dependencies only
RUN apt-get update && \
    apt-get install -y --no-install-recommends libmariadb3 && \
    rm -rf /var/lib/apt/lists/*
COPY --from=builder /usr/local/lib/python3.9/site-packages/ /usr/local/lib/python3.9/site-packages/

# Below copy specifically for gunicorn as it is installed in another location
COPY --from=builder /usr/local/bin/ /usr/local/bin/

COPY . .

EXPOSE 8000
#RUN python manage.py migrate
#RUN python manage.py makemigrations
