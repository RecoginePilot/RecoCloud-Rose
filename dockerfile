# Use an official Python runtime as the base image
FROM python:3.8-buster as production-image

# Set the working directory in the container
WORKDIR /app

# Install python dependencies
COPY ./app/requirements.txt /app/
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# Run the FastAPI application
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
