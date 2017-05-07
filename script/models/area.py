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
        areas = []
        for region, area in db_session.query(Region, Area).filter(
                and_(Region.RegionName == Area.RegionName, Region.RegionAbbr == region_addr)).all():
            areas.append(area)
        return areas

    @staticmethod
    def get_area_by_code(area_code):
        # get a area according to a area code
        # area_code: area code, eg 'SO'
        # return: a object
        return Area.query.filter_by(PostcodeAreaCode=area_code).first()

    @staticmethod
    def get_all_areas():
        # get all area information
        # return: object list
        return Area.query.all()


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
        return District.query.filter_by(PostcodeDistrict=district).first()

    @staticmethod
    def get_districts_under_area(area_code):
        return District.query.filter_by(PostcodeAreaCode=area_code).all()

    @staticmethod
    def get_all_districts():
        return District.query.all()

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
        return db_session.query(District).filter(
            and_(District.City.ilike('%' + city_name + '%'),
                 District.ActivePostcodes > 0,
                 District.Population > 0,
                 District.Households > 0)).all()
