import numpy as np
import pandas as pd
from shapely.geometry import Point
from shapely.geometry.polygon import Polygon
import time
import os
start_time = time.time()

year = '2022'
airport_icao = "EIDW"
month = '07',
radius = 0.05
# ENGM PM system in ['SE','SW','NE','NW']
PMsystem = 'W'
if PMsystem == '':
    file = ''
elif PMsystem == 'W':
    file = 'WEST_'

DATASET_DATA_DIR = os.path.join('..', "Outputs")
filename = "PM_"+file+"dataset_v2.csv"
flights1 = pd.read_csv(os.path.join(DATASET_DATA_DIR, filename), sep=' ',
    names = ['flightId', 'sequence', 'timestamp', 'lat', 'lon', 'rawAltitude', 'altitude', 'velocity', 'beginDate', 'endDate'],
    dtype={'flightId':str, 'sequence':int, 'timestamp':int, 'lat':float, 'lon':float, 'rawAltitude':float, 'altitude':float, 'velocity':float, 'beginDate':str, 'endDate':str})



list_col_names = ['flightID', 'sequence', 'timestamp', 'lat', 'lon', 'rawAltitude', 'baroAltitude', 'velocity','endDate', 'date']
flights1.columns = list_col_names
flights1 = flights1.drop(['date'], axis=1)
    


err = ['220705RYR846Z','220705RYR8556','220713EIN74P','220710RYR21PU','220711EIN415','220701RYR7GK','220706THY98W','220701RYR4CA','220706EIN52X',
          '220702RYR7VN','220705BAW84W', '220719EIN605P', '220721RYR59BD', '220721RYR69QY','220721RYR863', '220721RYR92EW', '220721RYR9PT',
          '220716RYR671', '220717SWR48X', '220718EAI65BM', '220718RYR42XU','220719RYR3KU','220717RYR34BD','220721EIN63K','220717EIN545','220722CFE221',
          '220722EAI95LS', '220722EIN3LG','220722EIN69Y', '220722RYR94HQ', '220727EAI75BH', '220727EIN209', '220728EAB27MU','220714RYR3UN',
          '220722EIN799', '220724EIN545', '220725EAI57EU', '220725RYR171J','220724RYR56RB', '220726TOM239','220705RYR22EL','220706RYR1FL',
          '220715EIN122','220716EIN122','220717EIN960','220719AAL208','220719RYR84HD','220721AAL722','220721RYR4DP','220717RYR3JX','220720DAL154',
          '220721EAI87DM','220721EIN70V','220715EIN1MN','220721AFR95UF', '220721BLA2RA', '220721BLA4JU', '220721DLH982','220721EIN33W', '220721EIN4GJ',
          '220721EIN529','220721EIN737','220721EIN76HJ', '220721FIA711', '220721RYR12MC', '220721RYR1341','220721RYR1UP', '220721RYR2PV', '220721RYR323M',
          '220721RYR3WR','220721RYR3YW', '220721RYR47JE', '220721RYR673', '220721RYR69NK','220721RYR6MW', '220721RYR7149', '220721RYR717R', '220721RYR72',
          '220721RYR74TG', '220721RYR7EX', '220721RYR7ZZ', '220721RYR98KD','220721RYR9GF', '220721RYR9LK','220722EIN122', '220722EIN1MN', '220722EIN58R',
          '220722EIN5HL','220723AAL722', '220723AAL724', '220727EIN104', '220728EIN104','220728EIN122', '220728EIN13K', '220728RYR6678','220723EIN122',
          '220723EIN1MN', '220724EIN104', '220724EIN1TC','220727EIN11P','220722BLA3SX', '220722EIN17VT', '220722EIN38JC', '220722EIN497','220722RYR4AV',
          '220722TOM1487', '220722TOM2DT','220722RYR23FJ']

flights1 = flights1[~flights1['flightID'].isin(err)]
flights1.set_index(['flightID'], inplace=True)

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

