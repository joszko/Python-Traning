"""
Merging text files in one directory into one file with name containing timestamp

glob 2 is generating a list of files with a given criteria
with open(... - no need to closing the file after the operation

"""

import glob2
import datetime

textfiles = glob2.glob('*txt')

with open(datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S-%f")+".txt", 'w') as file:
    for filename in textfiles:
        with open(filename,"r") as sourcefile:
            file.write(sourcefile.read()+'\n')