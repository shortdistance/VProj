# -*-coding:utf-8 -*-
import os, csv
from script.models import database
from script.models.area import Region, Area, District
from script.models.hpp import DistrictYearHpp, DistrictYearMonthHpp
from script.models.iphrp import IphrpIndexValue, IphrpAnnualChange

DATA_FOLDER = '/Users/leizhang/Workspace/opendata_coursework2/data'
REGION_FILE = os.path.join(DATA_FOLDER, '00.region_code_name.csv')
AREA_FILE = os.path.join(DATA_FOLDER, '01.postcode_area_region.csv')
DISTRICT_FILE = os.path.join(DATA_FOLDER, '02.Postcode_districts.csv')
DISTRICT_YEAR_HPP_FILE = os.path.join(DATA_FOLDER, '03.postcode_districts_year_hpp.csv')
DISTRICT_YEAR_MONTH_HPP_FILE = os.path.join(DATA_FOLDER, '04.postcode_districts_year_month_hpp.csv')
IPHRP_INDEX_VALUE_FILE = os.path.join(DATA_FOLDER, '05.regions_year_month_iphrp(index_values).csv')
IPHRP_ANNUAL_CHANGE_FILE = os.path.join(DATA_FOLDER, '06.regions_year_month_iphrp(annual_change).csv')


def dropDB():
    database.drop_database()
    print('drop all the db tables.')


def createDB():
    database.create_database()
    print('create all the db tables.')


# | ----------------------------------------|
# | Region_code | Region_name | Region_abbr |
# | ----------------------------------------|
# | E12000001	| North East  | NE          |
# | ----------------------------------------|
def import_region(region_file):
    with open(region_file) as fp:
        for line in fp:
            line.replace('"', '')  # delete quotation in the line
            line = line.strip()  # delete all line break
            a = line.split(',')
            b = Region(a[0], a[1], a[2])


# |------------------------------------------|
# |Postcode_Area | Area_Name | Region        |
# |------------------------------------------|
# |      DE	     |  Derby	 | East Midlands |
# |------------------------------------------|
# |      LE	     | Leicester | East Midlands |
# |------------------------------------------|
# |      LN	     |  Lincoln	 | East Midlands |
# |------------------------------------------|
def import_area(area_file):
    lines = open(area_file).readlines()
    for line in lines:
        line.replace('"', '')
        line = line.strip()
        a = line.split(',')
        b = Area(a[0], a[1], a[2])


# Postcode district info
# ---------------------------
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

def import_district(district_file):
    lines = open(district_file).readlines()
    for line in lines:
        line.replace('"', '')
        line = line.strip()
        a = line.split(',')
        b = District(a[0], a[1], a[2],
                     a[3], a[4], a[5],
                     a[6], a[7], a[8],
                     a[9])


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
def import_district_year_hpp(district_year_hpp_file):
    lines = open(district_year_hpp_file).readlines()
    for line in lines:
        line.replace('"', '')
        line = line.strip()
        a = line.split(',')
        b = DistrictYearHpp(a[0], a[1], a[2],
                            a[3], a[4], a[5],
                            a[6], a[7], a[8],
                            a[9], a[10])


def import_district_year_month_hpp(district_year_month_hpp_file):
    with open(district_year_month_hpp_file) as fp:
        for line in fp:
            line.replace('"', '')
            line = line.strip()
            a = line.split(',')
            b = DistrictYearMonthHpp(a[0], a[1], a[2],
                                     a[3], a[4], a[5],
                                     a[6], a[7], a[8],
                                     a[9], a[10])


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
def import_iphrp_index_value(iphrp_index_value_file):
    with open(iphrp_index_value_file) as fp:
        for line in fp:
            line.replace('"', '')
            line = line.strip()
            a = line.split(',')
            b = IphrpIndexValue(a[0], a[1], a[2],
                                a[3], a[4], a[5],
                                a[6], a[7], a[8],
                                a[9], a[10], a[11],
                                a[12], a[13], a[14])


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

def import_iphrp_annual_change(iphrp_annual_change_file):
    with open(iphrp_annual_change_file) as fp:
        for line in fp:
            line.replace('"', '')
            line = line.strip()
            a = line.split(',')
            b = IphrpAnnualChange(a[0], a[1], a[2],
                                  a[3], a[4], a[5],
                                  a[6], a[7], a[8],
                                  a[9], a[10], a[11],
                                  a[12], a[13], a[14])


if __name__ == '__main__':
    #dropDB()
    createDB()
    #import_region(REGION_FILE)
    #import_area(AREA_FILE)
    import_district(DISTRICT_FILE)
    #import_district_year_hpp(DISTRICT_YEAR_HPP_FILE)
    #import_district_year_month_hpp(DISTRICT_YEAR_MONTH_HPP_FILE)
    #import_iphrp_index_value(IPHRP_INDEX_VALUE_FILE)
    #import_iphrp_annual_change(IPHRP_ANNUAL_CHANGE_FILE)
