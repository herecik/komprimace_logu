import os
import gzip
import shutil

#Declare a path to log files
path = "var/log/"
#load contents of log direcotory
files = os.listdir(path)

for i in files:
    if not os.path.isdir(path + i):
        #open original file to read and create new compressed file
        f_original = open(path + i, 'rb')
        f_compressed = gzip.open(path + i + ".gz", 'wb')
        #copy from original to compressed 
        shutil.copyfileobj(f_original, f_compressed)
        #close both files
        f_original.close()
        f_compressed.close()
        #remove non-compressed files
        os.remove(path + i)
