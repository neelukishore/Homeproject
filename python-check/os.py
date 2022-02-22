#/usr/bin/python

import os
from datetime import datetime

#print(dir(os))
print(os.listdir())
print(os.getcwd())
print(os.environ.get('HOME'))
print(os.stat('second.sh'))
mod_time=os.stat('second.sh').st_mtime
print(datetime.fromtimestamp(mod_time))
print(os.stat('second.sh').st_size)

