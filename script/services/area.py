from script.models.area import Region, Area, District
import re
import requests
import json
import logging


def location_search(qry_str):
    qry_str = qry_str.strip()
    logging.info(qry_str)

    bexist = False
    ptype = 0  # 0:nothing, 1:postcode, 2:postcode district, 3: city
    poutput = None
    try:
        if len(qry_str):
            qry_str = qry_str.upper()
            ret = re.findall(r'[A-Z]{1,2}[0-9][A-Z0-9]? [0-9][ABD-HJLNP-UW-Z]', qry_str)
            if ret and len(ret) == 1:
                # it maybe a postcode
                ptype = 1
                r = requests.get('http://api.postcodes.io/postcodes/%s' % qry_str)
                r_json = json.loads(r.content)
                if r_json['status'] == 200:  # if can search, it means the postcode is valid.
                    bexist = True
                    poutput = r_json

            else:
                ret = re.findall(r'[A-Z]{1,2}[0-9][A-Z0-9]?', qry_str)
                if ret and len(ret) == 1:
                    # it maybe a postcode district
                    ptype = 2
                    r = District.get_district(qry_str)
                    if r:
                        bexist = True
                        poutput = r

                else:
                    # it maybe a city
                    ptype = 3
                    r = District.get_all_districts_under_city(qry_str)
                    if r:
                        bexist = True
                        poutput = r
    except Exception, e:
        pass
    finally:
        return (bexist, ptype, poutput)
