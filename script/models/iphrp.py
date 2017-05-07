from sqlalchemy import Column, Integer, String, Float
from script.models.database import BaseModel, db_session


class IphrpIndexValue(BaseModel):
    # Datetime,201101
    # England,100
    # Wales,100
    # Scotland,100
    # North East,100
    # North West,100
    # Yorkshire and The Humber,100
    # East Midlands,100
    # West Midlands,100
    # East,100
    # London,100
    # South East,100
    # South West,100
    # GB excluding London,100
    # England excluding London,100
    __tablename__ = 'IphrpIndexValue'
    Id = Column(Integer, primary_key=True, autoincrement=True)
    Datetime = Column(String(64))
    E = Column(Float)
    W = Column(Float)
    S = Column(Float)
    NE = Column(Float)
    NW = Column(Float)
    YtH = Column(Float)
    EM = Column(Float)
    WM = Column(Float)
    East = Column(Float)
    L = Column(Float)
    SE = Column(Float)
    SW = Column(Float)
    GBeL = Column(Float)  # GB excluding London
    EeL = Column(Float)  # England excluding London

    def __init__(self, dt, e, w, s, ne, nw, yth, em, wm, east, l, se, sw, gbel, eel):
        self.Datetime = dt
        self.E = e
        self.W = w
        self.S = s
        self.NE = ne
        self.NW = nw
        self.YtH = yth
        self.EM = em
        self.WM = wm
        self.East = east
        self.L = l
        self.SE = se
        self.SW = sw
        self.GBeL = gbel
        self.EeL = eel

        db_session.add(self)
        db_session.commit()

    @staticmethod
    def get_iphrp():
        return IphrpIndexValue.query.all()


class IphrpAnnualChange(BaseModel):
    # Datetime,201201
    # England,2.8
    # Wales,1.3
    # Scotland,1.4
    # North East,1.4
    # North West,1.1
    # Yorkshire and The Humber,0.8
    # East Midlands,1.6
    # West Midlands,1.3
    # East,1.7
    # London,4.9
    # South East,2.4
    # South West,1.9
    # GB excluding London,1.7
    # England excluding London,1.7
    __tablename__ = 'IphrpAnnualChange'
    Id = Column(Integer, primary_key=True, autoincrement=True)
    Datetime = Column(String(64))
    E = Column(Float)
    W = Column(Float)
    S = Column(Float)
    NE = Column(Float)
    NW = Column(Float)
    YtH = Column(Float)
    EM = Column(Float)
    WM = Column(Float)
    East = Column(Float)
    L = Column(Float)
    SE = Column(Float)
    SW = Column(Float)
    GBeL = Column(Float)  # GB excluding London
    EeL = Column(Float)  # England excluding London

    def __init__(self, dt, e, w, s, ne, nw, yth, em, wm, east, l, se, sw, gbel, eel):
        self.Datetime = dt
        self.E = e
        self.W = w
        self.S = s
        self.NE = ne
        self.NW = nw
        self.YtH = yth
        self.EM = em
        self.WM = wm
        self.East = east
        self.L = l
        self.SE = se
        self.SW = sw
        self.GBeL = gbel
        self.EeL = eel

        db_session.add(self)
        db_session.commit()

    @staticmethod
    def get_iphrp():
        return IphrpAnnualChange.query.all()