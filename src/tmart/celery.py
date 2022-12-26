from __future__ import absolute_import, unicode_literals

import os

from celery import Celery
from celery.schedules import crontab

import logging
from django.conf import settings


logger = logging.getLogger("Celery")

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tmart.settings')

app = Celery('tmart')
app.config_from_object('django.conf:settings', namespace="CELERY")
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)
app.task(bind=True, ignore_result=False)


app.conf.beat_schedule = {
    'send_new_product_notification': {
        'task': 'product.tasks.send_new_product_notifications',
        'schedule': crontab(minute='20', hour='13', day_of_week='monday' ),
        'schedule' : 2,
    },

    'send_new_product_to_subscribers': {
        'task': 'product.tasks.send_new_product_to_subscribers',
        'schedule': crontab(minute='20', hour='13', day_of_week='monday' ),
        'schedule' : 2,
    },
}


