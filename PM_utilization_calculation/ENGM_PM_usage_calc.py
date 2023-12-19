import numpy as np
import pandas as pd
from shapely.geometry import Point
from shapely.geometry.polygon import Polygon
import time
import os
start_time = time.time()

year = '2022'
airport_icao = "ENGM"
month = '10',
radius = 0.03
# ENGM PM system in ['SE','SW','NE','NW']
PMsystem = 'SW'
if PMsystem == 'NE':
    if radius == 0.05:
        file = 'GM418_rwy19_NEW'
    elif radius == 0.03:
        file = 'GM418_rwy19_rad03'
elif PMsystem == 'NW':
    if radius == 0.05:
        file = 'GM429_GM432_rwy19'
    elif radius == 0.03:
        file = 'GM429_GM432_rwy19_rad03'
elif PMsystem == 'SW':
    if radius == 0.05:
        file = 'GM405_GM410_rwy01'
    elif radius == 0.03:
        file = 'GM405_GM410_rwy01_rad03'
else:
    if radius == 0.05:
        file = 'GM416_GM411_rwy01'
    elif radius == 0.03:
        file = 'GM416_GM411_rwy01_rad03'

filename = "PM_dataset_arrival_50NM_"+file+".csv"
flights1 = pd.read_csv(os.path.join('Output', filename), sep=' ',
    names = ['flightId', 'sequence', 'timestamp', 'lat', 'lon', 'rawAltitude', 'altitude', 'velocity', 'beginDate', 'endDate'],
    dtype={'flightId':str, 'sequence':int, 'timestamp':int, 'lat':float, 'lon':float, 'rawAltitude':float, 'altitude':float, 'velocity':float, 'beginDate':str, 'endDate':str})



list_col_names = ['flightID', 'sequence', 'timestamp', 'lat', 'lon', 'rawAltitude', 'baroAltitude', 'velocity','endDate', 'date']
flights1.columns = list_col_names
flights1 = flights1.drop(['date'], axis=1)
    

for i in ['221001NOZ4ES','221026WIF144','221020SAS64P','221021NOZ1151','221022SAS4433','221023LBD1','221009MDT6',
          '221016SAS4047','221015NOZ8US','221024WIF9BF','221024NOZ11G','221023N900AJ','221013SAS4545','221013NOZ6MH']:
    flights1.drop(flights1[flights1['flightID'] == str(i)].index, inplace = True)


flights1.set_index(['flightID'], inplace=True)

RT7_lat = [60.761417,60.724861,60.657833,60.567194,60.466111]
RT8_lat = [60.572944,60.6685,60.739528,60.771639,60.466111]
RT7_lon = [10.977667,10.778139,10.616583,10.510444,11.084444]
RT8_lon = [10.479722,10.590667,10.760528,10.9185,11.084444]

GM404_circle_center = Point(10.256944, 59.814444)
GM405_circle_center = Point(10.1785, 60.027056)
GM406_circle_center = Point(10.180472, 59.91725)
GM407_circle_center = Point(10.211389, 60.024306)
GM408_circle_center = Point(10.213278, 59.920528)
GM409_circle_center = Point(10.285444, 59.822778)
GM410_circle_center = Point(10.41975, 59.743583)
GM411_circle_center = Point(11.704639, 59.816194)
GM412_circle_center = Point(11.427306, 59.65125)
GM413_circle_center = Point(11.595222, 59.721278)
GM414_circle_center = Point(11.67475, 59.821861)
GM415_circle_center = Point(11.569167, 59.732583)
GM416_circle_center = Point(11.217, 59.630412)
GM417_circle_center = Point(11.410528, 59.665472)
GM418_circle_center = Point(11.7955, 60.651194)
GM419_circle_center = Point(11.930556, 60.570167)
GM420_circle_center = Point(12.001583, 60.471861)
GM421_circle_center = Point(12.000083, 60.368222)
GM423_circle_center = Point(12.03375, 60.36525)
GM424_circle_center = Point(12.03525, 60.474583)
GM425_circle_center = Point(11.9595, 60.578)
GM432_circle_center = Point(RT7_lon[0],RT7_lat[0])
GM433_circle_center = Point(RT7_lon[1],RT7_lat[1])
GM434_circle_center = Point(RT7_lon[2],RT7_lat[2])
GM435_circle_center = Point(RT7_lon[3],RT7_lat[3])
GM429_circle_center = Point(RT8_lon[0],RT8_lat[0])
GM430_circle_center = Point(RT8_lon[1],RT8_lat[1])
GM431_circle_center = Point(RT8_lon[2],RT8_lat[2])
GM453_circle_center = Point(11.858472, 60.644361)
GM452_circle_center = Point(RT8_lon[3],RT8_lat[3])
GM454_circle_center = Point(11.275028, 59.619333)
GM455_circle_center = Point(10.358917, 59.748833)

NE = [GM423_circle_center,GM424_circle_center,GM425_circle_center,GM453_circle_center,GM418_circle_center,GM419_circle_center,GM420_circle_center,GM421_circle_center]
NW = [GM429_circle_center,GM430_circle_center,GM431_circle_center,GM452_circle_center,GM432_circle_center,GM433_circle_center,GM434_circle_center,GM435_circle_center]
SE = [GM416_circle_center,GM417_circle_center,GM415_circle_center,GM414_circle_center,GM411_circle_center,GM413_circle_center,GM412_circle_center,GM454_circle_center]
SW = [GM410_circle_center,GM409_circle_center,GM408_circle_center,GM407_circle_center,GM405_circle_center,GM406_circle_center,GM404_circle_center,GM455_circle_center]

NEn = ['GM423','GM424','GM425','GM453','GM418','GM419','GM420','GM421']
NWn = ['GM429','GM430','GM431','GM452','GM432','GM433','GM434','GM435']
SEn = ['GM411','GM413','GM412','GM454','GM416','GM417','GM415','GM414']
SWn = ['GM405','GM406','GM404','GM455','GM410','GM409','GM408','GM407']

if PMsystem == 'NE':
    points = NE
    names = NEn
    thres = 60.5
elif PMsystem == 'NW':
    points = NW
    names = NWn
    thres = 60.62
elif PMsystem == 'SE':
    points = SE
    names = SEn
    thres = 59.75
else:
    points = SW
    names = SWn
    thres = 59.9
    

print('calculating for '+PMsystem+' system, check: ',points)

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
        if zero_lat >= thres:
            if (check_circle_contains_point(points[7], radius, Point(lon, lat))):
                PM_usage.loc[len(PM_usage)] = [flight_id,names[7]]
                print('in '+names[7])
                break
            elif (check_circle_contains_point(points[6], radius, Point(lon, lat))):
                PM_usage.loc[len(PM_usage)] = [flight_id,names[6]]
                print('in '+names[6])
                break
            elif (check_circle_contains_point(points[5], radius, Point(lon, lat))):
                PM_usage.loc[len(PM_usage)] = [flight_id,names[5]]
                print('in '+names[5])
                break
            elif (check_circle_contains_point(points[4], radius, Point(lon, lat))):
                PM_usage.loc[len(PM_usage)] = [flight_id,names[4]]
                print('went up to '+names[4])
                break
            else:
                print('in none of them')
                continue
        else:
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
    filename = airport_icao+"_"+PMsystem+"_ARCS.csv"
elif radius == 0.03:
    filename = airport_icao+"_"+PMsystem+"_ARCS_rad03.csv"
PM_usage.to_csv(os.path.join('Output', filename), sep=' ', encoding='utf-8', float_format='%.3f', index = True, header = False)

