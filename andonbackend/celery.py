import os
import random
from datetime import datetime, timedelta

from celery import Celery, shared_task

# Set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'andonbackend.settings')

app = Celery('andonbackend')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django apps.
app.autodiscover_tasks()


@app.task(bind=True, ignore_result=True)
def mainMailReadTask(arg):
    from production_monitoring.tasks import generate_random_production_count
    generate_random_production_count(arg)
    print("Generated random production count.")

@app.task(bind=True, ignore_result=True)
def deletetask(arg):
    from production_monitoring.tasks import delete_old_data
    delete_old_data(arg)
    print("Generated random production count.")

@app.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs):
    sender.add_periodic_task(1.0 * 60, mainMailReadTask.s())
    sender.add_periodic_task(24 * 60 * 60, deletetask.s())