import numpy as np
import pandas as pd
from shapely.geometry import Point
from shapely.geometry.polygon import Polygon
import time
import os
start_time = time.time()

year = '2022'
airport_icao = "RKSI"
month = '12'
PMsystem = 'NE'
radius = 0.05
dat = PMsystem

DATASET_DATA_DIR = os.path.join('..', "Outputs")
filename = "PM_dataset_"+dat+".csv"
flights1 = pd.read_csv(os.path.join(DATASET_DATA_DIR, filename), sep=' ',
    names = ['flightID', 'sequence', 'timestamp', 'lat', 'lon', 'rawAltitude', 'altitude', 'velocity', 'beginDate', 'endDate'],
    dtype={'flightID':str, 'sequence':int, 'timestamp':int, 'lat':float, 'lon':float, 'rawAltitude':float, 'altitude':float, 'velocity':float, 'beginDate':str, 'endDate':str})


err = ['221202TWB172', '221201ASV528', '221202JJA2206', '221203KAL320',
       '221215KAL630', '221222AAR7139','221202AAR736', '221202AAR740', '221202AAR762', '221202CES7041',
              '221202HVN408', '221202JJA2904', '221202JNA052', '221202KAL314',
              '221202KAL628', '221202KAL690', '221202PAL468', '221202SWM215',
              '221202VJC960', '221201AAR740', '221201AAR742', '221201BAV450',
              '221201JJA2204', '221201KAL630', '221202AAR390', '221202AAR704',
              '221202AAR970', '221202AFR193', '221202AIH512', '221202APG884',
              '221202APG9048', '221202BOX571', '221202CEB188', '221202CPA410',
              '221202FDX6076', '221202HVN430', '221202JJA4908', '221202KAL320',
              '221202KAL375', '221202KAL624', '221202KAL646', '221202KAL660',
              '221202KAL696', '221202KAL756', '221202KAL8442', '221202KLM832',
              '221202TGW842', '221202TGW896', '221202VJC836', '221202VJC838',
              '221202VJC878', '221202VJC880', '221202VJC962', '221202VJC974',
              '221202WGN5274', '221203AAR7149', '221203AIC312', '221203AIH512',
              '221203APG884', '221203APZ632', '221203KAL362', '221203KAL8186',
              '221203TAX700', '221201TWB102', '221202LAO923', '221208ABL748',
              '221208BAV450', '221208CEB186', '221208HVN430', '221208HVN440',
              '221208JJA2508', '221208KAL178', '221208AAR392', '221208AAR734',
              '221208AAR988', '221208ABL788', '221208ASV512', '221208BOX571',
              '221208CKK257', '221208GTI555', '221208HVN408', '221208JNA026',
              '221208KAL180', '221208KAL316', '221208KAL624', '221208KAL652',
              '221208KAL664', '221208KAL672', '221208KAL690', '221208LAO923',
              '221208JJA4206', '221208JJA4908', '221208JNA018', '221208KAL644',
              '221215AIH2426', '221215APG884', '221215APZ632', '221215CES7041',
              '221215CPA410', '221215CRK628', '221215DAL288', '221215HKE630',
              '221215JJA2206', '221215JJA4908', '221215JJA9206', '221215JNA942F',
              '221215KAL186']
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

PY049_lat, PY049_lon = dms2dd("370817.90N 1254804.60E")
PY049_circle_center = Point(PY049_lon, PY049_lat)
PY037_lat, PY037_lon = dms2dd("370828.10N 1260325.20E")
PY037_circle_center = Point(PY037_lon, PY037_lat)
CW001_lat, CW001_lon = dms2dd("371047.30N 1262003.60E")
CW001_circle_center = Point(CW001_lon, CW001_lat)
CW002_lat, CW002_lon = dms2dd("370652.40N 1262107.40E")
CW002_circle_center = Point(CW002_lon, CW002_lat)
CW003_lat, CW003_lon = dms2dd("370336.40N 1262400.80E")
CW003_circle_center = Point(CW003_lon, CW003_lat)
CW004_lat, CW004_lon = dms2dd("370130.30N 1262816.00E")
CW004_circle_center = Point(CW004_lon, CW004_lat)
CW005_lat, CW005_lon = dms2dd("370054.30N 1263312.30E")
CW005_circle_center = Point(CW005_lon, CW005_lat)
PAMBI_lat, PAMBI_lon = dms2dd("371054.30N 1263234.40E")
PAMBI_circle_center = Point(PAMBI_lon, PAMBI_lat)
NODUN_lat, NODUN_lon = dms2dd("371110.10N 1272025.50E")
NODUN_circle_center = Point(NODUN_lon, NODUN_lat)
UPSOM_lat, UPSOM_lon = dms2dd("372838.80N 1271904.30E")
UPSOM_circle_center = Point(UPSOM_lat, UPSOM_lon)
GUDKO_lat, GUDKO_lon = dms2dd("370110.90N 1273822.90E")
GUDKO_circle_center = Point(GUDKO_lon, GUDKO_lat)
GC072_lat, GC072_lon = dms2dd("372001.00N 1272512.20E")
GC072_circle_center = Point(GC072_lon, GC072_lat)
GC071_lat, GC071_lon = dms2dd("372938.50N 1272513.70E")
GC071_circle_center = Point(GC071_lon, GC071_lat)
SEL_lat, SEL_lon = dms2dd("372449.00N 1265542.10E")
SEL_circle_center = Point(SEL_lon, SEL_lat)
KARBU_lat, KARBU_lon = dms2dd("373159.00N 1273952.00E")
KARBU_circle_center = Point(KARBU_lon, KARBU_lat)
KC067_lat, KC067_lon = dms2dd("372101.50N 1271903.70E")
KC067_circle_center = Point(KC067_lon, KC067_lat)
KC066_lat, KC066_lon = dms2dd("371401.20N 1271518.80E")
KC066_circle_center = Point(KC066_lon, KC066_lat)


S = [CW001_circle_center,CW002_circle_center,CW003_circle_center,CW004_circle_center,CW005_circle_center]
NW = [UPSOM_circle_center,KC067_circle_center,KC066_circle_center]
NE = [NODUN_circle_center,GC072_circle_center,GC071_circle_center]

Sn = ['CW001','CW002','CW003','CW004','CW005']
NWn = ['UPSOM','KC067','KC066']
NEn = ['NODUN','GC072','GC071']

if PMsystem == 'NE':
    points = NE
    names = NEn
elif PMsystem == 'NW':
    points = NW
    names = NWn
elif PMsystem == 'S':
    points = S
    names = Sn

thres = 37.20
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
        if PMsystem == 'S':
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
        else:
            if (check_circle_contains_point(points[2], radius, Point(lon, lat))):
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
    filename = airport_icao+"_"+PMsystem+"_v2_ARCS.csv"
elif radius == 0.03:
    filename = airport_icao+"_ARCS_rad03.csv"
PM_usage.to_csv(os.path.join(DATASET_DATA_DIR, filename), sep=' ', encoding='utf-8', float_format='%.3f', index = True, header = False)

