from sqlalchemy import Column, Integer, String, Float
from script.models.database import BaseModel, db_session


class Hpp(BaseModel):
    # The house paid price records from 2015
    # Price: 231950
    # Datetime: 2015/3/27 0:00
    # Postcode: CF11 9EE
    # PropertyType: S
    # Old: N
    # Duration: F
    # PAON: 43
    # SAON:
    # Street: WYNDHAM CRESCENT
    # Locality:
    # City: CARDIFF
    # District: CARDIFF
    # County: CARDIFF
    __tablename__ = 'Hpp'
    Id = Column(Integer, primary_key=True, autoincrement=True)
    Datetime = Column(String(64))
    Postcode = Column(String(64))
    PropertyType = Column(String(64))
    Old = Column(String(64))
    Duration = Column(String(64))
    PAON = Column(String(64))
    SAON = Column(String(255))
    Street = Column(String(255))
    Locality = Column(String(255))
    City = Column(String(64))
    District = Column(String(64))
    County = Column(String(64))

    def __init__(self, datatime, postcode, property_type, old, duration, paon, saon,
                 street, locality, city, district, county):
        self.Datetime = datatime
        self.Postcode = postcode
        self.PropertyType = property_type
        self.Old = old
        self.Duration = duration
        self.PAON = paon
        self.SAON = saon
        self.Street = street
        self.Locality = locality
        self.City = city
        self.District = district
        self.County = county
        db_session.add(self)
        db_session.commit()

    @staticmethod
    def get_hpp_under_postcode():
        return Hpp.query.filter_by()

class DistrictYearHpp(BaseModel):
    # House paid price data
    # Postcode_district:AL1
    # Year:1996
    # Count: 518
    # Price: 98429.28378
    # D: 61
    # S: 131
    # T: 162
    # F: 164
    # O: 0
    # Y: 48
    # N: 470
    __tablename__ = 'DistrictYearHpp'
    Id = Column(Integer, primary_key=True, autoincrement=True)
    PostcodeDistrict = Column(String(64))
    Year = Column(String(8))
    Count = Column(Integer)
    Price = Column(Float)
    D = Column(Integer)
    S = Column(Integer)
    T = Column(Integer)
    F = Column(Integer)
    O = Column(Integer)
    Y = Column(Integer)
    N = Column(Integer)

    def __init__(self, district, year, count, price, d, s, t, f, o, y, n):
        self.PostcodeDistrict = district
        self.Year = year
        self.Count = count
        self.Price = price
        self.D = d
        self.S = s
        self.T = t
        self.F = f
        self.O = o
        self.Y = y
        self.N = n
        db_session.add(self)
        db_session.commit()

    @staticmethod
    def get_district_hpp(district):
        return DistrictYearHpp.query.filter_by(PostcodeDistrict=district)

    @staticmethod
    def get_district_year_hpp(district, year):
        return DistrictYearHpp.query.filter_by(PostcodeDistrict=district, Year=year)


class DistrictYearMonthHpp(BaseModel):
    # Postcode_district: AL1
    # Year_month: 199601
    # Count: 39
    # Price: 134824.359
    # D: 8
    # S: 14
    # T: 12
    # F: 5
    # O: 0
    # Y: 1
    # N: 3
    __tablename__ = 'DistrictYearMonthHpp'
    Id = Column(Integer, primary_key=True, autoincrement=True)
    PostcodeDistrict = Column(String(64))
    Year_month = Column(String(8))
    Count = Column(Integer)
    Price = Column(Float)
    D = Column(Integer)
    S = Column(Integer)
    T = Column(Integer)
    F = Column(Integer)
    O = Column(Integer)
    Y = Column(Integer)
    N = Column(Integer)

    def __init__(self, district, year_month, count, price, d, s, t, f, o, y, n):
        self.PostcodeDistrict = district
        self.Year_month = year_month
        self.Count = count
        self.Price = price
        self.D = d
        self.S = s
        self.T = t
        self.F = f
        self.O = o
        self.Y = y
        self.N = n
        db_session.add(self)
        db_session.commit()

    @staticmethod
    def get_district_hpp(district):
        return DistrictYearHpp.query.filter_by(PostcodeDistrict=district)

    @staticmethod
    def get_district_yearmonth_hpp(district, ym):
        return DistrictYearMonthHpp.query.filter_by(PostcodeDistrict=district, Year_month=ym)