SIVNA_lat, SIVNA_lon = dms2dd("531152.3N 0053827.7W")
SIVNA_circle_center = Point(SIVNA_lon, SIVNA_lat)
KOGAX_lat, KOGAX_lon = dms2dd("533418.6N 0053814.1W")
KOGAX_circle_center = Point(KOGAX_lon, KOGAX_lat)
ASDER_lat, ASDER_lon = dms2dd("533346.7N 0062226.4W")
ASDER_circle_center = Point(ASDER_lon, ASDER_lat)
BERMO_lat, BERMO_lon = dms2dd("531738.9N 0062450.8W")
BERMO_circle_center = Point(BERMO_lon, BERMO_lat)
KUDOM_lat, KUDOM_lon = dms2dd("532925.8N 0053314.3W")
KUDOM_circle_center = Point(KUDOM_lon, KUDOM_lat)
DW814_lat, DW814_lon = dms2dd("532347.5N 0053141.1W")
DW814_circle_center = Point(DW814_lon, DW814_lat)
DW815_lat, DW815_lon = dms2dd("531812.9N 0053346.6W")
DW815_circle_center = Point(DW815_lon, DW815_lat)
DW816_lat, DW816_lon = dms2dd("531346.9N 0053844.4W")
DW816_circle_center = Point(DW816_lon, DW816_lat)
SUGAD_lat, SUGAD_lon = dms2dd("531722.5N 0053139.8W")
SUGAD_circle_center = Point(SUGAD_lon, SUGAD_lat)
DW704_lat, DW704_lon = dms2dd("532403.7N 0052910.1W")
DW704_circle_center = Point(DW704_lon, DW704_lat)
DW705_lat, DW705_lon = dms2dd("533046.6N 0053126.4W")
DW705_circle_center = Point(DW705_lon, DW705_lat)
DW706_lat, DW706_lon = dms2dd("533621.3N 0053806.9W")
DW706_circle_center = Point(DW706_lon, DW706_lat)
AKIVA_lat, AKIVA_lon = dms2dd("533856.0N 0062709.6W")
AKIVA_circle_center = Point(AKIVA_lon, AKIVA_lat)
ADNAL_lat, ADNAL_lon = dms2dd("534153.9N 0063541.5W")
ADNAL_circle_center = Point(ADNAL_lon, ADNAL_lat)
APRUT_lat, APRUT_lon = dms2dd("534149.0N 0064534.9W")
APRUT_circle_center = Point(APRUT_lon, APRUT_lat)
DW865_lat, DW865_lon = dms2dd("533842.8N 0065358.4W")
DW865_circle_center = Point(DW865_lon, DW865_lat)
DW866_lat, DW866_lon = dms2dd("533329.1N 0065827.2W")
DW866_circle_center = Point(DW866_lon, DW866_lat)
BABON_lat, BABON_lon = dms2dd("531303.3N 0063056.5W")
BABON_circle_center = Point(BABON_lon, BABON_lat)
BIVDI_lat, BIVDI_lon = dms2dd("531059.5N 0064005.6W")
BIVDI_circle_center = Point(BIVDI_lon, BIVDI_lat)
DW754_lat, DW754_lon = dms2dd("531202.3N 0064942.6W")
DW754_circle_center = Point(DW754_lon, DW754_lat)
DW755_lat, DW755_lon = dms2dd("531554.2N 0065704.5W")
DW755_circle_center = Point(DW755_lon, DW755_lat)

E = [KOGAX_circle_center,KUDOM_circle_center,DW814_circle_center,DW815_circle_center,DW816_circle_center,SIVNA_circle_center,SUGAD_circle_center,DW704_circle_center,DW705_circle_center,DW706_circle_center]
W = [ASDER_circle_center,AKIVA_circle_center,ADNAL_circle_center,APRUT_circle_center,DW865_circle_center,DW866_circle_center,BERMO_circle_center,BABON_circle_center,BIVDI_circle_center,DW754_circle_center,DW755_circle_center]

En = ['KOGAX','KUDOM','DW814','DW815','DW816','SIVNA','SUGAD','DW704','DW705','DW706']
Wn = ['ASDER','AKIVA','ADNAL','APRUT','DW865','DW866','BERMO','BABON','BIVDI','DW754','DW755']


if PMsystem == '':
    points = E
    names = En
    thres = 53.25
elif PMsystem == 'W':
    points = W
    names = Wn
    thres = 53.25
    

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
            if (check_circle_contains_point(points[5], radius, Point(lon, lat))):
                PM_usage.loc[len(PM_usage)] = [flight_id,names[5]]
                print('in '+names[5])
                break
            elif (check_circle_contains_point(points[4], radius, Point(lon, lat))):
                PM_usage.loc[len(PM_usage)] = [flight_id,names[4]]
                print('in '+names[4])
                break
            elif (check_circle_contains_point(points[3], radius, Point(lon, lat))):
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
        else:
            if (check_circle_contains_point(points[10], radius, Point(lon, lat))):
                PM_usage.loc[len(PM_usage)] = [flight_id,names[10]]
                print('in '+names[10])
                break
            elif (check_circle_contains_point(points[9], radius, Point(lon, lat))):
                PM_usage.loc[len(PM_usage)] = [flight_id,names[9]]
                print('in '+names[9])
                break
            elif (check_circle_contains_point(points[8], radius, Point(lon, lat))):
                PM_usage.loc[len(PM_usage)] = [flight_id,names[8]]
                print('in '+names[8])
                break
            elif (check_circle_contains_point(points[7], radius, Point(lon, lat))):
                PM_usage.loc[len(PM_usage)] = [flight_id,names[7]]
                print('in '+names[7])
                break
            elif (check_circle_contains_point(points[6], radius, Point(lon, lat))):
                PM_usage.loc[len(PM_usage)] = [flight_id,names[6]]
                print('went up to '+names[6])
                break
            else:
                print('in none of them')
                continue

if radius == 0.05:
    filename = airport_icao+"_"+PMsystem+"_ARCS_v2.csv"
elif radius == 0.03:
    filename = airport_icao+"_"+PMsystem+"_ARCS_rad03.csv"
PM_usage.to_csv(os.path.join(DATASET_DATA_DIR, filename), sep=' ', encoding='utf-8', float_format='%.3f', index = True, header = False)

