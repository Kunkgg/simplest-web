FROM python:3.7.0-alpine3.8
WORKDIR /app
COPY . /app
RUN python host_info.py
EXPOSE 8000
CMD ["python", "-m", "http.server"]

