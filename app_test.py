from script.models.area import Region, Area, District
from script.models.hpp import DistrictYearHpp, DistrictYearMonthHpp
from script.services.hpp import hpp_analysis_under_city, hpp_analysis_of_district
import requests,json

# area case 001
print("##########test Region.get_all_regions()")
print(len(Region.get_all_regions()))

# area case 002
print("##########test Region.get_region(region_abbr)")
region_abbr = 'NE'
print(Region.get_region(region_abbr).RegionName)

# area case 003
print("##########test Area.get_areas_under_region(region_addr)")
region_abbr = 'NW'
print(Area.get_areas_under_region(region_abbr))

# api case 004
'''
NE:5
NW: 14
YtH: 10
EM: 5
WM: 10
East: 7 
L: 20
SE: 16
SW: 12
E: 
S: 16
W: 5 
'''
print("##########test Area.get_areas_under_region(region_addr)")
areas = []
ret_area = {}
region_abbr = 'S'
print region_abbr
areas = Area.get_areas_under_region(region_abbr)
print (areas)

# area case 005
print("##########test Area.get_area_by_code(area_code)")
area_code = 'SO'
print(Area.get_area_by_code(area_code))

# area case 006
print("##########test Area.get_all_areas()")
print(Area.get_all_areas())

# area case 007
print("##########test District.get_district(district)")
district = 'SO14'
print(District.get_district(district))

# area case 008
print("##########test get_districts_under_area(area)")
area_code = 'SO'
print(District.get_districts_under_area(area_code))

# area case 009
print("##########test get_all_districts()")
print(District.get_all_districts())

# area case 010
print("##########test get_all_districts_under_city(city_name)")
city_name = 'London'
print(len(District.get_all_districts_under_city(city_name)))

# area case 011
print("##########test get_all_cities_under_region(region_abbr)")
region_abbr = 'NE'
print(District.get_all_cities_under_region(region_abbr))

# rest case 012
print("##########test api.location_search")
from script.services.area import location_search
print(location_search('Southampton'))


#hpp case 013
print("#########3test DistrictYearHpp.get_district_hpp")
print(DistrictYearHpp.get_district_hpp('SO16'))


#hpp case 014
print("#########3test DistrictYearMonthHpp")
print(DistrictYearMonthHpp.get_district_hpp('SO14'))

#hpp case 015
print("#########test DistrictYearHpp.get_district_year_hpp")
print(DistrictYearHpp.get_district_year_hpp('SO14', '2000','2008'))

#hpp case 016
print("#########test DistrictYearMonthHpp.get_district_year_hpp")
print(DistrictYearMonthHpp.get_district_year_month_hpp('SO14', '200001','200801'))

#hpp service case 017
print("#########test hpp service.hpp_analysis_under_city(city_name, start_year, end_year)")
_city_analysis, _district_hpp = hpp_analysis_under_city('Southampton')

d1 = json.dumps(_city_analysis, sort_keys=True, indent=4, ensure_ascii=False, separators=(',',':'))
print d1
#d2 = json.dumps(_district_hpp, sort_keys=True, indent=4, ensure_ascii=False, separators=(',',':'))
#print d2

#hpp service case 018
print("#########test hpp service.hpp_analysis_of_district(district, start_year, end_year)")
my_json = hpp_analysis_of_district('SO15')
d1 = json.dumps(my_json, sort_keys=True, indent=4, ensure_ascii=False, separators=(',',':'))


#area service case 019
print("##########test area service, ptype:2##########")
import re
qry_str = 'SO14'
ret = re.findall(r'[A-Z]{1,2}[0-9][A-Z0-9]?', qry_str)
if ret and len(ret) == 1:
    # it maybe a postcode district
    ptype = 2
    district = District.get_district(qry_str)
    if district:
        bexist = 1
        hpp_analysis = hpp_analysis_of_district(qry_str)
        poutput = {'district': district, 'hpp_analysis': hpp_analysis}
        print(poutput)

print("#########test area service ptype:1##########")
qry_str='SO14 0BH'
qry_str = qry_str.upper()
ret = re.findall(r'[A-Z]{1,2}[0-9][A-Z0-9]? [0-9][A-Z]{1,2}', qry_str)
print(ret)
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
        print(poutput)