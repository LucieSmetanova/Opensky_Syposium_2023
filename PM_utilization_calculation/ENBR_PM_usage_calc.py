import numpy as np
import pandas as pd
from shapely.geometry import Point
from shapely.geometry.polygon import Polygon
import time
import os
start_time = time.time()

year = '2022'
airport_icao = "ENBR"
month = '10'
radius = 0.05
# ENBR PM system in ['SE','SW','NE','NW1','NW2']
PMsystem = 'NE'
if PMsystem == 'NE':
    file = 'BR624_LUTIV'
elif PMsystem == 'NW1':
    file = 'IRLOB_BR635'
elif PMsystem == 'NW2':
    file = 'BR634_BR633_v2'
elif PMsystem == 'SW':
    file = 'BR724_BR723_pok2'
else:
    file = 'BR734_BR733_pok2'

DATASET_DATA_DIR = os.path.join('..', "Outputs")
filename = "PM_dataset_arrival_50NM_"+file+".csv"
flights1 = pd.read_csv(os.path.join(DATASET_DATA_DIR, filename), sep=' ',
    names = ['flightId', 'sequence', 'timestamp', 'lat', 'lon', 'rawAltitude', 'altitude', 'velocity', 'beginDate', 'endDate'],
    dtype={'flightId':str, 'sequence':int, 'timestamp':int, 'lat':float, 'lon':float, 'rawAltitude':float, 'altitude':float, 'velocity':float, 'beginDate':str, 'endDate':str})



list_col_names = ['flightID', 'sequence', 'timestamp', 'lat', 'lon', 'rawAltitude', 'baroAltitude', 'velocity','endDate', 'date']
flights1.columns = list_col_names
flights1 = flights1.drop(['date'], axis=1)
    

for i in ['221005WIF424','221028WIF418','221027WIF20K','221016WIF04L','221003WIF507','221028WIF503',
          '221002NOZ173','221002WIF71A','221008WIF41S',
          '221012WIF507','221017WIF41S','221024WIF418','221010WIF461','221006WIF0JA','221019WIF291',
          '221026BCS3164','221026SAS4194','221008BHL781','221003BHL939', '221008BHL255', '221011BHL232',
          '221013BHL244','221013BHL255', '221018BHL232', '221018BHL246', '221018BHL247','221018BHL253',
          '221018BHL939', '221019BHL240', '221019BHL245','221019BHL251', '221019BHL252', '221019BHL256',
          '221019BHL939','221020BHL71S', '221020BHL930', '221021BHL242', '221022BHL251','221022BHL782',
          '221018BHL245','221022BHL781','221020BHL781','221007DOC59','221020MDT1','221015DOC55',
          '221005BHL939','221011FIN8DR','221011NOZ616','221009SAS63G','221015WIF43M']:
    flights1.drop(flights1[flights1['flightID'] == str(i)].index, inplace = True)


flights1.set_index(['flightID'], inplace=True)

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

