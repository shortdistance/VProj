from script.config import REDIS_URL, RABBITMQ_BIGWIG_URL, MONGODB_URI
from datetime import timedelta
from celery import Celery
from celery.task import periodic_task
from script.util import get_waves, get_tides
from script.models.mongodb import insert_db
import json
import os

redis_url = os.environ.get('REDIS_URL') or REDIS_URL
rabbit_url = os.environ.get('RABBITMQ_BIGWIG_URL') or RABBITMQ_BIGWIG_URL
mongodb_url = os.environ.get('MONGODB_URI') or MONGODB_URI

app = Celery('tasks',
             broker=rabbit_url)


@periodic_task(run_every=timedelta(seconds=15))
def a():
    waves_json = get_waves()
    tides_json = get_tides()

    if isinstance(waves_json, str):
        waves_json = json.loads(waves_json)

    if isinstance(tides_json, str):
        tides_json = json.loads(tides_json)

    json_data = {}
    if waves_json and tides_json:
        json_data = dict(waves_json=waves_json, tides_json=tides_json)
        insert_db(mongodb_url, json_data)

    return json_data


'''
#run command:
#celery worker -l info -A tasks --beat
'''
