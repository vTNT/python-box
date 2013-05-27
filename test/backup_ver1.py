#!/usr/bin/env python
# -*- coding:utf-8 -*-

### (2) mod doc ###
"""This is a mod doc"""

### (3) import  ###
import os
import time

source = ['/home/xx', '/home/bb']
target_dir = '/home/cc'
target = target_dir + time.strftime('%Y%m%d%H%M%S') + '.zip'

print time.strftime('%Y_%m_%d_%H_%M_%S')
print '%s ' % (' '.join(source))
zip_command = "zip -qr '%s' %s" % (target, ' '.join(source))

if os.system(zip_command) == 0:
    print 'successful backup to', target
else:
    print 'backup failed'

