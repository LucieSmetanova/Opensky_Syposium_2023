import pandas as pd
import os
import pyproj

from shapely.geometry import Point
from shapely.geometry import LineString

from datetime import datetime
import calendar

import time
start_time = time.time()

year = '2022'
airport_icao = "ENGM"
months = ['10']

#airport_icao = "ENGM"
TMA_lon=[9.59556, 11.7944, 11.8494, 12.0989, 12.3611, 12.3394, 12.3417, 12.2917, 11.8292, 11.6958, 11.0722, 10.95, 10.5583, 10.1, 9.59556];
TMA_lat=[59.7097, 59.3667, 59.8333, 59.8906, 60.2236, 60.4039, 60.5, 60.7125, 60.875, 60.7972, 60.8778, 60.9389, 60.925, 60.7292, 59.7097];

# Runway 01L
rwy01L_lat=[60.185, 60.216067];
rwy01L_lon=[11.073744, 11.091664];
# Runway 19R
rwy19R_lat=[60.216067, 60.185];
rwy19R_lon=[11.091664, 11.073744];
# Runway 01R
rwy01R_lat = [60.175756, 60.201208];
rwy01R_lon = [11.107783, 11.122486];
# Runway 19L
rwy19L_lat = [60.201208, 60.175756];
rwy19L_lon = [11.122486, 11.107783];



geod = pyproj.Geod(ellps='WGS84')   # to determine runways via azimuth
#fwd_azimuth, back_azimuth, distance = geod.inv(lat1, long1, lat2, long2)
rwy01LR_azimuth, rwy01LL_azimuth, distance = geod.inv(rwy01L_lon[0], rwy01L_lat[0], rwy01L_lon[1], rwy01L_lat[1])
rwy19RR_azimuth, rwy19RL_azimuth, distance = geod.inv(rwy19R_lon[0], rwy19R_lat[0], rwy19R_lon[1], rwy19R_lat[1])
rwy01RR_azimuth, rwy01RL_azimuth, distance = geod.inv(rwy01R_lon[0], rwy01R_lat[0], rwy01R_lon[1], rwy01R_lat[1])
rwy19LR_azimuth, rwy19LL_azimuth, distance = geod.inv(rwy19L_lon[0], rwy19L_lat[0], rwy19L_lon[1], rwy19L_lat[1])

print(rwy01LR_azimuth, rwy01LL_azimuth)
print(rwy19RR_azimuth, rwy19RL_azimuth)
print(rwy01RR_azimuth, rwy01RL_azimuth)
print(rwy19LR_azimuth, rwy19LL_azimuth)


#point1 = [59.537, 17.9]
#point2 = [59.766, 17.98]
#fwd_azimuth, back_azimuth, distance = geod.inv(point1[0], point1[1], point2[0], point2[1])
#print(fwd_azimuth, back_azimuth)

#Point1 = Point(point1[1], point1[0])
#Point2 = Point(point2[1], point2[0])

a = (rwy01L_lon[0], rwy01L_lat[0])
b = (rwy01L_lon[1], rwy01L_lat[1])
# distance between runways - 2 km
offset_length = 0.018 #approximate 1 km in longitude degrees, when latitude is 60N

ab = LineString([a, b])
cd = ab.parallel_offset(offset_length)
# Point1 = cd.boundary[0]
# Point2 = cd.boundary[1]
Point1 = Point(cd.coords[0])
Point2 = Point(cd.coords[1])

print(Point1, Point2)


# Check the sign of the determninant of 
# | x2-x1  x3-x1 |
# | y2-y1  y3-y1 |
# It will be positive for points on one side, and negative on the other (0 on the line)
def is_left(Point3):
    if ((Point2.x - Point1.x)*(Point3.y - Point1.y) - (Point2.y - Point1.y)*(Point3.x - Point1.x)) < 0:
        return True
    else:
        return False


def get_all_states(csv_input_file):

    df = pd.read_csv(csv_input_file, sep=' ',
                    names = ['flightId', 'sequence', 'timestamp', 'lat', 'lon', 'rawAltitude', 'altitude', 'velocity', 'beginDate', 'endDate'],
                    dtype={'flightId':str, 'sequence':int, 'timestamp':int, 'lat':float, 'lon':float, 'rawAltitude':int, 'altitude':float, 'velocity':float, 'beginDate':str, 'endDate':str})
    
    df.set_index(['flightId', 'sequence'], inplace=True)
    
    return df


