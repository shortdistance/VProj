from flask import Blueprint


bplogin = Blueprint('bplogin',__name__)
bpmain = Blueprint('bpmain', __name__)
bpmain_filter = Blueprint('bpmain_filter', __name__)

from . import route_login, route_main


