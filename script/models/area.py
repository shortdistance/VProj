from sqlalchemy import Column, Integer, String, Float, and_, func, distinct
from script.models.database import BaseModel, db_session


class Region(BaseModel):
    # Post Code Region info
    # | ----------------------------------------|
    # | Region_code | Region_name | Region_abbr |
    # | ----------------------------------------|
    # | E12000001	| North East  | NE          |
    # | ----------------------------------------|
    __tablename__ = 'Region'
    RegionCode = Column(String(64), primary_key=True)
    RegionName = Column(String(64))
    RegionAbbr = Column(String(64))

    def __init__(self, region_code, region_name, region_abbr):
        self.RegionCode = region_code
        self.RegionName = region_name
        self.RegionAbbr = region_abbr
        db_session.add(self)
        db_session.commit()

    @staticmethod
    def get_region(region_abbr):
        return Region.query.filter_by(RegionAbbr=region_abbr).first()

    @staticmethod
    def get_all_regions():
        return Region.query.all()


class Area(BaseModel):
    # Post code area info
    # |------------------------------------------|
    # |Postcode_Area | Area_Name | Region        |
    # |------------------------------------------|
    # |      DE	     |  Derby	 | East Midlands |
    # |------------------------------------------|
    # |      LE	     | Leicester | East Midlands |
    # |------------------------------------------|
    # |      LN	     |  Lincoln	 | East Midlands |
    # |------------------------------------------|
    __tablename__ = 'Area'
    Id = Column(Integer, primary_key=True, autoincrement=True)
    PostcodeAreaCode = Column(String(64))
    PostcodeAreaName = Column(String(64))
    RegionName = Column(String(64))

    def __init__(self, area_code, area_name, region_name):
        self.PostcodeAreaCode = area_code
        self.PostcodeAreaName = area_name
        self.RegionName = region_name
        db_session.add(self)
        db_session.commit()

    @staticmethod
    def get_areas_under_region(region_addr):
        # get all the areas of a region according to a region abbrevation.
        # region_abbr: eg:'NE','L','E'
        # return: list
        area_list = []
        for region, area in db_session.query(Region, Area).filter(
                and_(Region.RegionName == Area.RegionName, Region.RegionAbbr == region_addr)).all():
            area_list.append(Area.area_to_json(area))
        return area_list

    @staticmethod
    def get_area_by_code(area_code):
        # get a area according to a area code
        # area_code: area code, eg 'SO'
        # return: a object
        area = Area.query.filter_by(PostcodeAreaCode=area_code).first()
        return Area.area_to_json(area)

    @staticmethod
    def get_all_areas():
        # get all area information
        # return: object list
        area_list = []
        for area in Area.query.all():
            area_list.append(Area.area_to_json(area))
        return area_list

    @staticmethod
    def area_to_json(area):
        ret_json = {}
        if isinstance(area, Area):
            ret_json = {
                'PostcodeAreaCode': area.PostcodeAreaCode,
                'PostcodeAreaName': area.PostcodeAreaName,
                'RegionName': area.RegionName
            }
        return ret_json


class District(BaseModel):
    # Postcode district info
    # -------------------------
    # Postcode_district: "AB10"
    # Postcode_area: "AB"
    # Latitude: 57.1348
    # Longitude: -2.11748
    # City: "Aberdeen"
    # Region: "Scotland"
    # Postcodes: 888
    # Active postcodes: 675
    # Population: 21964
    # Households: 11517
    __tablename__ = 'District'
    Id = Column(Integer, primary_key=True, autoincrement=True)
    PostcodeDistrict = Column(String(64))
    PostcodeAreaCode = Column(String(64))
    Latitude = Column(Float)
    Longitude = Column(Float)
    City = Column(String(255))
    Region = Column(String(64))
    Postcodes = Column(Integer)
    ActivePostcodes = Column(Integer)
    Population = Column(Integer)
    Households = Column(Integer)

    def __init__(self, district, area_code, latitude, longitude, city, region, postcodes, active_postcodes,
                 population, household):
        self.PostcodeDistrict = district
        self.PostcodeAreaCode = area_code
        self.Latitude = latitude
        self.Longitude = longitude
        self.City = city
        self.Region = region
        self.Postcodes = postcodes
        self.ActivePostcodes = active_postcodes
        self.Population = population
        self.Households = household
        db_session.add(self)
        db_session.commit()

    @staticmethod
    def get_district(district):
        district = District.query.filter_by(PostcodeDistrict=district).first()
        return District.distrinct_to_json(district)

    @staticmethod
    def get_districts_under_area(area_code):
        ret_list = []

        for district in District.query.filter_by(PostcodeAreaCode=area_code).all():
            ret_json = District.distrinct_to_json(district)
            if ret_json:
                ret_list.append(ret_json)
        return ret_list

    @staticmethod
    def get_all_districts():
        ret_list = []
        for district in District.query.all():
            ret_json = District.distrinct_to_json(district)
            if ret_json:
                ret_list.append(ret_json)
        return ret_list

    @staticmethod
    def get_all_cities_under_region(region_abbr):
        cities = []
        for region, district in db_session.query(Region, District).filter(
                and_(Region.RegionAbbr == region_abbr, District.Region == Region.RegionName)).all():
            if district.City not in cities:
                cities.append(district.City)
        return cities

    @staticmethod
    def get_all_districts_under_city(city_name):

        city_name = city_name.lower()
        ret_list = []
        for district in db_session.query(District).filter(
                and_(District.Region.ilike('%' + city_name + '%'),
                     District.ActivePostcodes > 0,
                     District.Population > 0,
                     District.Households > 0)).all():
            ret_json = District.distrinct_to_json(district)
            if ret_json:
                ret_list.append(ret_json)
        if not ret_list:
            for district in db_session.query(District).filter(
                    and_(District.City.ilike('%' + city_name + '%'),
                         District.ActivePostcodes > 0,
                         District.Population > 0,
                         District.Households > 0)).all():
                ret_json = District.distrinct_to_json(district)
                if ret_json:
                    ret_list.append(ret_json)
        return ret_list

    @staticmethod
    def distrinct_to_json(district):
        ret_json = {}
        if isinstance(district, District):
            ret_json = {
                'PostcodeDistrict': district.PostcodeDistrict,
                'PostcodeAreaCode': district.PostcodeAreaCode,
                'Latitude': district.Latitude,
                'Longitude': district.Longitude,
                'City': district.City,
                'Region': district.Region,
                'Postcodes': district.Postcodes,
                'ActivePostcodes': district.ActivePostcodes,
                'Population': district.Population,
                'Households': district.Households
            }
        return ret_json
