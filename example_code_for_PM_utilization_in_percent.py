import pandas as pd

flights1 = pd.read_csv('ARCS_dat.csv', 
header=None,
sep=' '
) 
list_col_names = ['s','flightID','last_star']
flights1.columns = list_col_names
flights1 = flights1.drop(['s'], axis=1)


# last starts
sixth_st = ['DW866']
fifth_st = ['DW816','DW706','DW755','DW865']
fourth_st = ['DW754','APRUT','DW705','DW815']
third_st = ['DW704','DW814','ADNAL','BIVDI']
second_st = ['AKIVA','BABON','KUDOM','SUGAD']
first_st = ['SIVNA','KOGAX','ASDER','BERMO']

NWn = ['ASDER','AKIVA','ADNAL','APRUT','DW865','DW866']
SWn = ['BERMO','BABON','BIVDI','DW754','DW755']
En = ['KOGAX','KUDOM','DW814','DW815','DW816','SIVNA','SUGAD','DW705','DW704','DW706']
SW = PMus[PMus['last_star'].isin(SWn)]
SW.name = 'SW'
E = PMus[PMus['last_star'].isin(En)]
E.name = 'E'
NW = PMus[PMus['last_star'].isin(NWn)]
norm = PMus[~PMus['last_star'].isin(NWn)]
norm.name = 'ALL'

if not problem.empty:
    hundred = NW[NW['last_star'].isin(sixth_st)]
    eighty = NW[NW['last_star'].isin(fifth_st)]
    sixty = NW[NW['last_star'].isin(fourth_st)]
    fourty = NW[NW['last_star'].isin(third_st)]
    twenty = NW[NW['last_star'].isin(second_st)]
    zero = NW[NW['last_star'].isin(first_st)]
    percent_100 = (len(hundred)/len(problem))*100
    percent_80 = (len(eighty)/len(problem))*100
    percent_60 = (len(sixty)/len(problem))*100
    percent_40 = (len(fourty)/len(problem))*100 
    percent_20 = (len(twenty)/len(problem))*100 
    percent_0 = (len(zero)/len(problem))*100 
    print('ARC WEST NORTH:')
    print('Whole PM ',percent_100)
    print('PM 80% ',percent_80)
    print('PM 60% ',percent_60)
    print('PM 40% ',percent_40)
    print('PM 20% ',percent_20)
    print('PM only start ',percent_0)   
    print('Number of aircraft: ',NW['flightID'].nunique())    

for pm in [norm,E,SW]:
    if len(pm) == 0:
        continue
    hundred = pm[pm['last_star'].isin(fifth_st)]
    seventy_five = pm[pm['last_star'].isin(fourth_st)]
    fifty = pm[pm['last_star'].isin(third_st)]
    twenty_five = pm[pm['last_star'].isin(second_st)]
    zero = pm[pm['last_star'].isin(first_st)]
    percent_100 = (len(hundred)/len(pm))*100
    percent_75 = (len(seventy_five)/len(pm))*100
    percent_50 = (len(fifty)/len(pm))*100
    percent_25 = (len(twenty_five)/len(pm))*100
    percent_0 = (len(zero)/len(pm))*100 
    print('_________________')
    print('ARCS '+pm.name)
    print('Whole PM ',percent_100)
    print('PM 75% ',percent_75)
    print('PM 50% ',percent_50)
    print('PM 25% ',percent_25)
    print('PM only start ',percent_0)   
    print('Number of aircraft: ',pm['flightID'].nunique())    
    
