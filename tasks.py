from script.config import REDIS_URL, RABBITMQ_BIGWIG_URL
from datetime import timedelta
from celery import Celery
from celery.task import periodic_task
from script.util import get_waves, get_tides
import json
import os

redis_url = os.environ.get('REDIS_URL') or  REDIS_URL
rabbit_url = os.environ.get('RABBITMQ_BIGWIG_URL') or RABBITMQ_BIGWIG_URL


app = Celery('tasks', backend=redis_url,
             broker=rabbit_url)


@periodic_task(run_every=timedelta(seconds=15))
def a():
    waves_json = get_waves()
    tides_json = get_tides()

    if isinstance(waves_json, str):
        waves_json = json.loads(waves_json)
        tides_json = json.loads(tides_json)

    return dict(waves_json=waves_json, tides_json=tides_json)


'''
#run command:
#celery worker -l info -A tasks --beat
'''
