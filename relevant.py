
import pandas as pd
import csv

data = pd.read_csv('data.csv')

text = " Hello DNSserver BGPri"

def nawab_read_list(data):
        search_list = []
        for index, row in data.iterrows():
            search_list.append(row["Proto_list"])
        return (search_list)





def main():
    min_cnt = 3
    query = nawab_read_list(data)
    cnt = 0
    for line in query:
        key = str(line).strip('#')
        if key in text:
            cnt+=1
    print(cnt)
        
if __name__ == "__main__":
    main()