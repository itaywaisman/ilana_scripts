from os import listdir, rename
from os.path import isfile, join
import re

path = "E:/EEG data Analysis/A7/1st and 2nd steps-Header/1 st step/Raw"
files = [f for f in listdir(path) if isfile(join(path,f))]

for f in files:
    fileParts = f.split('.')
    nameParts = fileParts[0].split('_')
    if re.search('[a-zA-Z]', nameParts[1]) is None:
        renamed = "%s_%s_%s.%s" % (nameParts[0], nameParts[2], nameParts[1], fileParts[1])       
        rename(join(path,f),join(path,renamed))