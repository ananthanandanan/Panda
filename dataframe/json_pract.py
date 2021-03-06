
import json
import pandas as pd
import time
import csv
import os




if not os.path.isfile('samples.csv'):
    with open('samples.csv', 'w') as f:
        Headers = ['Datetime', 'Id']
        writer = csv.writer(f)
        writer.writerow(Headers)
        

dicts = { 'Datetime' : [time.strftime("%m/%d/%Y %I:%M:%S %p ")],
                'Id': [str(3212232334)]}
    
data = pd.DataFrame(dicts)
data.to_csv('samples.csv',mode='a',header=False, index=False)
sample = pd.read_csv('samples.csv')
print(sample)




 
