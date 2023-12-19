import pandas as pd
from shapely.geometry import Point
import os
import time
start_time = time.time()

year = '2022'
airport_icao = "EGLC"
month = '06'
dat = ''

for week in ['1','2','3','4']:
    DATASET_DATA = DATASET_DATA_DIR
    
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
        seconds = float(as_string[4:9])
        lat_dd = float(degrees) + float(minutes)/60 + float(seconds)/(60*60)
        degrees = int(as_string[10:14])
        minutes = int(as_string[14:16])
        seconds = float(as_string[16:21])
        lon_dd = float(degrees) + float(minutes)/60 + float(seconds)/(60*60)
    
        return lat_dd, lon_dd
    
    BABKU_lat, BABKU_lon = dms2dd("513519.59N 0011916.23E")
    BABKU_circle_center = Point(BABKU_lon, BABKU_lat)
    
    NONVA_lat, NONVA_lon = dms2dd("513846.45N 0012144.31E")
    NONVA_circle_center = Point(NONVA_lon, NONVA_lat)
    
    ELMIV_lat, ELMIV_lon = dms2dd("512033.08N 0011533.36E")
    ELMIV_circle_center = Point(ELMIV_lon, ELMIV_lat)
    
    GODLU_lat, GODLU_lon = dms2dd("510958.44N 0011704.26E")
    GODLU_circle_center = Point(GODLU_lon, GODLU_lat)
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
            if (check_circle_contains_point(NONVA_circle_center, radius, Point(lon, lat))):
                step = 1
            if (check_circle_contains_point(BABKU_circle_center, radius, Point(lon, lat))):
                if step == 1:
                    drop = False
                    #print(seq)
                    break
                elif step == 0:
                    drop = True
                    break      

            if (check_circle_contains_point(GODLU_circle_center, radius, Point(lon, lat))):
                step = 1
            if (check_circle_contains_point(ELMIV_circle_center, radius, Point(lon, lat))):
                if step == 1:
                    drop = False
                    #print(seq)
                    break
                elif step == 0:
                    drop = True
                    break      
        if drop:  
            states_df = states_df.drop(flight_id)
        
    filename = "PM_dataset_"+dat+"_week"+week+".csv"
    states_df.to_csv(os.path.join(DATASET_DATA_DIR, filename), sep=' ', encoding='utf-8', float_format='%.3f', index = True, header = False)