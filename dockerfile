# Use an official Python runtime as the base image
FROM python:3.10.12-slim-bullseye as production-image

# Set the working directory in the container
WORKDIR /app

# Install python dependencies
COPY ./app/requirements.lock.txt /app/
COPY ./app/hypercorn.toml /app/
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.lock.txt
