#!/usr/bin/env python
# -*- coding:utf-8 -*-
import cpu
import disk
import load
import mem
import uptime

def status():
    c = cpu.cpu_stat()
    print "\033[1;32;40m%s\033[0m" % "CPU:"
    print "\tthe core number is  %s " % c[0]
    print "\tthe core name   is %s " % c[2]['model name']

    dd = disk.disk_stat()
    #print time
    #print "%0.3f" % time['Free rate']
    print "\033[1;32;40m%s\033[0m" % "disk:"
    print "\tTotal\tavail\tused"
    print "\t%sM\t%sM\t%sM" % (dd['capacity'],dd['available'],dd['used'])

    memn = mem.memory_stat()
    print "\033[1;32;40m%s\033[0m" % "mem:"
    print "\tthe total is %s Mb" % memn['MemTotal']
    print "\tthe free is %s Mb" % memn['MemFree']
    print "\tthe used is %s Mb" % memn['Memused']

    loadd = load.load_stat()
    print "\033[1;32;40m%s\033[0m" % "load:"
    print "\tthe 1  min  load is %s " % loadd['lavg_1']
    print "\tthe 5  min  load is %s " % loadd['lavg_5']
    print "\tthe 15 min  load is %s " % loadd['lavg_15']

    time = uptime.uptime_stat()
    print "\033[1;32;40m%s\033[0m" % "uptime:"
    print "\tday\thour\tminute\tidle"
    print "\t%s\t%s\t%s\t%s%%" % (time['day'],time['hour'],time['minute'],time['Free rate'] * 100)

if __name__ == '__main__':
    status()
