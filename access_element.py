# importing pandas package
import pandas as pd
 
# making data frame from csv file also indexed column will be left most and search related
data = pd.read_csv("nba.csv")

ser = pd.Series(data['Name'])

for i in range(5):
    print(ser[i])

