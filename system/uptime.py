#!/usr/bin/env python
# -*- coding:utf-8 -*-

### (2) mod doc ###
"""This is a check uptime scripts"""

def uptime_stat():
    uptime = {}
    f = open("/proc/uptime")
    con = f.readline().split()
    f.close()

    all_sec = float(con[0])
    MINUTE,HOUR,DAY = 60,3600,86400
    uptime['day'] = int(all_sec / DAY)
    uptime['hour'] = int((all_sec % DAY) / HOUR)
    uptime['minute'] = int((all_sec %HOUR) / MINUTE)
    uptime['second'] = int(all_sec %MINUTE)
    uptime['Free rate'] = round((float(con[1]) / (float(con[0]) * 4 )),3)
    #print uptime['Free rate']

    return uptime

### (7) main    ###
if __name__ == '__main__':
    time = uptime_stat()
    #print time
    #print "%0.3f" % time['Free rate']
    print "day\thour\tminute\tidle"
    print "%s\t%s\t%s\t%s%%" % (time['day'],time['hour'],time['minute'],time['Free rate'] * 100)

