import numpy as np
import pandas as pd
from shapely.geometry import Point
from shapely.geometry.polygon import Polygon

import os

import time
start_time = time.time()

year = '2022'
airport_icao = "SKBO"
month = '12'
dat = 'NW'

for week in ['1','2','3','4']:
    for rwy in ['_rwy13L','_rwy13R','_rwy31L','_rwy31R']:
        #specify path to your downloaded 
        filename = 'YOUR FILE NAME'
        DATASET_DATA_DIR(os.path.join('YOUR PATH', filename))
        # add path to runway determined files

        DATASET_DATA = os.path.join(DATASET_DATA_DIR, "osn_"+airport_icao+"_states_50NM_extracted_"+year+"_"+month+"_week"+week+"_by_runways")
        
        states_df = pd.DataFrame()
        
        filename = "osn_"+airport_icao+"_states_50NM_"+year+"_"+month+"_week"+week+rwy+".csv"
        states_df = pd.read_csv(os.path.join(DATASET_DATA, filename), sep=' ',
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
            degrees = -1*int(as_string[10:14])
            minutes = -1*int(as_string[14:16])
            seconds = -1*float(as_string[16:21])
            lon_dd = float(degrees) + float(minutes)/60 + float(seconds)/(60*60)
        
            return lat_dd, lon_dd
        
        PAPET_lat, PAPET_lon = dms2dd("051359.10N 0741904.78W")
        PAPET_circle_center = Point(PAPET_lon, PAPET_lat)
        
        BO804_lat, BO804_lon = dms2dd("052506.00N 0740630.00W")
        BO804_circle_center = Point(BO804_lon, BO804_lat)
        
        BO824_lat, BO824_lon = dms2dd("052019.62N 0740034.24W")
        BO824_circle_center = Point(BO824_lon, BO824_lat)
        
        BO832_lat, BO832_lon = dms2dd("050702.01N 0735743.14W")
        BO832_circle_center = Point(BO832_lon, BO832_lat)
        
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
                # if (check_circle_contains_point(BO804_circle_center, radius, Point(lon, lat))):
                #     step = 1
                # if (check_circle_contains_point(BO824_circle_center, radius, Point(lon, lat))):
                #     step = 1
                # if (check_circle_contains_point(BO832_circle_center, radius, Point(lon, lat))):
                #     step = 1
                if (check_circle_contains_point(PAPET_circle_center, radius, Point(lon, lat))):
                    drop = False
                    #print(seq)
                    break

                    # if step == 1:
                    #     drop = False
                    #     #print(seq)
                    #     break
                    # elif step == 0:
                    #     drop = True
                    #     break      
            if drop:  
                states_df = states_df.drop(flight_id)
            
        filename = airport_icao+"_PM_dataset_PM_"+dat+"_week"+week+rwy+"_v2.csv"
        states_df.to_csv(os.path.join(DATASET_DATA_DIR, filename), sep=' ', encoding='utf-8', float_format='%.3f', index = True, header = False)
