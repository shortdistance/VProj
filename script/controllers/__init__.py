from flask import Blueprint
from script.models import database

main = Blueprint('main', __name__)

from . import route

'''
@main.after_request
def close_session_after_request(response):
    database.close_session()
    return response
'''
