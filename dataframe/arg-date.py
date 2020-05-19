import argparse
import datetime
import pandas as pd

parser = argparse.ArgumentParser()
parser.add_argument('-d','--date', type=lambda s: datetime.datetime.strptime(s, '%m/%d/%Y %H:%M:%S'))  # For testing.  Pass no arguments in production
args = vars(parser.parse_args())
date = args['date']
new_Date = date.date()

data = pd.read_csv('samples.csv')

for index, Date in data.iterrows():
    
    tid_date = datetime.datetime.strptime((Date['Datetime']).strip(), '%m/%d/%Y %H:%M:%S %p')
    
    print(tid_date.time())
   