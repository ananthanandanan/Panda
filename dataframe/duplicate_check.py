



def nawab_check_tweet(tweet_id):
    with open("tid_store.txt", "r") as fp:
         if any(line.strip() == tweet_id for line in fp):
             print(True)
             return True
         else:
             print(False)
             return False


if __name__ == "__main__":

    tid = '12312234342435' ##last tid
    nawab_check_tweet(tid)
         
