#!/usr/bin/env python
# -*- coding:utf-8 -*-

### (2) mod doc ###
"""This is a mod doc"""

### (3) import  ###
import time
import os

source = ['/home/aa', '/home/bb']
target_dir = ['/home/linyd/python/backup']

today = target_dir + time.strftime('%Y%m%d')
print 'today is ', today
now = time.strftime('%H%M%S')
print 'now is ', now

if not os.path.exists(today):
    os.mkdir(today)
    print 'successfully created directory', today

target = today + os.sep + now + '.zip'
print 'target is ', target

zip_command = "zip -qr '%s' %s" % (target, ' '.join(source))

if os.system(zip_command) == 0:
    print 'successful backup to', target
else:
    print 'backup failed'
