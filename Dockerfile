FROM python:3.11-slim-buster
WORKDIR /app
COPY . /app
RUN pip install poetry && python -m poetry install -v --no-root --compile
CMD ["python", "main.py"]
