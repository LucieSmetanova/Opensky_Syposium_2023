import numpy as np
import pandas as pd
from shapely.geometry import Point
from shapely.geometry.polygon import Polygon
import time
import os
start_time = time.time()

year = '2022'
airport_icao = "ULLI"
month = '08'
PMsystem = 'NW'
radius = 0.05

#specify path to your downloaded opensky data
DATASET_DATA_DIR = os.path.join('..', "Outputs")
filename = "PM_dataset_"+PMsystem+"_v2.csv"
flights1 = pd.read_csv(os.path.join(DATASET_DATA_DIR, filename), sep=' ',
    names = ['flightID', 'sequence', 'timestamp', 'lat', 'lon', 'rawAltitude', 'altitude', 'velocity', 'beginDate', 'endDate'],
    dtype={'flightID':str, 'sequence':int, 'timestamp':int, 'lat':float, 'lon':float, 'rawAltitude':float, 'altitude':float, 'velocity':float, 'beginDate':str, 'endDate':str})


err = ['220813SDM6442','220810SDM6002', '220825SDM6402', '220825SDM6452', '220825SDM6574','220801SDM6462', '220811PBD530', '220812PBD536', '220825SDM6332',
       '220824SDM6002', '220825NWS594', '220825PBD592','220806AFL032', '220806SDM6024', '220806SDM6066', '220806UZB631',
              '220808SDM6014', '220810AFL058', '220813VDA6474','220806SVR124','220802SDM6036','220806GZP835','220801AFL018', '220801AUL532', '220801PBD508', '220806SDM6596',
                     '220808SDM6324', '220810SVR8642', '220814SDM6596', '220818PBD560',
                     '220820AFL028', '220825KAR317', '220826PBD314', '220826PBD560',
                     '220826SDM6596','220812UPEM020','220801UZB637','220821SDM6116','220824SBI1015']
flights1 = flights1[~flights1['flightID'].isin(err)]

print('data error extracted')
flights1.set_index(['flightID'], inplace=True)

print('points done')
def dms2dd(as_string):
    degrees = int(as_string[:2])
    minutes = int(as_string[2:4])
    seconds = float(as_string[4:8])
    lat_dd = float(degrees) + float(minutes)/60 + float(seconds)/(60*60)
    degrees = int(as_string[10:14])
    minutes = int(as_string[14:16])
    seconds = float(as_string[16:21])
    lon_dd = float(degrees) + float(minutes)/60 + float(seconds)/(60*60)

    return lat_dd, lon_dd

