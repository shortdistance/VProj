from flask import Blueprint
from script.models.database import db_session

main = Blueprint('main', __name__)

from . import route


@main.after_request
def close_session_after_request(response):
    db_session.remove()
    return response

