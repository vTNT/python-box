#!/usr/bin/env python
# -*- coding:utf-8 -*-

### (2) mod doc ###
"""This is loadavg scripts"""

def load_stat():
    loadavg = {}
    f = open("/proc/loadavg")
    con = f.readline().split()
    f.close()
    loadavg['lavg_1']   = con[0]
    loadavg['lavg_5']   = con[1]
    loadavg['lavg_15']  = con[2]
    loadavg['nr']       = con[3]
    loadavg['last_pid'] = con[4]

    return loadavg

### (7) main    ###
if __name__ == '__main__':
    load = load_stat()
    print load.keys()
    print load.values()
    sql= "inseret into %s (%s) values (%s)" % ("t",",".join([k for k in load.keys()]),",".join([v for v in load.values()])) 
    print sql
