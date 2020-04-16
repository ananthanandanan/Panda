# importing pandas package
import pandas as pd
import config 
import csv
 
# making data frame from csv file also indexed column will be left most and search related
data = pd.read_csv("nawab.csv")

ser = pd.Series(data['id'])

for i in ser:
    print(int(i))
tweet = 1233423442   
name = str(tweet) 

    
with open('nawab.csv', 'a') as f:
    append=csv.writer(f)
    append.writerow(name)
    
print("success")