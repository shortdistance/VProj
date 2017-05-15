from script.models.area import Region, Area, District
from script.models.hpp import DistrictYearHpp
import collections
import re
import requests
import json
from datetime import datetime


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


def date_range_analysis(date_flag):
    start_date = None
    end_date = None
    this_year = datetime.now().year

    if str(date_flag) == '1':
        start_date = '%d' % (int(this_year) - 2)
        end_date = '%d' % int(this_year)
    elif str(date_flag) == '2':
        start_date = '%d' % (int(this_year) - 5)
        end_date = '%d' % int(this_year)
    elif str(date_flag) == '3':
        start_date = '%d' % (int(this_year) - 10)
        end_date = '%d' % int(this_year)
    else:
        pass
    return start_date, end_date


def hpp_search(loc_str, price_flag, date_flag):
    loc_str = loc_str.strip()
    start_price, end_price = price_analysis(price_flag)
    start_date, end_date = date_range_analysis(date_flag)
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
                    district = District.get_district(r_json['result']['outcode'])
                    district_list = []
                    district_list.append(district)
                    hpp_analysis = hpp_analysis_of_district(r_json['result']['outcode'], start_price, end_price,
                                                            start_date, end_date)
                    _district_hpp = {}
                    _district_hpp[r_json['result']['outcode']] = hpp_analysis
                    poutput = {'district_list': district_list, 'hpp_analysis': hpp_analysis,
                               'district_hpp_analysis': _district_hpp}
            else:
                ret = re.findall(r'[A-Z]{1,2}[0-9][A-Z0-9]?', loc_str)
                if ret and len(ret) == 1:
                    # it maybe a postcode district
                    ptype = 2
                    district = District.get_district(loc_str)
                    if district:
                        bexist = 1

                        district_list = []
                        district_list.append(district)
                        hpp_analysis = hpp_analysis_of_district(loc_str, start_price, end_price, start_date, end_date)
                        _district_hpp = {}
                        _district_hpp[loc_str] = hpp_analysis
                        poutput = {'district_list': district_list, 'hpp_analysis': hpp_analysis,
                                   'district_hpp_analysis': _district_hpp}
                else:
                    # it maybe a city
                    ptype = 3
                    district_list = District.get_all_districts_under_city(loc_str)
                    if district_list:
                        bexist = 1
                        new_district_list, _city_analysis, _district_hpp = hpp_analysis_under_city(loc_str, start_price, end_price,
                                                                                start_date, end_date)
                        poutput = {'district_list': new_district_list, 'hpp_analysis': _city_analysis,
                                   'district_hpp_analysis': _district_hpp}
    except Exception, e:
        pass
    finally:
        return (bexist, ptype, poutput)


