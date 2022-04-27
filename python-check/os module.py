#!/usr/bin/python

import os
from datetime import datetime

#print(dir(os))
print(os.getcwd())
print(os.listdir())
#os.rename('1.py','sample.py')

#print(os.stat('sample.py'))

#print(os.stat('sample.py').st_gid)
# mod_time = os.stat('sample.py').st_mtime
# print(datetime.fromtimestamp(mod_time))

for dirpath,dirnames,filenames in os.walk('/Users/javvaji'):
    print('cureentpath:',dirpath)
    print('directories:',dirnames)
    print('filenames:',filenames)
    print()


