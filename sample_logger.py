import argparse
import os 
import pwd
import logging
import logging.handlers




def hello(Path,hi=None):
    print(hi,Path)
    
def main():
    
    # default directory
    default_dir = '/var/tmp/'
    # initialise the parser
    parser = argparse.ArgumentParser(description="Writing to text file")
    
    # add arguments
    parser.add_argument("-p", "--path", type=str, required=False,
                        help="Path where the log files be stored. Note to create directory in that path beforehand.")
    parser.add_argument('-d', '--default', action="store_const", const=30)
   # parser.add_argument('-path', type=dir_path)
    #parse arg 
    parser.add_argument("-r", "--retweet", help="Retweet all tweets automatically, doesn't spawn a telegram bot",
                        action='store_true', required=False) 
    args = vars(parser.parse_args())
    ## To check if new_path is passed
    if args['default']:
        print(args['default'])
    hello(args['path'],args['retweet'])
    

    
   

    

if __name__ == "__main__":
    
    main()
    
    """try:
            last_id = self.nawab_get_id()
        except FileNotFoundError as e:
            self.nw_logger.logger(
                '|No tweet id found, hence assuming no file created and therefore creating the new file ', 'error', 'Error')
            f = open(self.dirpath + "tid_store.csv", "w+")
            last_id = None"""
    