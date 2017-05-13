from script.models.area import Region, Area, District
from script.services.hpp import hpp_analysis_under_city, hpp_analysis_of_district
import re
import requests
import json


def location_search(qry_str):
    qry_str = qry_str.strip()

    bexist = 0  # 0: not exist, 1: exist
    ptype = 0  # 0:nothing, 1:postcode, 2:postcode district, 3: city
    poutput = None
    try:
        if len(qry_str):
            qry_str = qry_str.upper()
            ret = re.findall(r'[A-Z]{1,2}[0-9][A-Z0-9]? [0-9][A-Z]{1,2}', qry_str)
            if ret and len(ret) == 1:
                # it maybe a postcode
                ptype = 1
                r = requests.get('http://api.postcodes.io/postcodes/%s' % qry_str)
                r_json = json.loads(r.content)
                if r_json['status'] == 200:  # if can search, it means the postcode is valid.
                    bexist = 1
                    district = District.get_district(r_json['result']['outcode'])
                    hpp_analysis = hpp_analysis_of_district(r_json['result']['outcode'])
                    poutput = {'district': district, 'hpp_analysis': hpp_analysis}
            else:
                ret = re.findall(r'[A-Z]{1,2}[0-9][A-Z0-9]?', qry_str)
                if ret and len(ret) == 1:
                    # it maybe a postcode district
                    ptype = 2
                    district = District.get_district(qry_str)
                    if district:
                        bexist = 1
                        hpp_analysis = hpp_analysis_of_district(qry_str)
                        poutput = {'district': district, 'hpp_analysis': hpp_analysis}
                else:
                    # it maybe a city
                    ptype = 3
                    district_list = District.get_all_districts_under_city(qry_str)
                    if district_list:
                        bexist = 1
                        _city_analysis, _district_hpp = hpp_analysis_under_city(qry_str)
                        poutput = {'district_list': district_list, 'hpp_analysis': _city_analysis,
                                   'district_hpp_analysis': _district_hpp}
    except Exception, e:
        pass
    finally:
        return (bexist, ptype, poutput)
