"""gunicorn server configuration."""

from multiprocessing import cpu_count
from os import environ


workers = (cpu_count() * 2) + 1
worker_class = 'uvicorn.workers.UvicornWorker'
bind = ":" + environ.get("PORT", "8080")
