import argparse
import os 
import pwd
import logging
import logging.handlers





    
def main():
    
    # default directory
    default_dir = '/var/tmp/'
    # initialise the parser
    """parser = argparse.ArgumentParser(description="Writing to text file")
    
    # add arguments
    parser.add_argument('file',type=str, 
                         help="file to store the text")
    parser.add_argument('text',type=str, 
                         help="the text to be written in file")
    parser.add_argument('--path', type=str
                        , help= 'paste path to desired directory')
    
   # parser.add_argument('-path', type=dir_path)
    #parse arg 
    
    args = vars(parser.parse_args())
    ## To check if new_path is passed
    
    if(args['path']):
        default_dir = args['path']"""
    

    if not os.path.exists(default_dir):
        os.system(("mkdir %s" % (default_dir)))


    logger = logging.getLogger('myapp')
    hdlr = logging.FileHandler(default_dir + 'myapp.log')
    formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
    hdlr.setFormatter(formatter)
    logger.addHandler(hdlr) 
    logger.setLevel(logging.WARNING)
   
    logger.error('We have a problem')
    logger.info('While this is just chatty')
   

    

if __name__ == "__main__":
    
    main()
    
    ##parser.add_argument('path', option = os.chdir(input("paste here path to biog.txt file:")), help= 'paste path to biog.txt file')
    
    
    