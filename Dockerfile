FROM python:3.10-slim

WORKDIR /app
COPY . /app

# Install system dependencies for image generation if needed
RUN apt-get update && apt-get install -y libgl1-mesa-glx

RUN pip install --upgrade pip
RUN pip install flask pillow flask-sqlalchemy transformers diffusers torch

EXPOSE 5000
CMD ["python", "app.py"]
