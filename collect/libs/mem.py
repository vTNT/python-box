#!/usr/bin/env python
# -*- coding:utf-8 -*-

def memory_stat():
    mem = {}
    f = open("/proc/meminfo")
    lines = f.readlines()
    f.close()
    for line in lines:
        if len(line) < 2:
            continue
        name = line.split(':')[0]
        var = line.split(':')[1].split()[0]
        mem[name] = int(long(var) / 1024.0)
    #print mem['MemTotal']
    mem['Memused'] = mem['MemTotal'] - mem['MemFree'] - mem['Buffers'] - mem['Cached']
    return mem

if __name__ == '__main__':
   mem = memory_stat()
   #print mem
   print "the total is %s Mb" % mem['MemTotal']
   print "the free is %s Mb" % mem['MemFree']
   print "the used is %s Mb" % mem['Memused']


