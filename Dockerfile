FROM python:3.7.0-alpine3.8
WORKDIR /app
COPY . /app
EXPOSE 8000
CMD ["python", "app.py"]

