from script.models.hpp import DistrictYearMonthHpp, DistrictYearHpp
from script.models.area import Region, Area, District
import collections


def hpp_analysis_of_district(district, start_year=None, end_year=None):
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

    year_hpp_list = DistrictYearHpp.get_district_year_hpp(district, start_year, end_year)
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
        except ZeroDivisionError,e:
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
            #_total_year['_incr_rate'][k_list[i]] = round(float(v_list[i] - v_list[i - 1]) / v_list[i - 1], 2)
            _total_year['_incr_rate'][k_list[i]] = round(float(v_list[i] - v_list[i - 1]) / v_list[i - 1] / (int(k_list[i]) - int(k_list[i - 1])), 2)
            #_total_incs_rate += _total_year['_incr_rate'][k_list[i]]
            _total_incs_rate += _total_year['_incr_rate'][k_list[i]]*(int(k_list[i]) - int(k_list[i - 1]))
    try:
        #_total_year['_incr_rate']['_total'] = round(float(_total_incs_rate) / _total_year['_len']['_total'], 2)
        _total_year['_incr_rate']['_total'] = round(float(_total_incs_rate) / (int(k_list[-1]) - int(k_list[0])), 2)
    except ZeroDivisionError,e:
        _total_year['_incr_rate']['_total'] = 0

    return _total_year


def hpp_analysis_under_city(city_name, start_year=None, end_year=None):
    district_list = District.get_all_districts_under_city(city_name)
    # to save total
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

    for district in district_list:
        year_hpp_list = DistrictYearHpp.get_district_year_hpp(district['PostcodeDistrict'], start_year, end_year)
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
        except ZeroDivisionError,e:
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
            try:
                _total_year['_incr_rate'][k_list[i]] = round(
                    float(v_list[i] - v_list[i - 1]) / v_list[i - 1] / (int(k_list[i]) - int(k_list[i - 1])), 2)
            except ZeroDivisionError,e:
                _total_year['_incr_rate'][k_list[i]] = 0

            _total_incs_rate += _total_year['_incr_rate'][k_list[i]] * (int(k_list[i]) - int(k_list[i - 1]))
    _total_year['_incr_rate']['_total'] = round(float(_total_incs_rate) / (int(k_list[-1]) - int(k_list[0])), 2)

    return _total_year

