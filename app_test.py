from script.models.area import Region, Area, District
from script.models import database
from flask import jsonify
import re
import requests
import json

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
city_name = 'South'
print(District.get_all_districts_under_city(city_name))

# area case 011
print("##########test get_all_cities_under_region(region_abbr)")
region_abbr = 'NE'
print(District.get_all_cities_under_region(region_abbr))

# rest case 012
print("##########test api.hpp_search")


from script.services.area import location_search
print(location_search('bournemouth'))