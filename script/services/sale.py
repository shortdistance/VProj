from script.models.area import District
import re
import requests
import json
from script.config import ZOOPLER_KEY
from xml.etree.ElementTree import fromstring
from xmljson import parker, Parker


def price_analysis(price_flag):
    start_price = 0
    end_price = 0

    if str(price_flag) == '1':
        start_price = 0
        end_price = 100000

    elif str(price_flag) == '2':
        start_price = 100000
        end_price = 300000

    elif str(price_flag) == '3':
        start_price = 300000
        end_price = 700000

    elif str(price_flag) == '4':
        start_price = 700000
        end_price = 1000000

    elif str(price_flag) == '5':
        start_price = 1000000
        end_price = 2000000

    elif str(price_flag) == '6':
        start_price = 2000000
        end_price = 5000000

    elif str(price_flag) == '7':
        start_price = 5000000
        end_price = 10000000

    elif str(price_flag) == '8':
        start_price = 10000000
        end_price = 0
    else:
        pass

    return start_price, end_price


def type_analysis(type_flag):
    '''
        :param type_flag: The property type flag, 0: all, 1:Houses, 2:Flats, 3:Farms/Lands
        :return: type string
    '''
    type_str = None
    if type_flag == 1:
        type_str = 'Houses'

    elif type_flag == 2:
        type_str = 'Flats'

    elif type_flag == 3:
        type_str = 'Farms'
    else:
        pass

    return type_str


def sale_search(loc_str, price_flag, type_flag):
    loc_str = loc_str.strip()
    start_price, end_price = price_analysis(price_flag)
    type_str = type_analysis(type_flag)

    bexist = 0  # 0: not exist, 1: exist
    ptype = 0  # 0:nothing, 1:postcode, 2:postcode district, 3: city
    poutput = None

    try:
        if len(loc_str):
            loc_str = loc_str.upper()
            ret = re.findall(r'[A-Z]{1,2}[0-9][A-Z0-9]? [0-9][A-Z]{1,2}', loc_str)
            if ret and len(ret) == 1:
                # it maybe a postcode
                ptype = 1
                r = requests.get('http://api.postcodes.io/postcodes/%s' % loc_str)
                r_json = json.loads(r.content)
                if r_json['status'] == 200:  # if can search, it means the postcode is valid.
                    bexist = 1
                    sale_analysis = sale_analysis_of_district(loc_str, start_price, end_price,
                                                              type_str)
                    poutput = {'sale_analysis': sale_analysis}
            else:
                ret = re.findall(r'[A-Z]{1,2}[0-9][A-Z0-9]?', loc_str)
                if ret and len(ret) == 1:
                    # it maybe a postcode district
                    ptype = 2
                    district = District.get_district(loc_str)
                    if district:
                        bexist = 1
                        sale_analysis = sale_analysis_of_district(loc_str, start_price, end_price, type_str)
                        poutput = {'sale_analysis': sale_analysis}
                else:
                    # it maybe a city
                    ptype = 3
                    district_list = District.get_all_districts_under_city(loc_str)
                    if district_list:
                        bexist = 1
                        _city_analysis = sale_analysis_under_city(loc_str, start_price, end_price, type_str)
                        poutput = {'sale_analysis': _city_analysis, 'district_list': district_list}
    except Exception, e:
        bexist = 0
        ptype = 0
        poutput = None
    finally:
        return bexist, ptype, poutput


def sale_analysis_of_district(loc_str, start_price=None, end_price=None, type_str=None):
    '''
    http://api.zoopla.co.uk/api/v1/property_listings.xml?postcode=SO14&api_key=hkcbz38j32pqgepepv7nx5vu
    :param loc_str: 
    :param start_price: 
    :param end_price: 
    :param type_str: 
    :return: 
    '''
    ret_json = {}
    try:
        req_url = 'http://api.zoopla.co.uk/api/v1/property_listings.xml?postcode=%s&api_key=%s' % (loc_str, ZOOPLER_KEY)
        r = requests.get(req_url)
        if r.status_code == 200:
            ret_json = json.loads(json.dumps(parker.data(fromstring(r.content))))
    except Exception, e:
        pass
    return ret_json


def sale_analysis_under_city(loc_str, start_price=None, end_price=None, type_str=None):
    '''
    http://api.zoopla.co.uk/api/v1/property_listings.xml?area=Southampton&api_key=hkcbz38j32pqgepepv7nx5vu
    :param loc_str: 
    :param start_price: 
    :param end_price: 
    :param type_str: 
    :return: 
    '''
    ret_json = {}
    try:
        req_url = 'http://api.zoopla.co.uk/api/v1/property_listings.xml?area=%s&api_key=%s' % (loc_str, ZOOPLER_KEY)
        r = requests.get(req_url)
        if r.status_code == 200:
            ret_json = json.loads(json.dumps(parker.data(fromstring(r.content))))
    except Exception, e:
        pass
    return ret_json
