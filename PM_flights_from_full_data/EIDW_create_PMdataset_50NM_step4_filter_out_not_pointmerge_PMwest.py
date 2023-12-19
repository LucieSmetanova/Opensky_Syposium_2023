import numpy as np
import pandas as pd
from shapely.geometry import Point
from shapely.geometry.polygon import Polygon

import os

import time
start_time = time.time()

year = '2022'
airport_icao = "EIDW"
month = '07'

from constants_EIDW import *

DATA_DIR = os.path.join('Data', airport_icao)
DATA_DIR = os.path.join(DATA_DIR, year)
DATASET_DATA_DIR = os.path.join(DATA_DIR, "osn_"+airport_icao+"_states_50NM_"+year+"_filtered_by_altitude")
for week in ['3','4']:
    
    states_df = pd.DataFrame()
    
    #specify path to your downloaded 
    filename = 'YOUR FILE NAME'
    DATASET_DATA_DIR(os.path.join('YOUR PATH', filename))
    states_df = pd.read_csv(DATASET_DATA_DIR, sep=' ',
        names = ['flightId', 'sequence', 'timestamp', 'lat', 'lon', 'rawAltitude', 'altitude', 'velocity', 'beginDate', 'endDate'],
        dtype={'flightId':str, 'sequence':int, 'timestamp':int, 'lat':float, 'lon':float, 'rawAltitude':float, 'altitude':float, 'velocity':float, 'beginDate':str, 'endDate':str})
    states_df.set_index(['flightId', 'sequence'], inplace=True)
    
    number_of_flights = len(states_df.groupby(level='flightId'))
    count = 0
    
    # no sign for lat because of 'N'
    # '-' sign for lon because of 'W'
    def dms2dd(as_string):
        degrees = int(as_string[:2])
        minutes = int(as_string[2:4])
        seconds = float(as_string[4:8])
        lat_dd = float(degrees) + float(minutes)/60 + float(seconds)/(60*60)
        degrees = -1*int(as_string[10:13])
        minutes = -1*int(as_string[13:15])
        seconds = -1*float(as_string[15:19])
        lon_dd = float(degrees) + float(minutes)/60 + float(seconds)/(60*60)
    
        return lat_dd, lon_dd
    
    ASDER_lat, ASDER_lon = dms2dd("533346.7N 0062226.4W")
    ASDER_circle_center = Point(ASDER_lon, ASDER_lat)
    
    BERMO_lat, BERMO_lon = dms2dd("531738.9N 0062450.8E")
    BERMO_circle_center = Point(BERMO_lon, BERMO_lat)
    ADNAL_lat, ADNAL_lon = dms2dd("534153.9N 0063541.5E")
    ADNAL_circle_center = Point(ADNAL_lon, ADNAL_lat)
    BABON_lat, BABON_lon = dms2dd("531303.3N 0063056.5E")
    BABON_circle_center = Point(BABON_lon, BABON_lat)
    radius = 0.05
    
    def check_circle_contains_point(circle_center, circle_radius, point): 
       
        if point.distance(circle_center) <= circle_radius:
            return True
        else:
            return False
    
    for flight_id, flight_df in states_df.groupby(level='flightId'):
        
        count = count + 1
        print(number_of_flights, count)
        
        drop = True
        
        for seq, row in flight_df.groupby(level='sequence'):
            lat = row.loc[(flight_id, seq)]['lat']
            lon = row.loc[(flight_id, seq)]['lon']
            if (check_circle_contains_point(ASDER_circle_center, radius, Point(lon, lat))):
                drop = False
                break
            if (check_circle_contains_point(BABON_circle_center, radius, Point(lon, lat))):
                drop = False
                break
            if (check_circle_contains_point(ADNAL_circle_center, radius, Point(lon, lat))):
                drop = False
                break
            if (check_circle_contains_point(BERMO_circle_center, radius, Point(lon, lat))):
                drop = False
                break       
        if drop:  
            states_df = states_df.drop(flight_id)
        
    filename = "PM_WEST_dataset_week"+week+"_v2.csv"
    states_df.to_csv(os.path.join(DATASET_DATA_DIR, filename), sep=' ', encoding='utf-8', float_format='%.3f', index = True, header = False)