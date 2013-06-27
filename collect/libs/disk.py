#!/usr/bin/env python
# -*- coding:utf-8 -*-

### (2) mod doc ###
"""This is a mod doc"""

### (3) import  ###

### (6) func    ###
def disk_stat():
    import os
    hd = {}
    disk = os.statvfs("/")
    hd['available'] = round((disk.f_bsize * disk.f_bavail) / (1024 * 1024) ,3)
    hd['capacity'] = round((disk.f_bsize * disk.f_blocks) / (1024 * 1024),3)
    hd['used'] = round((disk.f_bsize * disk.f_bfree) / (1024 * 1024 ) ,3)
    return hd

### (7) main    ###
if __name__ == '__main__':
    disk = disk_stat()
    print disk
    #print "Total\tavail\tused"
    #print "%sM\t%sM\t%sM" % (disk['capacity'],disk['available'],disk['used'])
            
