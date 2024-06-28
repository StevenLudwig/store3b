import os
from celery import Celery
from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'store.settings')

app = Celery('store')
app.conf.update(
    timezone=settings.TIME_ZONE,
    accept_content=['application/json'],
    result_serializer='json',
    task_serializer='json',
    result_backend='django-db',
    result_extended=True,
    broker_url=os.environ.get('REDIS_URL'),
    broker_connection_retry_on_startup=True,
    task_track_started=True
)
app.autodiscover_tasks()