def determine_runways(month, week):
    
    input_filename = "osn_arrival_"+ airport_icao + "_states_50NM_" + year + '_' + month + "_week" + str(week) + ".csv"
    full_input_filename = os.path.join('Input', input_filename)

    output_filename = "runways_" + year + '_' +  month + "_week" + str(week) + ".csv"
    full_output_filename = os.path.join('Output', output_filename)

    states_df = get_all_states(full_input_filename)
    
    number_of_flights = len(states_df.groupby(level='flightId'))
    print(number_of_flights)
        
    runways_df = pd.DataFrame(columns=['flight_id', 'date', 'hour', 'runway'])
    
    flight_id_num = len(states_df.groupby(level='flightId'))

    count = 0
    for flight_id, flight_id_group in states_df.groupby(level='flightId'):
        
        count = count + 1
        print(airport_icao, year, month, week, flight_id_num, count, flight_id)

        date_str = states_df.loc[flight_id].head(1)['endDate'].values[0]
        
        end_timestamp = states_df.loc[flight_id]['timestamp'].values[-1]
        end_datetime = datetime.utcfromtimestamp(end_timestamp)
        end_hour_str = end_datetime.strftime('%H')
        
        
        # Determine Runway based on lat, lon
        
        runway = ""
        trajectory_point_last = [flight_id_group['lat'][-1], flight_id_group['lon'][-1]]
        # 30 seconds before:
        trajectory_point_before_last = [flight_id_group['lat'][-30], flight_id_group['lon'][-30]]
        
        #fwd_azimuth, back_azimuth, distance = geod.inv(lat1, long1, lat2, long2)
        trajectory_azimuth, temp1, temp2 = geod.inv(trajectory_point_before_last[1],
                                                    trajectory_point_before_last[0],
                                                    trajectory_point_last[1],
                                                    trajectory_point_last[0])

        if (trajectory_azimuth > -90) and (trajectory_azimuth < 90):
            Point3 = Point(trajectory_point_last[1], trajectory_point_last[0])
            if is_left(Point3):
                runway = '01L'
            else:
                runway = '01R'
        else: # 19L or 19R
            Point3 = Point(trajectory_point_last[1], trajectory_point_last[0])
            if is_left(Point3):
                runway = '19R'
            else:
                runway = '19L'
        xx = pd.DataFrame({'flight_id': flight_id, 'date': date_str,
                                        'hour': end_hour_str,
                                        'runway': runway}, index=[0]) 
        runways_df = pd.concat([runways_df,xx],ignore_index=True)
    runways_df.to_csv(full_output_filename, sep=' ', encoding='utf-8', float_format='%.3f', header=True, index=False)

def create_runways_files(month, week):
    
    input_filename1 = "osn_arrival_"+ airport_icao + "_states_50NM_" + year + '_' + month + "_week" + str(week) + ".csv"
    full_input_filename1 = os.path.join('Input', input_filename1)
    
    states_df = get_all_states(full_input_filename1)
    
    number_of_flights = len(states_df.groupby(level='flightId'))
    
    input_filename2 = "runways_" + year + '_' +  month + "_week" + str(week) + ".csv"
    full_input_filename2 = os.path.join('Output', input_filename2)
    
    runways_df = pd.read_csv(full_input_filename2, sep=' ')
    runways_df.set_index(['flight_id'], inplace=True)

    rwy01L_df = pd.DataFrame()
    rwy19R_df = pd.DataFrame()
    rwy01R_df = pd.DataFrame()
    rwy19L_df = pd.DataFrame()

    
    count = 0
    for flight_id, flight_id_group in states_df.groupby(level='flightId'):
        count = count + 1
        print(airport_icao, year, month, week, number_of_flights, count, flight_id)

        runway = runways_df.loc[flight_id][['runway']].values[0]
        if runway == "01L":
            flight_id_gr = flight_id_group.reset_index()
            rwy01L_df = pd.concat([rwy01L_df,flight_id_gr],ignore_index=True)
        elif runway == "19R":
            flight_id_gr = flight_id_group.reset_index()
            rwy19R_df = pd.concat([rwy19R_df,flight_id_gr],ignore_index=True)
        elif runway == "01R":
            flight_id_gr = flight_id_group.reset_index()
            rwy01R_df = pd.concat([rwy01R_df,flight_id_gr],ignore_index=True)
        elif runway == "19L":
            flight_id_gr = flight_id_group.reset_index()
            rwy19L_df = pd.concat([rwy19L_df,flight_id_gr],ignore_index=True)


    output_filename = "osn_"+ airport_icao + "_states_50NM_" + year + '_' + month + "_week" + str(week)
    full_output_filename = os.path.join('Output', output_filename)

    rwy01L_df.to_csv(full_output_filename + "_rwy01L.csv", sep=' ', encoding='utf-8', float_format='%.3f', index = True, header = False)
    rwy19R_df.to_csv(full_output_filename + "_rwy19R.csv", sep=' ', encoding='utf-8', float_format='%.3f', index = True, header = False)
    rwy01R_df.to_csv(full_output_filename + "_rwy01R.csv", sep=' ', encoding='utf-8', float_format='%.3f', index = True, header = False)
    rwy19L_df.to_csv(full_output_filename + "_rwy19L.csv", sep=' ', encoding='utf-8', float_format='%.3f', index = True, header = False)
  
    
def main():
    
    for month in months:
        number_of_weeks = (1, 1)[month == '02' and not calendar.isleap(int(year))]
        #number_of_weeks = 1
        
        for week in range(0, number_of_weeks):
        #for week in range(1, number_of_weeks):
        
            determine_runways(month, week+1)
                       
            create_runways_files(month, week+1)
    
    
main()    

print("--- %s minutes ---" % ((time.time() - start_time)/60))