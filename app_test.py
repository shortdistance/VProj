from script.models.area import Region,Area,District
from script.models import database

#area case 001
print("##########test Region.get_all_regions()")
print(len(Region.get_all_regions()))

#area case 002
print("##########test Region.get_region(region_abbr)")
region_abbr = 'NE'
print(Region.get_region(region_abbr).RegionName)

#area case 003
print("##########test Area.get_areas_under_region(region_addr)")
region_addr = 'L'
print(Area.get_areas_under_region(region_addr))

#api case 004
print("##########test Area.get_areas_under_region(region_addr)")
areas = []
ret_area = {}
for area in Area.get_areas_under_region(region_abbr):
    ret_area['PostcodeAreaCode'] = area.PostcodeAreaCode
    ret_area['PostcodeAreaName'] = area.PostcodeAreaName
    ret_area['RegionAbbr'] = region_abbr
    ret_area['RegionName'] = area.RegionName
    areas.append(ret_area)
print (areas)

#area case 005
print("##########test Area.get_area_by_code(area_code)")
area_code = 'SO'
print(Area.get_area_by_code(area_code).PostcodeAreaName)

#area case 006
print("##########test Area.get_all_areas()")
print(Area.get_all_areas())

#area case 007
print("##########test District.get_district(district)")
district = 'SO14'
print(District.get_district(district).City)

#area case 008
print("##########test get_districts_under_area(area)")
area_code  = 'SO'
print(District.get_districts_under_area(area_code))

#area case 009
print("##########test get_all_districts()")
print(District.get_all_districts())

#area case 010
print("##########test get_all_districts_under_city(city_name)")
city_name = 'South'
print(District.get_all_districts_under_city(city_name))

#area case 011
print("##########test get_all_cities_under_region(region_abbr)")
region_abbr = 'NE'
print(len(District.get_all_cities_under_region(region_abbr)))
