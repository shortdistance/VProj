# -*-coding:utf-8-*-
from flask import jsonify
from . import api
from script.util import get_waves, get_tides, get_met
import json


@api.route('/get_info')
def get_dataset():
    waves_json = get_waves()
    tides_json = get_tides()

    if isinstance(waves_json, str):
        waves_json = json.loads(waves_json)
        tides_json = json.loads(tides_json)

    return jsonify(waves_json=waves_json, tides_json=tides_json)
