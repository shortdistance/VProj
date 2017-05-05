from flask import Blueprint
from script.models import database

api = Blueprint('api', __name__)

# from . import


'''
@main.after_request
def close_session_after_request(response):
    database.close_session()
    return response
'''
