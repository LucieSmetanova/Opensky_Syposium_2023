import numpy as np
import pandas as pd
from shapely.geometry import Point
from shapely.geometry.polygon import Polygon
import time
import os
start_time = time.time()

year = '2022'
airport_icao = "SKBO"
month = '12'
radius = 0.05

#specify path to your downloaded opensky data
DATASET_DATA_DIR = os.path.join('..', "Outputs")
filename = "PM_dataset.csv"
flights1 = pd.read_csv(os.path.join(DATASET_DATA_DIR, filename), sep=' ',
    names = ['flightId', 'sequence', 'timestamp', 'lat', 'lon', 'rawAltitude', 'altitude', 'velocity', 'beginDate', 'endDate'],
    dtype={'flightId':str, 'sequence':int, 'timestamp':int, 'lat':float, 'lon':float, 'rawAltitude':float, 'altitude':float, 'velocity':float, 'beginDate':str, 'endDate':str})
print('data uploaded')


list_col_names = ['flightID', 'sequence', 'timestamp', 'lat', 'lon', 'rawAltitude', 'baroAltitude', 'velocity','endDate', 'date']
flights1.columns = list_col_names
flights1 = flights1.drop(['date'], axis=1)
print('data types done')

err = ['221201AVA257','221201KLM749','221216AVA037','221201RPB7005','221202AVA079','221205RPB7027',
         '221202AVA129','221204AVA8561','221222AVA9376','221228RPB7410','221228VVC5618','221205AVA129',
         '221201AVA253', '221202RPB7025', '221203AVA129', '221203RPB7027',
                '221204AVA253', '221206ACL865', '221206AVA093', '221208ACL1153',
                '221210AVA093', '221210AVA124', '221211AVA9460', '221212AVA8419',
                '221214ARE4400', '221214AVA079', '221214AVA209', '221214HK2596',
                '221215AVA052', '221216AVA079', '221218AVA259', '221220ACL864',
                '221222RPB7081', '221224AVA127', '221225RPB7027','221201AVA9781', '221202ARE4255', '221203AVA057', '221203AVA059',
                       '221203CMP416', '221205AVA116', '221206ACL1161', '221208ARE4255',
                       '221208ARE4257', '221208CMP413', '221210AVA053', '221210CMP872',
                       '221210RPB7412', '221211AVA059', '221212ARE4257', '221212RPB7576',
                       '221213ULS5167', '221214ARE4255', '221214AVA8561', '221214VVC5619',
                       '221217AVA058', '221219ARE4257', '221219AVA8527', '221219GLG8383',
                       '221221AVA069', '221221AVA192', '221222VVC0436', '221223AVA9374',
                       '221223VVC5628', '221224ARE4256', '221224VVC8325', '221225ULS5166',
                       '221226RPB7410', '221226VVC8328', '221228AVA9778']
flights1 = flights1[~flights1['flightID'].isin(err)]

print('data error extracted')
flights1.set_index(['flightID'], inplace=True)

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

