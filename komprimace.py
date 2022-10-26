import os
import gzip
import shutil

#Declare a path to log files
PATH = "var/log/"
#First two bytes in gzip
GZIP_NUMBER = b'\x1f\x8b'
#Load contents of log direcotory
files = os.listdir(PATH)

#counter used for debugging. Uncomment to use 
#cnt = 0

def is_gzip(file_name):
    """ 
    Function that checks if a file is already gzipped
    Opens the file and checks first two bytes, then compares them with expected bytes that are always at the begining of gzip
    
    Args:
        file_name (str): Name of the checked file
    Returns:
        float: Ture if first two bytes from opened file are equals to GZIP_NUMBER
    """
    f = open(file_name, 'rb')
    read = f.read(2)
    f.close()
    return read == GZIP_NUMBER

for i in files:
    """ 
    Loop checks every item in the list "files"
    Item can't be a directory and it can't be a gzip
    Gzip file is created, then the content from original log file is copied to the new gzip file and compressed
    At the end of each iteration, loop removes original uncompressed log file
    """
    file_path = PATH + i
    
    if not os.path.isdir(file_path) and not is_gzip(file_path):
        
        #open original file to read and create new compressed file
        f_original = open(file_path, 'rb')
        f_compressed = gzip.open(file_path + ".gz", 'wb')
        
        #copy from original to compressed 
        shutil.copyfileobj(f_original, f_compressed)
        
        #close both files
        f_original.close()
        f_compressed.close()
        
        #remove non-compressed files
        os.remove(file_path)
        #Uncomment cnt to use for debugging
        #cnt += 1
        
#Message for debugging, counting files that have been compressed. Uncomment to use  
#print("Debug: Total of " + str(cnt) + " files were compressed")
