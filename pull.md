 Added a new tweet storage file -tid_store.csv for better access. 
- Removed a strip() which were not required anymore. 
- Used the writer() for writing on to the .csv file. 
- Used Series() in pandas to iterate through the specified column.
1. writing to file
```python
with open("tid_store.csv","a") as fp: ##nawab_store_id()
        append=csv.writer(fp)
        store_list = ['',tweet_id]
        append.writerow(store_list)
```
- The above code opens up the tid_store.csv on append mode to store the tweet id. 
And to append the tweet_id to file, the tweet id were stored as list. 
- Using the csv method writerow() tweet will be stored in file.
2. Reading and searching the file
```python
def nawab_get_blacklist():
    ser = pd.Series(data['Blacklist'])
    for line in ser:
        if "#DO_NOT_REMOVE_THIS_LINE#" not in str(line):
            banned_accs.append(line)
```
- To read and search the file, Series() method of pandas is used. Using this method a specified column can be iterated over. Here all the blacklisted data is stored to the banned_access array.

3.
```python
def nawab_check_tweet(tweet_id):
    ser = pd.Series(tid['id'])
    for i in ser:
        if i == tweet_id:
            return True
    return False
```
- Here when the check_tweet()  is called, it will iterate through and check if the tweet_id is a stored tweet or not.