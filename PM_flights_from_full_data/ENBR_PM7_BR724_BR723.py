import numpy as np
import pandas as pd
from shapely.geometry import Point
from shapely.geometry.polygon import Polygon

import os

import time
start_time = time.time()

year = '2022'
airport_icao = "ENBR"
month = '10'

#airport_icao = "ENBR"
TMA_lon=[4.5, 5.4833, 5.5389, 5.7081, 6.0036, 6.0578, 6.25, 6.2067, 5.8333, 5.5319, 5.1592, 4.4992, 4.3978, 4.3333, 4.4622, 4.5];
TMA_lat=[61.0, 61.0, 60.9775, 60.9075, 60.7161, 60.5503, 59.95, 59.6853, 59.6681, 59.6536, 59.6378, 59.6064, 60.0025, 60.25, 60.8333, 61.0];
# Runway 17
rwy17_lat=[60.304233, 60.281597];
rwy17_lon=[5.214486, 5.222092];
# Runway 35
rwy35_lat=[60.282544, 60.304897];
rwy35_lon=[5.221775, 5.214267];


states_df = pd.DataFrame()

for week in [1,2,3,4]:
    #specify path to your downloaded 
    filename = 'YOUR FILE NAME'
    DATASET_DATA_DIR(os.path.join('YOUR PATH', filename))
    states_df_1 = pd.read_csv(DATASET_DATA_DIR, sep=' ',
        names = ['flightId', 'sequence', 'timestamp', 'lat', 'lon', 'rawAltitude', 'altitude', 'velocity', 'beginDate', 'endDate'],
        dtype={'flightId':str, 'sequence':int, 'timestamp':int, 'lat':float, 'lon':float, 'rawAltitude':float, 'altitude':float, 'velocity':float, 'beginDate':str, 'endDate':str})

    states_df = states_df.append(states_df_1)
    
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

BR724_lat, BR724_lon = (60.104197,4.830814)
BR724_circle_center = Point(BR724_lon, BR724_lat)

BR723_lat, BR723_lon = (60.046469,4.830317)
BR723_circle_center = Point(BR723_lon, BR723_lat)

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
        if (check_circle_contains_point(BR724_circle_center, radius, Point(lon, lat))):
            #step = 1
	    drop = False
	    break
        #if (check_circle_contains_point(BR723_circle_center, radius, Point(lon, lat))):
            #if step == 1:
                #drop = False
                #print(seq)
                #break
            #elif step == 0:
                #drop = True
                #break
        #if (check_circle_contains_point(LUTIV_circle_center, radius, Point(lon, lat))):
            #drop = False
            #break       
    if drop:  
        states_df = states_df.drop(flight_id)
    
filename = "PM_dataset_arrival_50NM_BR724_BR723.csv"
states_df.to_csv(os.path.join(DATASET_DATA_DIR, filename), sep=' ', encoding='utf-8', float_format='%.3f', index = True, header = False)