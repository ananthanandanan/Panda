import argparse
import os 








def writn(filename,texts):
    print("writing to {}".format(filename))
    
    fp =  open(filename,'w')
    
    fp.write(texts)
    
def main():
    
    # default directory
    ##def_dir = 'var/log'
    """if not os.path.exists(def_dir):
        os.makedirs(def_dir)
        os.chdir(def_dir)"""
    
    
    # initialise the parser
    parser = argparse.ArgumentParser(
        description="Writing to text file"
    )
    
    # add arguments
    parser.add_argument('file',type=str, 
                         help="file to store the text")
    parser.add_argument('text',type=str, 
                         help="the text to be written in file")
    parser.add_argument('--path', action='store', default='/var/log'
                        , help= 'paste path to desired directory')
    
   # parser.add_argument('-path', type=dir_path)
    #parse arg 
    
    args = vars(parser.parse_args())
    ## To check if new_path is passed
    path = args['path']
    if not os.path.exists(path):
        os.makedirs(path)
        os.chdir(path)
    os.chdir(path)
    

    writn(args['file'], args['text'])

if __name__ == "__main__":
    
    main()
    
    ##parser.add_argument('path', option = os.chdir(input("paste here path to biog.txt file:")), help= 'paste path to biog.txt file')
    
    
    