LI725_lat, LI725_lon = dms2dd("594341.10N 0292816.00E")
LI725_circle_center = Point(LI725_lon, LI725_lat)
LI739_lat, LI739_lon = dms2dd("600226.20N 0293900.00E")
LI739_circle_center = Point(LI739_lon, LI739_lat)
LI760_lat, LI760_lon = dms2dd("595123.50N 0310020.80E")
LI760_circle_center = Point(LI760_lon, LI760_lat)
LI766_lat, LI766_lon = dms2dd("595148.10N 0310943.70E")
LI766_circle_center = Point(LI766_lon, LI766_lat)
LI761_lat, LI761_lon = dms2dd("594531.60N 0310432.30E")
LI761_circle_center = Point(LI761_lon, LI761_lat)
LI748_lat, LI748_lon = dms2dd("593149.50N 0305225.20E")
LI748_circle_center = Point(LI748_lon, LI748_lat)
LI754_lat, LI754_lon = dms2dd("593101.00N 0310120.90E")
LI754_circle_center = Point(LI754_lon, LI754_lat)
LI749_lat, LI749_lon = dms2dd("593533.60N 0310137.70E")
LI749_circle_center = Point(LI749_lon, LI749_lat)
LI737_lat, LI737_lon = dms2dd("600248.20N 0295828.70E")
LI737_circle_center = Point(LI737_lon, LI737_lat)
LI738_lat, LI738_lon = dms2dd("600340.10N 0294510.90E")
LI738_circle_center = Point(LI738_lon, LI738_lat)
LI740_lat, LI740_lon = dms2dd("595920.10N 0293146.70E")
LI740_circle_center = Point(LI740_lon, LI740_lat)
LI741_lat, LI741_lon = dms2dd("595505.70N 0292727.00E")
LI741_circle_center = Point(LI741_lon, LI741_lat)
LI742_lat, LI742_lon = dms2dd("595020.90N 0292638.50E")
LI742_circle_center = Point(LI742_lon, LI742_lat)
LI743_lat, LI743_lon = dms2dd("594547.90N 0292926.70E")
LI743_circle_center = Point(LI743_lon, LI743_lat)
LI733_lat, LI733_lon = dms2dd("600655.70N 0293036.40E")
LI733_circle_center = Point(LI733_lon, LI733_lat)
LI732_lat, LI732_lon = dms2dd("600820.00N 0291344.60E")
LI732_circle_center = Point(LI732_lon, LI732_lat)
LI722_lat, LI722_lon = dms2dd("593245.50N 0303016.20E")
LI722_circle_center = Point(LI722_lon, LI722_lat)
LI723_lat, LI723_lon = dms2dd("593930.70N 0294454.90E")
LI723_circle_center = Point(LI723_lon, LI723_lat)
LI724_lat, LI724_lon = dms2dd("594055.10N 0293511.60E")
LI724_circle_center = Point(LI724_lon, LI724_lat)
LI730_lat, LI730_lon = dms2dd("591507.30N 0291958.20E")
LI730_circle_center = Point(LI730_lon, LI730_lat)
LI731_lat, LI731_lon = dms2dd("592555.90N 0284907.90E")
LI731_circle_center = Point(LI731_lon, LI731_lat)
LI726_lat, LI726_lon = dms2dd("595010.40N 0292327.00E")
LI726_circle_center = Point(LI726_lon, LI726_lat)
LI727_lat, LI727_lon = dms2dd("595532.30N 0292421.40E")
LI727_circle_center = Point(LI727_lon, LI727_lat)
LI728_lat, LI728_lon = dms2dd("600020.00N 0292914.70E")
LI728_circle_center = Point(LI728_lon, LI728_lat)
LI729_lat, LI729_lon = dms2dd("600350.60N 0293724.60E")
LI729_circle_center = Point(LI729_lon, LI729_lat)
LI759_lat, LI759_lon = dms2dd("595613.40N 0304712.80E")
LI759_circle_center = Point(LI759_lon, LI759_lat)
LI765_lat, LI765_lon = dms2dd("595719.50N 0314050.10E")
LI765_circle_center = Point(LI765_lon, LI765_lat)
LI762_lat, LI762_lon = dms2dd("594047.20N 0310334.40E")
LI762_circle_center = Point(LI762_lon, LI762_lat)
LI763_lat, LI763_lon = dms2dd("593634.80N 0305909.20E")
LI763_circle_center = Point(LI763_lon, LI763_lat)
LI764_lat, LI764_lon = dms2dd("593331.30N 0305156.70E")
LI764_circle_center = Point(LI764_lon, LI764_lat)
LI746_lat, LI746_lon = dms2dd("593151.40N 0302738.90E")
LI746_circle_center = Point(LI746_lon, LI746_lat)
LI747_lat, LI747_lon = dms2dd("593150.90N 0304148.90E")
LI747_circle_center = Point(LI747_lon, LI747_lat)
LI750_lat, LI750_lon = dms2dd("594018.90N 0310637.80E")
LI750_circle_center = Point(LI750_lon, LI750_lat)
LI751_lat, LI751_lon = dms2dd("594540.40N 0310743.70E")
LI751_circle_center = Point(LI751_lon, LI751_lat)
LI752_lat, LI752_lon = dms2dd("595050.70N 0310444.00E")
LI752_circle_center = Point(LI752_lon, LI752_lat)
MADID_lat, MADID_lon = dms2dd("594530.10N 0303515.00E")
MADID_circle_center = Point(MADID_lon, MADID_lat)
BIPRI_lat, BIPRI_lon = dms2dd("594452.50N 0303356.30E")
BIPRI_circle_center = Point(BIPRI_lon, BIPRI_lat)
LEPTO_lat, LEPTO_lon = dms2dd("595109.30N 0295716.80E")
LEPTO_circle_center = Point(LEPTO_lon, LEPTO_lat)
GEBKA_lat, GEBKA_lon = dms2dd("595030.40N 0295600.80E")
GEBKA_circle_center = Point(GEBKA_lon, GEBKA_lat)

NE = [LI739_circle_center,LI740_circle_center,LI741_circle_center,LI742_circle_center,LI743_circle_center]
NW = [LI760_circle_center,LI761_circle_center,LI762_circle_center,LI763_circle_center,LI764_circle_center]
SE = [LI725_circle_center,LI726_circle_center,LI727_circle_center,LI728_circle_center,LI729_circle_center]
SW = [LI748_circle_center,LI749_circle_center,LI750_circle_center,LI751_circle_center,LI752_circle_center]

NEn = ['LI739','LI740','LI741','LI742','LI743']
NWn = ['LI760','LI761','LI762','LI763','LI764']
SEn = ['LI725','LI726','LI727','LI728','LI729']
SWn = ['LI748','LI749','LI750','LI751','LI752']

if PMsystem == 'NE':
    points = NE
    names = NEn
elif PMsystem == 'NW':
    points = NW
    names = NWn
elif PMsystem == 'SE':
    points = SE
    names = SEn
else:
    points = SW
    names = SWn

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
    zero_lon = flight_df['lon'][0]
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
        if (check_circle_contains_point(points[4], radius, Point(lon, lat))):
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

if radius == 0.05:
    filename = airport_icao+"_"+PMsystem+"_ARCS.csv"
elif radius == 0.03:
    filename = airport_icao+"_ARCS_rad03.csv"
PM_usage.to_csv(os.path.join(DATASET_DATA_DIR, filename), sep=' ', encoding='utf-8', float_format='%.3f', index = True, header = False)