BO804_lat, BO804_lon = dms2dd('052506.00N 0740630.00W')
BO804_circle_center = Point(BO804_lon, BO804_lat)
PAPET_lat, PAPET_lon = dms2dd('051359.10N 0741904.78W')
PAPET_circle_center = Point(PAPET_lon, PAPET_lat)
SUR01_lat, SUR01_lon = dms2dd('051440.07N 0742743.85W')
SUR01_circle_center = Point(SUR01_lon, SUR01_lat)
SUR02_lat, SUR02_lon = dms2dd('051137.19N 0743551.51W')
SUR02_circle_center = Point(SUR02_lon, SUR02_lat)
SUR03_lat, SUR03_lon = dms2dd('050449.17N 0744217.59W')
SUR03_circle_center = Point(SUR03_lon, SUR03_lat)
TOBKI_lat, TOBKI_lon = dms2dd('045630.78N 0744454.16W')
TOBKI_circle_center = Point(TOBKI_lon, TOBKI_lat)
BO885_lat, BO885_lon = dms2dd('045527.75N 0743254.72W')
BO885_circle_center = Point(BO885_lon, BO885_lat)
AMVES_lat, AMVES_lon = dms2dd('045445.99N 0742456.45W')
AMVES_circle_center = Point(AMVES_lon, AMVES_lat)
BO824_lat, BO824_lon = dms2dd('052019.62N 0740034.24W')
BO824_circle_center = Point(BO824_lon, BO824_lat)
BO832_lat, BO832_lon = dms2dd('050702.01N 0735743.14W')
BO832_circle_center = Point(BO832_lon, BO832_lat)
GERBA_lat, GERBA_lon = dms2dd('042611.64N 0745000.76W')
GERBA_circle_center = Point(GERBA_lon, GERBA_lat)
IRUPU_lat, IRUPU_lon = dms2dd("044607.05N 0744723.02W")
IRUPU_circle_center = Point(IRUPU_lon, IRUPU_lat)
BO862_lat, BO862_lon = dms2dd("043623.25N 0750454.62W")
BO862_circle_center = Point(BO862_lon, BO862_lat)
BO886_lat, BO886_lon = dms2dd("045016.82N 0750659.00W")
BO886_circle_center = Point(BO886_lon, BO886_lat)
MQU_lat, MQU_lon = dms2dd("051218.00N 0745516.00W")
MQU_circle_center = Point(MQU_lon, MQU_lat)
NOR02_lat, NOR02_lon = dms2dd("050649.75N 0744545.88W")
NOR02_circle_center = Point(NOR02_lon, NOR02_lat)
BO950_lat, BO950_lon = dms2dd("052457.91N 0741913.77W")
BO950_circle_center = Point(BO950_lon, BO950_lat)
NOR01_lat, NOR01_lon = dms2dd('045651.67N 0744853.72W')
NOR01_circle_center = Point(NOR01_lon, NOR01_lat)
NOR03_lat, NOR03_lon = dms2dd('051459.40N 0743802.59W')
NOR03_circle_center = Point(NOR03_lon, NOR03_lat)
NOR04_lat, NOR04_lon = dms2dd('051838.89N 0742817.35W')
NOR04_circle_center = Point(NOR04_lon, NOR04_lat)
NOR05_lat, NOR05_lon = dms2dd('051749.71N 0741754.40W')
NOR05_circle_center = Point(NOR05_lon, NOR05_lat)
PULDI_lat, PULDI_lon = dms2dd('050227.24N 0742235.82W')
PULDI_circle_center = Point(PULDI_lon, PULDI_lat)
BO884_lat, BO884_lon = dms2dd('050934.60N 0745028.86W')
BO884_circle_center = Point(BO884_lon, BO884_lat)
EDPUL_lat, EDPUL_lon = dms2dd('051655.00N 0751114.00W')
EDPUL_circle_center = Point(EDPUL_lon, EDPUL_lat)
FLOTE_lat, FLOTE_lon = dms2dd('052258.47N 0745947.41W')
FLOTE_circle_center = Point(FLOTE_lon, FLOTE_lat)
BO935_lat, BO935_lon = dms2dd('054005.96N 0743225.58W')
BO935_circle_center = Point(BO935_lon, BO935_lat)
print('points done')
W1 = [PAPET_circle_center,SUR01_circle_center,SUR02_circle_center,SUR03_circle_center,TOBKI_circle_center]
W2 = [IRUPU_circle_center,NOR01_circle_center,NOR02_circle_center,NOR03_circle_center,NOR04_circle_center,NOR05_circle_center]

W1n = ['PAPET','SUR01','SUR02','SUR03','TOBKI']
W2n = ['IRUPU','NOR01','NOR02','NOR03','NOR04','NOR05']

thres = -74.20
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
        if zero_lon <= thres:
            points = W2
            names = W2n
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
            points = W1
            names = W1n
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
    filename = airport_icao+"_ARCS.csv"
elif radius == 0.03:
    filename = airport_icao+"_ARCS_rad03.csv"
PM_usage.to_csv(os.path.join(DATASET_DATA_DIR, filename), sep=' ', encoding='utf-8', float_format='%.3f', index = True, header = False)

