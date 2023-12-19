import pandas as pd
import matplotlib.pyplot as plt
import os

radius = 0.05

RT1_lat = [60.88889,60.435667,60.281025,60.130306,60.027056,59.91725,59.814444,59.748833,59.973611]
RT2_lat = [60.323611,60.272222,60.130306,60.027056,59.91725,59.814444,59.748833,59.973611]
RT3_lat = [59.327778,59.617417,59.743583,59.822778,59.920528,60.024306,59.973611]
RT4_lat = [61.013889,60.218611,60.067756,59.924861,59.816194,59.721278,59.65125,59.619333,59.925622]
RT5_lat = [60.012711,59.983583,59.924861,59.816194,59.721278,59.65125,59.619333,59.925622]
RT6_lat = [59.183333,59.452194,59.630412,59.665472,59.732583,59.821861,59.925622]
RT7_lat = [60.93475,60.761417,60.724861,60.657833,60.567194,60.466111]
RT8_lat = [60.323611,60.397444,60.465583,60.572944,60.6685,60.739528,60.771639,60.466111]
RT9_lat = [59.327778,59.65925,59.937806,60.147325,60.32775,60.465583,60.572944,60.6685,60.739528,60.771639,60.466111]
RT10_lat = [61.013889,60.819028,60.651194,60.570167,60.471861,60.368222,60.421361]
RT11_lat = [60.012711,60.262611,60.36525,60.474583,60.578,60.644361,60.421361]
RT12_lat = [59.419694,59.9326,60.111083,60.262611,60.36525,60.474583,60.578,60.644361,60.421361]
RT1_lon = [10.473611,10.30525,10.278583,10.252833,10.1785,10.180472,10.256944,10.358917,10.802417]
RT2_lon = [9.383333,9.863889,10.252833,10.1785,10.180472,10.256944,10.358917,10.802417]
RT3_lon = [9.75,10.214361,10.41975,10.285444,10.213278,10.211389,10.802417]
RT4_lon = [12.216667,11.969722,11.853764,11.744972,11.704639,11.595222,11.427306,11.275028,11.11405]
RT5_lon =[12.392347,12.171306,11.744972,11.704639,11.595222,11.427306,11.275028,11.11405]
RT6_lon = [11.315278,11.259556,11.217,11.410528,11.569167,11.67475,11.11405]
RT7_lon = [10.831167,10.977667,10.778139,10.616583,10.510444,11.084444]
RT8_lon = [9.383333,9.926333,10.442389,10.479722,10.590667,10.760528,10.9185,11.084444]
RT9_lon = [9.75,9.935111,10.091722,10.212453,10.3175,10.442389,10.479722,10.590667,10.760528,10.9185,11.084444]
RT10_lon = [12.216667,11.989722,11.7955,11.930556,12.001583,12.000083,11.402722]
RT11_lon = [12.392347,11.954833,12.03375,12.03525,11.9595,11.858472,11.402722]
RT12_lon = [11.464278,11.792175,11.909139,11.954833,12.03375,12.03525,11.9595,11.858472,11.402722]
GM416_lat, GM416_lon = (59.630412,11.217)
GM411_lat, GM411_lon = (59.816194,11.704639)
GM405_lat, GM405_lon = (60.027056,10.1785)
GM410_lat, GM410_lon = (59.743583,10.41975)
GM423_lat, GM423_lon = (60.36525,12.03375)
GM418_lat, GM418_lon = (60.651194,11.7955)
GM429_lat, GM429_lon = (60.572944,10.479722)
GM432_lat, GM432_lon = (60.761417,10.977667)

DATA_DIR = os.path.join('Output', 'PM_dataset.csv')
flightsrwy = pd.read_csv(DATA_DIR, header=None, sep=' ') 
list_col_names = ['ix','flightID', 'sequence', 'timestamp', 'lat', 'lon', 'rawAltitude', 'baroAltitude', 'velocity','endDate', 'date']
flightsrwy.columns = list_col_names


