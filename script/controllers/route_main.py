from flask import render_template, request
from . import bpmain
from script.models.area import Area, District
from script.services.hpp import hpp_search
import json
from filter import login_filter
from script.models.database import db_session

bpmain.before_request(login_filter)


@bpmain.after_request
def close_session_after_request(response):
    db_session.remove()
    return response


@bpmain.route('/hpp/search')
def search():
    return render_template('hpp/search.html')


@bpmain.route('/sale/search')
def sale_search():
    return render_template('sale/search.html')


@bpmain.route('/hpp/area/detail')
def get_a_area():
    loc_str = request.args.get('location')
    price_str = request.args.get('price-selection')
    date_str = request.args.get('daterange-selection')

    bexist, ptype, poutput = hpp_search(loc_str, price_str, date_str)
    qry_str = {
        'loc': loc_str,
        'price': price_str,
        'date': date_str
    }

    if bexist and poutput:
        return render_template('/hpp/details.html', qry_str=qry_str, bexist=bexist, ptype=ptype, poutput=poutput)
    else:
        return render_template('hpp/search.html')


@bpmain.route('/admin/<string:pagename>')
def admin(pagename):
    return render_template('admin/%s' % pagename)


@bpmain.route('/google/<string:pagename>')
def google(pagename):
    return render_template('google/%s' % pagename)
