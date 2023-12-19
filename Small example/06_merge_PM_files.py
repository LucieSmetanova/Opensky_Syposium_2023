import pandas as pd
import glob
import os

airp = 'ENGM'
month = '10'


full_input_filename = os.path.join('Output', 'PM_dataset_*.csv')
files = glob.glob(full_input_filename)

countU = 0
lenU = 0
PM_dat = pd.DataFrame()
for file in files:
    df = pd.read_csv(file, sep = ' ',header = None,index_col=None)
    countU += df[:][0].nunique()
    lenU += len(df)
    PM_dat = pd.concat([PM_dat,df],ignore_index=True)
    
full_output_filename = os.path.join('Output', 'PM_dataset.csv')
PM_dat.to_csv(full_output_filename, sep=' ', encoding='utf-8', float_format='%.3f', index = True, header = False)
