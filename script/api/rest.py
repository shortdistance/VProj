from flask import session, redirect, url_for, render_template, jsonify, request
from . import api
from script.models.area import Region, Area, District
from script.models.database import db_session

#area case 001
@api.route('/area/get_all_regions', method=['GET'])
def get_all_regions():
    """
    get all regions information
    """
    regions = Region.get_all_regions()
    return jsonify(regionlist=regions)


# api case 004
@api.route('/area/get_areas_under_region', method=['POST'])
def get_areas_under_region():
    """
    get all areas under a region information
    """
    region_abbr = request.json['RegionAbbr']
    areas = []
    ret_area = {}
    for area in Area.get_areas_under_region(region_abbr):
        ret_area['PostcodeAreaCode'] = area.PostcodeAreaCode
        ret_area['PostcodeAreaName'] = area.PostcodeAreaName
        ret_area['RegionAbbr'] = region_abbr
        ret_area['RegionName'] = area.RegionName
        areas.append(ret_area)
    return jsonify(areas=areas)

