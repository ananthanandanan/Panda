
import pandas as pd
import csv

data = pd.read_csv('data.csv')

text = "A newly discovered #DNS protocol vulnerability affecting ALL recursive DNS resolvers. It allows a random subdomain… https://t.co/ooAIhv wn1e"

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
            
            cnt+=text.count(key)
    print(cnt)
        
if __name__ == "__main__":
    main()