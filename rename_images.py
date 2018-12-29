from os import listdir, rename, makedirs
from os.path import isfile, join, exists
import re
import sys

if len(sys.argv) != 3:
        print("ERROR - you must supply the block symbol and correct directory.")
else:
        path = sys.argv[2]
        blockSymbol = sys.argv[1]

        files = [f for f in listdir(path) if isfile(join(path,f))]
        print("FOUND %s FILES"%(len(files)))
        for f in files:
                fileParts = f.split('.')
                renamed = "%s%s.%s" % (fileParts[0], blockSymbol, fileParts[1])
                print("RENAME: %s - %s"%(f, renamed))   
                rename(join(path,f),join(path,renamed))