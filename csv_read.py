# importing pandas package
import pandas as pd
 
# making data frame from csv file also indexed column will be left most and search related
data = pd.read_csv("data.csv")
 
# retrieving row by loc method

last = data['Blacklist'].iloc[-1]

for index, Proto_list in data.iterrows():
     print(Proto_list['Proto_list'])