LUNUR_lat, LUNUR_lon = dms2dd('605023.50N 0060506.90E')
DIRBI_lat, DIRBI_lon = dms2dd('603720.26N 0055123.99E')
BR625_lat, BR625_lon = dms2dd('603253.91N 0054647.00E')
LUTIV_lat, LUTIV_lon = dms2dd('603206.39N 0053637.34E')
LUTIV_circle_center = Point(LUTIV_lon, LUTIV_lat)
BR623_lat, BR623_lon = dms2dd('603522.61N 0053428.32E')
BR623_circle_center = Point(BR623_lon, BR623_lat)
BR622_lat, BR622_lon = dms2dd('603803.48N 0053000.66E')
BR622_circle_center = Point(BR622_lon, BR622_lat)
BR621_lat, BR621_lon = dms2dd('603949.41N 0052356.51E')
BR621_circle_center = Point(BR621_lon, BR621_lat)
BR620_lat, BR620_lon = dms2dd('604026.92N 0051556.28E')
BR620_circle_center = Point(BR620_lon, BR620_lat)
GILVA_lat, GILVA_lon = dms2dd('603029.12N 0051649.48E')
PESUR_lat, PESUR_lon = dms2dd('601435.70N 0063507.30E')
BR627_lat, BR627_lon = dms2dd('602122.53N 0060714.83E')
BR624_lat, BR624_lon = dms2dd('602838.60N 0053641.53E')
BR624_circle_center = Point(BR624_lon, BR624_lat)
LEGTA_lat, LEGTA_lon = dms2dd('594918.61N 0054915.29E')
LUSAP_lat, LUSAP_lon = dms2dd('600757.44N 0054231.11E') #ONLY SHORT PART; FEW WAYPOINTS ARE MISSING
EPADU_lat, EPADU_lon = dms2dd('594647.95N 0045420.38E')
BENTI_lat, BENTI_lon = dms2dd('600533.47N 0044858.90E')
BR634_lat, BR634_lon = dms2dd('602415.14N 0044332.34E')
BR634_circle_center = Point(BR634_lon, BR634_lat)
BR633_lat, BR633_lon = dms2dd('602730.71N 0044110.11E')
BR633_circle_center = Point(BR633_lon, BR633_lat)
IRLOB_lat, IRLOB_lon = dms2dd('603058.52N 0044111.66E')
IRLOB_circle_center = Point(IRLOB_lon, IRLOB_lat)
BR632_lat, BR632_lon = dms2dd('603413.52N 0044337.54E')
BR632_circle_center = Point(BR632_lon, BR632_lat)
BR631_lat, BR631_lon = dms2dd('603652.06N 0044810.72E')
BR631_circle_center = Point(BR631_lon, BR631_lat)
BR630_lat, BR630_lon = dms2dd('603844.57N 0045519.02E')
BR630_circle_center = Point(BR630_lon, BR630_lat)
NEPAM_lat, NEPAM_lon = dms2dd('602910.96N 0050105.14E')
MODNI_lat, MODNI_lon = dms2dd('600210.50N 0035951.00E')
BR637_lat, BR637_lon = dms2dd('601355.55N 0042016.98E')
BR636_lat, BR636_lon = dms2dd('602146.37N 0042016.98E')
ETNOR_lat, ETNOR_lon = dms2dd('603725.30N 0035743.40E')
SANDO_lat, SANDO_lon = dms2dd('603327.62N 0042139.17E')
BR635_lat, BR635_lon = dms2dd('603150.98N 0043114.03E')
NIDGI_lat, NIDGI_lon = dms2dd('610340.20N 0044834.80E')
BR638_lat, BR638_lon = dms2dd('604814.20N 0044005.55E')
TUNIX_lat, TUNIX_lon = dms2dd('603640.23N 0043349.43E')
LUNUR_lat, LUNUR_lon = dms2dd('605023.50N 0060506.90E')
ROXET_lat, ROXET_lon = dms2dd('602550.34N 0055052.08E')
BR734_lat, BR734_lon = dms2dd('601046.09N 0054218.39E')
BR734_circle_center = Point(BR734_lon, BR734_lat)
BR733_lat, BR733_lon = dms2dd('600730.97N 0054441.89E')
BR733_circle_center = Point(BR733_lon, BR733_lat)
RATUG_lat, RATUG_lon = dms2dd('600403.14N 0054442.73E')
RATUG_circle_center = Point(RATUG_lon, RATUG_lat)
BR732_lat, BR732_lon = dms2dd('600047.68N 0054221.53E')
BR732_circle_center = Point(BR732_lon, BR732_lat)
BR731_lat, BR731_lon = dms2dd('595808.05N 0053755.88E')
BR731_circle_center = Point(BR731_lon, BR731_lat)
BR730_lat, BR730_lon = dms2dd('595613.23N 0053058.84E')
BR730_circle_center = Point(BR730_lon, BR730_lat)
GODID_lat, GODID_lon = dms2dd('600544.40N 0052502.21E')
PESUR_lat, PESUR_lon = dms2dd('601435.70N 0063507.30E')
BR736_lat, BR736_lon = dms2dd('601316.09N 0055058.46E')
DIBMA_lat, DIBMA_lon = dms2dd('594007.56N 0055046.43E')
LEGTA_lat, LEGTA_lon = dms2dd('594918.61N 0054915.29E')
LATSI_lat, LATSI_lon = dms2dd('595817.54N 0055239.87E')
BR735_lat, BR735_lon = dms2dd('600311.41N 0055432.22E')
NIDGI_lat, NIDGI_lon = dms2dd('610340.20N 0044834.80E')
NIDIN_lat, NIDIN_lon = dms2dd('604030.97N 0044712.89E')
LELMI_lat, LELMI_lon = dms2dd('602545.52N 0044621.71E')
BR724_lat, BR724_lon = dms2dd('600615.11N 0044950.93E')
BR724_circle_center = Point(BR724_lon, BR724_lat)
BR723_lat, BR723_lon = dms2dd('600247.29N 0044949.14E')
BR723_circle_center = Point(BR723_lon, BR723_lat)
IBLIR_lat, IBLIR_lon = dms2dd('595931.67N 0045209.36E')
IBLIR_circle_center = Point(IBLIR_lon, IBLIR_lat)
BR722_lat, BR722_lon = dms2dd('595651.74N 0045634.12E')
BR722_circle_center = Point(BR722_lon, BR722_lat)
BR721_lat, BR721_lon = dms2dd('595506.61N 0050231.36E')
BR721_circle_center = Point(BR721_lon, BR721_lat)
BR720_lat, BR720_lon = dms2dd('595429.34N 0051020.71E')
BR720_circle_center = Point(BR720_lon, BR720_lat)
RIVIP_lat, RIVIP_lon = dms2dd('600427.21N 0050929.36E')
BR727_lat, BR727_lon = dms2dd('600503.85N 0042235.81E')
BR726_lat, BR726_lon = dms2dd('600707.97N 0044000.92E')
ALUVA_lat, ALUVA_lon = dms2dd('592327.40N 0045810.10E')
GENVU_lat, GENVU_lon = dms2dd('593736.90N 0045551.40E')
OKLAN_lat, OKLAN_lon = dms2dd('595218.16N 0044633.50E')
BR725_lat, BR725_lon = dms2dd('595703.04N 0044331.29E')

