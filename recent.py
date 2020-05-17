
from datetime import timedelta, datetime
import pandas as pd


data = pd.read_csv('samples.csv')

prev_date = datetime.now()
prev_date = prev_date - timedelta(days=1)
prev = prev_date.strftime("%m/%d/%Y %H:%M:%S %p")
prev = datetime.strptime(prev,"%m/%d/%Y %H:%M:%S %p")
for index, tid_store in data.iterrows():
    tid_date = (datetime.strptime((tid_store['Datetime']).strip(), '%m/%d/%Y %H:%M:%S %p'))
    if tid_date.date() >= prev.date():
          print("correct")
          
