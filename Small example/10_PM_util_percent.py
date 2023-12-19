import pandas as pd
import os

for dat in ['NW','NW','SW','SE']:
    data_dir = os.path.join('Output', 'ENGM_'+dat+'_ARCS.csv')
    flights1 = pd.read_csv(data_dir,header=None,sep=' ') 
    list_col_names = ['x','s','flightID','last_star']
    flights1.columns = list_col_names
    flights1 = flights1.drop(['s'], axis=1)
    PMus = flights1.copy()
    
    # last starts
    fourth_st = ['GM407','GM455','GM414','GM454','GM453','GM421','GM435','GM452']
    third_st = ['GM408','GM404','GM415','GM412','GM425','GM420','GM434','GM431']
    second_st = ['GM409','GM406','GM417','GM413','GM424','GM419','GM433','GM430']
    first_st = ['GM410','GM405','GM416','GM411','GM423','GM418','GM432','GM429']
    
    hundred = PMus[PMus['last_star'].isin(fourth_st)]
    seventy_five = PMus[PMus['last_star'].isin(third_st)]
    twenty_five = PMus[PMus['last_star'].isin(second_st)]
    zero = PMus[PMus['last_star'].isin(first_st)]
    
    percent_100 = (len(hundred)/len(PMus))*100
    percent_75 = (len(seventy_five)/len(PMus))*100
    percent_25 = (len(twenty_five)/len(PMus))*100
    percent_0 = (len(zero)/len(PMus))*100 
    
    print('RESULTS FOR ',dat)
    print('---------------------')
    print('Whole PM ',percent_100)
    print('PM 75% ',percent_75)
    print('PM 25% ',percent_25)
    print('PM only start ',percent_0)   
    print('Number of aircraft: ',PMus['flightID'].nunique())    
    
