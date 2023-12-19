import numpy as np
import pandas as pd
from shapely.geometry import Point
from shapely.geometry.polygon import Polygon

import os

import time
start_time = time.time()

year = '2022'
airport_icao = "ENGM"
month = '10'

#airport_icao = "ENGM"
TMA_lon=[9.59556, 11.7944, 11.8494, 12.0989, 12.3611, 12.3394, 12.3417, 12.2917, 11.8292, 11.6958, 11.0722, 10.95, 10.5583, 10.1, 9.59556];

TMA_lat=[59.7097, 59.3667, 59.8333, 59.8906, 60.2236, 60.4039, 60.5, 60.7125, 60.875, 60.7972, 60.8778, 60.9389, 60.925, 60.7292, 59.7097];

# Runway 01L
rwy01L_lat=[60.185, 60.216067];
rwy01L_lon=[11.073744, 11.091664];
# Runway 19R
rwy19R_lat=[60.216067, 60.185];
rwy19R_lon=[11.091664, 11.073744];
# Runway 01R
rwy01R_lat = [60.175756, 60.201208];
rwy01R_lon = [11.107783, 11.122486];
# Runway 19L
rwy19L_lat = [60.201208, 60.175756];
rwy19L_lon = [11.122486, 11.107783];

states_df = pd.DataFrame()

for week in [1,2,3,4]:
    for rwy in ['_rwy19L','_rwy19R']:
        #specify path to your downloaded 
        filename = 'YOUR FILE NAME'
        DATASET_DATA_DIR(os.path.join('YOUR PATH', filename))
        # add path to runway determined files

        filename = "osn_"+ airport_icao + "_states_50NM_" + year + "_" + month + "_week" + str(week) + "_by_runways"
        DATASET_DATA_DIR_rwy = os.path.join(DATASET_DATA_DIR, filename)
        filename = "osn_"+ airport_icao + "_states_50NM_" + year + '_' + month + "_week" + str(week) + rwy +".csv"
        states_df_1 = pd.read_csv(os.path.join(DATASET_DATA_DIR_rwy, filename), sep=' ',
            names = ['flightId', 'sequence', 'timestamp', 'lat', 'lon', 'rawAltitude', 'altitude', 'velocity', 'beginDate', 'endDate'],
            dtype={'flightId':str, 'sequence':int, 'timestamp':int, 'lat':float, 'lon':float, 'rawAltitude':float, 'altitude':float, 'velocity':float, 'beginDate':str, 'endDate':str})
    
        states_df = states_df.append(states_df_1)
        
# states_df['lat_min'] = states_df.groupby(['flightId'])['lat'].transform('min')
# states_df['lat_max'] = states_df.groupby(['flightId'])['lat'].transform('max')
# states_df['lon_min'] = states_df.groupby(['flightId'])['lon'].transform('min')
# states_df['lon_max'] = states_df.groupby(['flightId'])['lon'].transform('max')

# states_df = states_df.loc[(states_df['lat_min'] > 60.25)]
# states_df = states_df.loc[(states_df['lon_min'] > 11)]
    
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

GM423_lat, GM423_lon = (60.36525,12.03375)
GM423_circle_center = Point(GM423_lon, GM423_lat)

GM418_lat, GM418_lon = (60.651194,11.7955)
GM418_circle_center = Point(GM418_lon, GM418_lat)

# KOGAX_lat, KOGAX_lon = dms2dd("533418.6N 0053814.1E")
# KOGAX_circle_center = Point(KOGAX_lon, KOGAX_lat)

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
    step = 0
    for seq, row in flight_df.groupby(level='sequence'):
        lat = row.loc[(flight_id, seq)]['lat']
        lon = row.loc[(flight_id, seq)]['lon']
        if (check_circle_contains_point(GM423_circle_center, radius, Point(lon, lat))):
            drop = False
        elif (check_circle_contains_point(GM418_circle_center, radius, Point(lon, lat))):
            drop = False
        #if (check_circle_contains_point(LUTIV_circle_center, radius, Point(lon, lat))):
            #drop = False
            #break       
    if drop:  
        states_df = states_df.drop(flight_id)
    
filename = "PM_dataset_arrival_50NM_GM418_rwy19_NEW.csv"
states_df.to_csv(os.path.join(DATASET_DATA_DIR, filename), sep=' ', encoding='utf-8', float_format='%.3f', index = True, header = False)
