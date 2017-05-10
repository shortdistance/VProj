from flask import session, redirect, url_for, render_template, jsonify, request
from . import main
from script.models.area import Area, District
from script.services.area import location_search


@main.route('/hpp/index')
def hpp():
    area_list = Area.get_all_areas()
    district_list = District.get_districts_under_area(area_list[0]['PostcodeAreaCode'])
    return render_template('hpp/index.html', area_list=area_list, district_list=district_list)


@main.route('/hpp/index/<string:area_code>')
def hpp_link_area(area_code):
    area_list = Area.get_all_areas()
    district_list = District.get_districts_under_area(area_code)
    return render_template('hpp/index.html', area_list=area_list, district_list=district_list)


@main.route('/hpp/area/detail', methods=['GET'])
def get_a_area():
    qry_str = request.args.get('location')
    bexist, ptype, poutput = location_search(qry_str)
    return render_template('/hpp/details.html', bexist=bexist, ptype=ptype, poutput=poutput)



@main.route('/admin/<string:pagename>')
def admin(pagename):
    return render_template('admin/%s' % pagename)


@main.route('/elementui/<string:pagename>')
def elementui(pagename):
    return render_template('elementui/%s' % pagename)


@main.route('/google/<string:pagename>')
def google(pagename):
    return render_template('google/%s' % pagename)


@main.route('/gmap_sidebar')
def gmap_sidebar():
    return render_template('google/gmap_sidebar.html')