# drop false-positive flights
flightsrwy.drop(flightsrwy[flightsrwy['flightID'] == '221001NOZ4ES'].index, inplace = True)
flightsrwy.drop(flightsrwy[flightsrwy['flightID'] == '221003DLH4LF'].index, inplace = True)
flightsrwy.drop(flightsrwy[flightsrwy['flightID'] == '221026WIF144'].index, inplace = True)
flightsrwy.drop(flightsrwy[flightsrwy['flightID'] == '221020SAS64P'].index, inplace = True)
flightsrwy.drop(flightsrwy[flightsrwy['flightID'] == '221021NOZ1151'].index, inplace = True)
flightsrwy.drop(flightsrwy[flightsrwy['flightID'] == '221022SAS4433'].index, inplace = True)
flightsrwy.drop(flightsrwy[flightsrwy['flightID'] == '221023LBD1'].index, inplace = True)
flightsrwy.drop(flightsrwy[flightsrwy['flightID'] == '221009MDT6'].index, inplace = True)
flightsrwy.drop(flightsrwy[flightsrwy['flightID'] == '221016SAS4047'].index, inplace = True)
flightsrwy.drop(flightsrwy[flightsrwy['flightID'] == '221015NOZ8US'].index, inplace = True)
flightsrwy.drop(flightsrwy[flightsrwy['flightID'] == '221024WIF9BF'].index, inplace = True)
flightsrwy.drop(flightsrwy[flightsrwy['flightID'] == '221024NOZ11G'].index, inplace = True)
flightsrwy.drop(flightsrwy[flightsrwy['flightID'] == '221023N900AJ'].index, inplace = True)
flightsrwy.drop(flightsrwy[flightsrwy['flightID'] == '221013SAS4545'].index, inplace = True)
flightsrwy.drop(flightsrwy[flightsrwy['flightID'] == '221013NOZ6MH'].index, inplace = True)


fig, ax = plt.subplots(figsize=(9,9))
for i, g in flightsrwy.groupby(['flightID','endDate']):
    g.plot(x='lon', y='lat', ax=ax, label=str(i),legend=False,color='gray',alpha=0.4,zorder=1)
circle1  = plt.Circle((GM416_lon, GM416_lat), radius, color='r', linewidth = 1.5,fill = False,zorder=3)
ax.add_patch(circle1)
circle2  = plt.Circle((GM411_lon, GM411_lat), radius, color='r', linewidth = 1.5,fill = False,zorder=3)
ax.add_patch(circle2)
circle3  = plt.Circle((GM405_lon, GM405_lat), radius, color='r', linewidth = 1.5,fill = False,zorder=3)
ax.add_patch(circle3)
circle4  = plt.Circle((GM410_lon, GM410_lat), radius, color='r',linewidth = 1.5, fill = False,zorder=3)
ax.add_patch(circle4)
circle5  = plt.Circle((GM423_lon, GM423_lat), radius, color='r',linewidth = 1.5, fill = False,zorder=3)
ax.add_patch(circle5)
circle6  = plt.Circle((GM418_lon, GM418_lat), radius, color='r',linewidth = 1.5, fill = False,zorder=3)
ax.add_patch(circle6)
circle7  = plt.Circle((GM429_lon, GM429_lat), radius, color='r',linewidth = 1.5, fill = False,zorder=3)
ax.add_patch(circle7)
circle8  = plt.Circle((GM432_lon, GM432_lat), radius, color='r',linewidth = 1.5, fill = False,zorder=3)
ax.add_patch(circle8)
#plot2 = plt.plot(RT1_lon, RT1_lat,linewidth=1.5,color = 'black',zorder=2)
plot3 = plt.plot(RT2_lon, RT2_lat,linewidth=1.5,color = 'black',zorder=2)
plot4 = plt.plot(RT3_lon, RT3_lat,linewidth=1.5,color = 'black',zorder=2)
plot5 = plt.plot(RT4_lon, RT4_lat,linewidth=1.5,color = 'black',zorder=2)
plot6 = plt.plot(RT5_lon, RT5_lat,linewidth=1.5,color = 'black',zorder=2)
plot7 = plt.plot(RT6_lon, RT6_lat,linewidth=1.5,color = 'black',zorder=2)
plot8 = plt.plot(RT7_lon, RT7_lat,linewidth=1.5,color = 'black',zorder=2)
plot9 = plt.plot(RT8_lon, RT8_lat,linewidth=1.5,color = 'black',zorder=2)
plot10 = plt.plot(RT9_lon, RT9_lat,linewidth=1.5,color = 'black',zorder=2)
plot11 = plt.plot(RT10_lon, RT10_lat,linewidth=1.5,color = 'black',zorder=2)
plot12 = plt.plot(RT11_lon, RT11_lat,linewidth=1.5,color = 'black',zorder=2)
#plot13 = plt.plot(RT12_lon, RT12_lat,linewidth=1.5,color = 'black',zorder=2)
# axes = plt.gca()
# axes.legend().set_visible(False)
ax.set_xlim([10.42,11.3])                                                               #setting limits for axes
ax.set_ylim([60.15,61])
ax.set(xlabel=None)
ax.grid()
plt.xticks(fontsize=16)
plt.yticks(fontsize=16)
plt.show()
