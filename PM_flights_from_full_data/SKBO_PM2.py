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
dat = 'NW2'

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
        
        IRUPU_lat, IRUPU_lon = dms2dd("044607.05N 0744723.02W")
        IRUPU_circle_center = Point(IRUPU_lon, IRUPU_lat)
        
        GERBA_lat, GERBA_lon = dms2dd("042611.64N 0745000.76W")
        GERBA_circle_center = Point(GERBA_lon, GERBA_lat)
        
        BO862_lat, BO862_lon = dms2dd("043623.25N 0750454.62W")
        BO862_circle_center = Point(BO862_lon, BO862_lat)
        
        BO886_lat, BO886_lon = dms2dd("045016.82N 0750659.00W")
        BO886_circle_center = Point(BO886_lon, BO886_lat)
        
        MQU_lat, MQU_lon = dms2dd("051218.00N 0745516.00W")
        MQU_circle_center = Point(MQU_lon, MQU_lat)
        
        NOR02_lat, NOR02_lon = dms2dd("050649.75N 0744545.88W")
        NOR02_circle_center = Point(NOR02_lon, NOR02_lat)
        
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
                # if (check_circle_contains_point(GERBA_circle_center, radius, Point(lon, lat))):
                #     step = 1
                # if (check_circle_contains_point(BO862_circle_center, radius, Point(lon, lat))):
                #     step = 1
                # if (check_circle_contains_point(BO886_circle_center, radius, Point(lon, lat))):
                #     step = 1
                if (check_circle_contains_point(IRUPU_circle_center, radius, Point(lon, lat))):
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
                # if (check_circle_contains_point(MQU_circle_center, radius, Point(lon, lat))):
                #     step = 1
                if (check_circle_contains_point(NOR02_circle_center, radius, Point(lon, lat))):
                    # if step == 1:
                    #     drop = False
                    #     #print(seq)
                    #     break
                    # elif step == 0:
                    #     drop = True
                    #     break      
                    drop = False
                    #print(seq)
                    break

            if drop:  
                states_df = states_df.drop(flight_id)
            
        filename = airport_icao+"_PM_dataset_PM_"+dat+"_week"+week+rwy+"_v2.csv"
        states_df.to_csv(os.path.join(DATASET_DATA_DIR, filename), sep=' ', encoding='utf-8', float_format='%.3f', index = True, header = False)
