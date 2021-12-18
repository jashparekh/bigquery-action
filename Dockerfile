FROM python:3-slim AS builder
ADD . /app
WORKDIR /app

# We are installing a dependency here directly into our app source dir
RUN pip install --target=/app -r plugin_scripts/requirements.lock
ENV PYTHONPATH /app

CMD ["python", "/app/plugin_scripts/__init__.py"]
