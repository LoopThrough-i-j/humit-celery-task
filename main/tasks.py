from celery import shared_task
from datetime import datetime

from main.lib import do_add_logs

@shared_task
def add_logs():
    log = "Logging at, "+ str(datetime.now())
    do_add_logs(log)
    return log