NW1 = [BR634_circle_center,BR633_circle_center,IRLOB_circle_center,BR632_circle_center,BR631_circle_center,BR630_circle_center]
NW2 = [BR634_circle_center,BR633_circle_center,IRLOB_circle_center,BR632_circle_center,BR631_circle_center,BR630_circle_center]
NE = [BR624_circle_center,LUTIV_circle_center,BR623_circle_center,BR622_circle_center,BR621_circle_center,BR620_circle_center]
SE = [BR734_circle_center,BR733_circle_center,RATUG_circle_center,BR732_circle_center,BR731_circle_center,BR730_circle_center]
SW = [BR724_circle_center,BR723_circle_center,IBLIR_circle_center,BR722_circle_center,BR721_circle_center,BR720_circle_center]

NW1n = ['BR634','BR633','IRLOB','BR632','BR631','BR630']
NW2n = ['BR634','BR633','IRLOB','BR632','BR631','BR630']
NEn = ['BR624','LUTIV','BR623','BR622','BR621','BR620']
SEn = ['BR734','BR733','RATUG','BR732','BR731','BR730']
SWn = ['BR724','BR723','IBLIR','BR722','BR721','BR720']

if PMsystem == 'NE':
    points = NE
    names = NEn
elif PMsystem == 'NW1':
    points = NW1
    names = NW1n
elif PMsystem == 'NW2':
    points = NW2
    names = NW2n
elif PMsystem == 'SE':
    points = SE
    names = SEn
else:
    points = SW
    names = SWn
    

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
            print('only in '+names[0])
            break
        else:
            print('in none of them')
            continue

if radius == 0.05:
    filename = airport_icao+"_"+PMsystem+"_ARCS.csv"
elif radius == 0.03:
    filename = airport_icao+"_"+PMsystem+"_ARCS_rad03.csv"
PM_usage.to_csv(os.path.join(DATASET_DATA_DIR, filename), sep=' ', encoding='utf-8', float_format='%.3f', index = True, header = False)

