# movies_company/celery.py

import os
from celery import Celery

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings.prod")
app = Celery("movies_company")
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()

