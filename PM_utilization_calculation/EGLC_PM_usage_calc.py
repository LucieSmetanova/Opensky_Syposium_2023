import numpy as np
import pandas as pd
from shapely.geometry import Point
from shapely.geometry.polygon import Polygon
import time
import os
start_time = time.time()

year = '2022'
airport_icao = "EGLC"
month = '06'
radius = 0.05

DATASET_DATA_DIR = os.path.join('..', "Outputs")
filename = "PM_dataset_v3.csv"
flights1 = pd.read_csv(os.path.join(DATASET_DATA_DIR, filename), sep=' ',
    names = ['flightID', 'sequence', 'timestamp', 'lat', 'lon', 'rawAltitude', 'altitude', 'velocity', 'beginDate', 'endDate'],
    dtype={'flightID':str, 'sequence':int, 'timestamp':int, 'lat':float, 'lon':float, 'rawAltitude':float, 'altitude':float, 'velocity':float, 'beginDate':str, 'endDate':str})


err = ['220623SWR46N']
flights1 = flights1[~flights1['flightID'].isin(err)]

print('data error extracted')
flights1.set_index(['flightID'], inplace=True)

print('points done')
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
LCE11_lat, LCE11_lon = dms2dd('512504.57N 0011834.81E')
LCE11_circle_center = Point(LCE11_lon, LCE11_lat)
LCE12_lat, LCE12_lon = dms2dd('512958.17N 0011906.68E')
LCE12_circle_center = Point(LCE12_lon, LCE12_lat)
LCE13_lat, LCE13_lon = dms2dd('513442.46N 0011704.79E')
LCE13_circle_center = Point(LCE13_lon, LCE13_lat)
RAVSA_lat, RAVSA_lon = dms2dd('512829.01N 0005513.72E')
RAVSA_circle_center = Point(RAVSA_lon, RAVSA_lat)
GAPGI_lat, GAPGI_lon = dms2dd('512844.89N 0004820.99E')
GAPGI_circle_center = Point(GAPGI_lon, GAPGI_lat)
JACKO_lat, JACKO_lon = dms2dd('514408.65N 0012536.00E')
JACKO_circle_center = Point(JACKO_lon, JACKO_lat)
LCE21_lat, LCE21_lon = dms2dd('513006.82N 0012130.07E')
LCE21_circle_center = Point(LCE21_lon, LCE21_lat)
LCE22_lat, LCE22_lon = dms2dd('512443.87N 0012054.73E')
LCE22_circle_center = Point(LCE22_lon, LCE22_lat)
LCE23_lat, LCE23_lon = dms2dd('511945.28N 0011734.94E')
LCE23_circle_center = Point(LCE23_lon, LCE23_lat)

N = [BABKU_circle_center,LCE21_circle_center,LCE22_circle_center,LCE23_circle_center]
S = [ELMIV_circle_center,LCE11_circle_center,LCE12_circle_center,LCE13_circle_center]

Nn = ['BABKU','LCE21','LCE22','LCE23']
Sn = ['ELMIV','LCE11','LCE12','LCE13']

thres = 51.30
count = 0
number_of_flights = len(flights1.groupby(level='flightID'))

def check_circle_contains_point(circle_center, circle_radius, point): 
   
    if point.distance(circle_center) <= circle_radius:
        return True
    else:
        return False
    
PM_usage = pd.DataFrame(columns=['flightID','last_star'])

for flight_id, flight_df in flights1.groupby(level='flightID'):
    flight_df = flight_df.reset_index()
    flight_df['sequence'] = range(0,len(flight_df)) 
    flight_df = flight_df.set_index(['flightID','sequence'])
    zero_lat = flight_df['lat'][0]
    flight_df = flight_df.sort_values(by='sequence', ascending=False)
    flight_df['seq_desc'] = range(0,len(flight_df))
    flight_df = flight_df.sort_values(by='sequence', ascending=True)
    flight_df = flight_df.reset_index()
    flight_df = flight_df.set_index(['flightID', 'seq_desc'])
    count = count + 1
    print(number_of_flights, count)
    step = 0
    for seq, row in flight_df.groupby(level='seq_desc'):
        lat = row.loc[(flight_id, seq)]['lat']
        lon = row.loc[(flight_id, seq)]['lon']
        if zero_lat > thres:
            points = N
            names = Nn
        else:
            points = S
            names = Sn
        if (check_circle_contains_point(points[3], radius, Point(lon, lat))):
            PM_usage.loc[len(PM_usage)] = [flight_id,names[3]]
            print('in '+names[3])
            break
        elif (check_circle_contains_point(points[2], radius, Point(lon, lat))):
            PM_usage.loc[len(PM_usage)] = [flight_id,names[2]]
            print('in '+names[2])
            break
        elif (check_circle_contains_point(points[1], radius, Point(lon, lat))):
            PM_usage.loc[len(PM_usage)] = [flight_id,names[1]]
            print('in '+names[1])
            break
        elif (check_circle_contains_point(points[0], radius, Point(lon, lat))):
            PM_usage.loc[len(PM_usage)] = [flight_id,names[0]]
            print('went up to '+names[0])
            break
        else:
            print('in none of them')
            continue

if radius == 0.05:
    filename = airport_icao+"_ARCS.csv"
elif radius == 0.03:
    filename = airport_icao+"_ARCS_rad03.csv"
PM_usage.to_csv(os.path.join(DATASET_DATA_DIR, filename), sep=' ', encoding='utf-8', float_format='%.3f', index = True, header = False)

