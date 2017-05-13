from flask import render_template, request
from . import bpmain
from script.models.area import Area, District
from script.services.area import location_search
import json
from filter import login_filter
from script.models.database import db_session

bpmain.before_request(login_filter)


@bpmain.after_request
def close_session_after_request(response):
    db_session.remove()
    return response


@bpmain.route('/hpp/index')
def hpp():
    area_list = Area.get_all_areas()
    district_list = District.get_districts_under_area(area_list[0]['PostcodeAreaCode'])
    return render_template('hpp/index.html', area_list=json.dumps(area_list), district_list=json.dumps(district_list))


@bpmain.route('/hpp/index/<string:area_code>')
def hpp_link_area(area_code):
    area_list = Area.get_all_areas()
    district_list = District.get_districts_under_area(area_code)
    return render_template('hpp/index.html', area_list=json.dumps(area_list), district_list=json.dumps(district_list))


@bpmain.route('/hpp/area/detail')
def get_a_area():
    qry_str = request.args.get('location')
    bexist, ptype, poutput = location_search(qry_str)
    return render_template('/hpp/details.html', qry_str=qry_str, bexist=bexist, ptype=ptype, poutput=poutput)


@bpmain.route('/admin/<string:pagename>')
def admin(pagename):
    return render_template('admin/%s' % pagename)


@bpmain.route('/elementui/<string:pagename>')
def elementui(pagename):
    return render_template('elementui/%s' % pagename)


@bpmain.route('/google/<string:pagename>')
def google(pagename):
    return render_template('google/%s' % pagename)


@bpmain.route('/gmap_sidebar')
def gmap_sidebar():
    return render_template('google/gmap_sidebar.html')
