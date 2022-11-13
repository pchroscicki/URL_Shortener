# Pull base image
FROM python:3.10.2-slim-bullseye
RUN apt-get update && apt-get install -y cron

# Set environment variables
ENV PIP_DISABLE_PIP_VERSION_CHECK 1
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set work directory
WORKDIR /code

# Install dependencies
COPY ./requirements.txt .
RUN pip install -r requirements.txt

# Copy project
COPY . .

# Add crontab
RUN python3 manage.py crontab add .