from flask import session, redirect, url_for, render_template, jsonify, request
from . import api
from script.models.area import Region, Area, District
from script.services.hpp import hpp_search


@api.route('/login_check', methods=['POST'])
def login_check():
    '''
    request.json
    {
        displayName: displayName,
        email: email,
        emailVerified: emailVerified,
        photoURL: photoURL,
        uid: uid,
        accessToken: accessToken,
        providerData: providerData
    }
    :return: 
    '''
    displayName = request.json['displayName']
    email = request.json['email']
    emailVerified = request.json['emailVerified']
    photoURL = request.json['photoURL']
    uid = request.json['uid']
    accessToken = request.json['accessToken']
    providerData = request.json['providerData']

    if accessToken:
        session['displayName'] = displayName
        session['email'] = email
        session['emailVerified'] = emailVerified
        session['photoURL'] = photoURL
        session['uid'] = uid
        session['accessToken'] = accessToken
        session['providerData'] = providerData

        if not session['photoURL']:
            session['photoURL'] = providerData[0]['photoURL']
        return jsonify(success=1)
    else:
        return jsonify(success=0)


# area case 001
@api.route('/area/get_all_regions', methods=['GET'])
def get_all_regions():
    """
    get all regions information
    """
    regions = Region.get_all_regions()
    return jsonify(regionlist=regions)


# api case 004
@api.route('/area/get_areas_under_region', methods=['POST'])
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


@api.route('/location/search', methods=['POST'])
def location_search_ajax():
    '''
    qry_str = request.json['location']
    bexist, ptype, poutput = hpp_search(qry_str)
    return jsonify(bexist=bexist, ptype=ptype, poutput=poutput)
    '''
    loc_str = request.args.get('location')
    price_str = request.args.get('price-selection')
    date_str = request.args.get('daterange-selection')

    bexist, ptype, poutput = hpp_search(loc_str, price_str, date_str)
    qry_str = {
        'loc': loc_str,
        'price': price_str,
        'date': date_str
    }
    return jsonify(qry_str=qry_str, bexist=bexist, ptype=ptype, poutput=poutput)