def hpp_analysis_of_district(district, start_price=0, end_price=0, start_year=None, end_year=None):
    _total_year = {
        '_count': {},
        '_price': {},
        '_avg_price': {},
        '_len': {},
        '_incr_rate': {},
        '_D': {},
        '_S': {},
        '_T': {},
        '_F': {},
        '_N': {},
        '_O': {},
        '_Y': {},
        '_N': {},
    }

    year_hpp_list = DistrictYearHpp.get_district_year_hpp(district, start_price, end_price, start_year, end_year)
    if year_hpp_list:
        for year_hpp in year_hpp_list:
            if _total_year['_count'].get('_total'):
                _total_year['_count']['_total'] += year_hpp['Count']
            else:
                _total_year['_count']['_total'] = year_hpp['Count']

            if _total_year['_count'].get(year_hpp['Year']):
                _total_year['_count'][year_hpp['Year']] += year_hpp['Count']
            else:
                _total_year['_count'][year_hpp['Year']] = year_hpp['Count']

            if _total_year['_price'].get('_total'):
                _total_year['_price']['_total'] += year_hpp['Price']
            else:
                _total_year['_price']['_total'] = year_hpp['Price']

            if _total_year['_len'].get('_total'):
                _total_year['_len']['_total'] += 1
            else:
                _total_year['_len']['_total'] = 1

            if _total_year['_len'].get(year_hpp['Year']):
                _total_year['_len'][year_hpp['Year']] += 1
            else:
                _total_year['_len'][year_hpp['Year']] = 1

            if _total_year['_price'].get(year_hpp['Year']):
                _total_year['_price'][year_hpp['Year']] += year_hpp['Price']
            else:
                _total_year['_price'][year_hpp['Year']] = year_hpp['Price']

            if _total_year['_D'].get('_total'):
                _total_year['_D']['_total'] += year_hpp['D']
            else:
                _total_year['_D']['_total'] = year_hpp['D']

            if _total_year['_D'].get(year_hpp['Year']):
                _total_year['_D'][year_hpp['Year']] += year_hpp['D']
            else:
                _total_year['_D'][year_hpp['Year']] = year_hpp['D']

            if _total_year['_S'].get('_total'):
                _total_year['_S']['_total'] += year_hpp['S']
            else:
                _total_year['_S']['_total'] = year_hpp['S']

            if _total_year['_S'].get(year_hpp['Year']):
                _total_year['_S'][year_hpp['Year']] += year_hpp['S']
            else:
                _total_year['_S'][year_hpp['Year']] = year_hpp['S']

            if _total_year['_T'].get('_total'):
                _total_year['_T']['_total'] += year_hpp['T']
            else:
                _total_year['_T']['_total'] = year_hpp['T']

            if _total_year['_T'].get(year_hpp['Year']):
                _total_year['_T'][year_hpp['Year']] += year_hpp['T']
            else:
                _total_year['_T'][year_hpp['Year']] = year_hpp['T']

            if _total_year['_F'].get('_total'):
                _total_year['_F']['_total'] += year_hpp['F']
            else:
                _total_year['_F']['_total'] = year_hpp['F']

            if _total_year['_F'].get(year_hpp['Year']):
                _total_year['_F'][year_hpp['Year']] += year_hpp['F']
            else:
                _total_year['_F'][year_hpp['Year']] = year_hpp['F']

            if _total_year['_O'].get('_total'):
                _total_year['_O']['_total'] += year_hpp['O']
            else:
                _total_year['_O']['_total'] = year_hpp['O']

            if _total_year['_O'].get(year_hpp['Year']):
                _total_year['_O'][year_hpp['Year']] += year_hpp['O']
            else:
                _total_year['_O'][year_hpp['Year']] = year_hpp['O']

            if _total_year['_Y'].get('_total'):
                _total_year['_Y']['_total'] += year_hpp['Y']
            else:
                _total_year['_Y']['_total'] = year_hpp['Y']

            if _total_year['_Y'].get(year_hpp['Year']):
                _total_year['_Y'][year_hpp['Year']] += year_hpp['Y']
            else:
                _total_year['_Y'][year_hpp['Year']] = year_hpp['Y']

            if _total_year['_N'].get('_total'):
                _total_year['_N']['_total'] += year_hpp['N']
            else:
                _total_year['_N']['_total'] = year_hpp['N']

            if _total_year['_N'].get(year_hpp['Year']):
                _total_year['_N'][year_hpp['Year']] += year_hpp['N']
            else:
                _total_year['_N'][year_hpp['Year']] = year_hpp['N']

        for key in _total_year['_price']:
            try:
                _total_year['_avg_price'][key] = int(float(_total_year['_price'][key]) / _total_year['_len'][key])
            except ZeroDivisionError, e:
                _total_year['_avg_price'][key] = 0

        od = collections.OrderedDict(sorted(_total_year['_avg_price'].items()))
        od.pop('_total')
        k_list = []
        v_list = []
        for k, v in od.iteritems():
            k_list.append(k)
            v_list.append(v)

        _total_incs_rate = 0
        for i in xrange(len(k_list)):
            if i == 0:
                _total_year['_incr_rate'][k_list[0]] = 0
            else:
                _total_year['_incr_rate'][k_list[i]] = round(float(v_list[i] - v_list[i - 1]) / v_list[i - 1], 2)
                # _total_year['_incr_rate'][k_list[i]] = round(float(v_list[i] - v_list[i - 1]) / v_list[i - 1] / (int(k_list[i]) - int(k_list[i - 1])), 2)
                _total_incs_rate += _total_year['_incr_rate'][k_list[i]]
                # _total_incs_rate += _total_year['_incr_rate'][k_list[i]] * (int(k_list[i]) - int(k_list[i - 1]))
        try:
            _total_year['_incr_rate']['_total'] = round(float(_total_incs_rate) / _total_year['_len']['_total'], 2)
            # _total_year['_incr_rate']['_total'] = round(float(_total_incs_rate) / (int(k_list[-1]) - int(k_list[0])), 2)
        except ZeroDivisionError, e:
            _total_year['_incr_rate']['_total'] = 0

        return _total_year
    else:
        return None


def hpp_analysis_under_city(city_name, start_price, end_price, start_date, end_date):
    district_list = District.get_all_districts_under_city(city_name)
    new_district_list = []
    # to save total
    _city_analysis = {
        '_count': {},
        '_price': {},
        '_avg_price': {},
        '_len': {},
        '_incr_rate': {},
        '_D': {},
        '_S': {},
        '_T': {},
        '_F': {},
        '_N': {},
        '_O': {},
        '_Y': {},
        '_N': {},
    }

    _district_hpp = {}
    for district in district_list:
        district_hpp_analysis = hpp_analysis_of_district(district['PostcodeDistrict'], start_price, end_price,
                                                         start_date, end_date)
        if district_hpp_analysis:
            new_district_list.append(district)
            _district_hpp[district['PostcodeDistrict']] = district_hpp_analysis


    if _district_hpp:
        for each_city_hpp in _district_hpp.values():
            for k in each_city_hpp.keys():
                for k1 in each_city_hpp[k].keys():
                    if _city_analysis[k].has_key(k1):
                        _city_analysis[k][k1] += each_city_hpp[k][k1]
                    else:
                        _city_analysis[k][k1] = each_city_hpp[k][k1]

        for k in _city_analysis['_avg_price'].keys():
            if k != '_total':
                _city_analysis['_avg_price'][k] = int(float(_city_analysis['_avg_price'][k]) / _city_analysis['_len'][k])
                _city_analysis['_incr_rate'][k] = round(float(_city_analysis['_incr_rate'][k]) / _city_analysis['_len'][k],
                                                        2)
            else:
                _city_analysis['_avg_price'][k] = int(
                    float(_city_analysis['_avg_price'][k]) * len(_city_analysis['_avg_price'].keys()) /
                    _city_analysis['_len'][k])
                _city_analysis['_incr_rate'][k] = round(
                    float(_city_analysis['_incr_rate'][k]) * len(_city_analysis['_avg_price'].keys()) /
                    _city_analysis['_len'][k], 2)

    return new_district_list, _city_analysis, _district_hpp
