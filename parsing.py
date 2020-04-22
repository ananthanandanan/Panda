import argparse
import os 







def writn(filename,texts):
    print("writing to {}".format(filename))
    
    fp =  open(filename,'w')
    
    fp.write(texts)
    
def main():
    # initialise the parser
    parser = argparse.ArgumentParser(
        description="Writing to text file"
    )
    
    # add arguments
    parser.add_argument('file',type=str, 
                         help="file to store the text")
    parser.add_argument('text',type=str, 
                         help="the text to be written in file")
    parser.add_argument('path', type=str 
                       , help= 'paste path to desired directory')
    
   # parser.add_argument('-path', type=dir_path)
    #parse arg 
    
    args = vars(parser.parse_args())
    os.chdir(args['path'])
    writn(args['file'], args['text'])

if __name__ == "__main__":
    
    main()
    
    
    