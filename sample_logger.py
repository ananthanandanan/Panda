import argparse
import os 
import pwd
import logging
import logging.handlers




def hello(hi=False):
    print(hi)
    
def main():
    
    # default directory
    default_dir = '/var/tmp/'
    # initialise the parser
    parser = argparse.ArgumentParser(description="Writing to text file")
    
    # add arguments
    parser.add_argument('-d', '--default', action="store_const", const=30)
   # parser.add_argument('-path', type=dir_path)
    #parse arg 
    parser.add_argument("-r", "--retweet", help="Retweet all tweets automatically, doesn't spawn a telegram bot",
                        action='store_true', required=False) 
    args = vars(parser.parse_args())
    ## To check if new_path is passed
    if args['default']:
        print(args['default'])
    hello(args['retweet'])
    

    
   

    

if __name__ == "__main__":
    
    main()
    
    ##parser.add_argument('path', option = os.chdir(input("paste here path to biog.txt file:")), help= 'paste path to biog.txt file')
    
    
    