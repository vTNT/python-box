#!/usr/bin/env python
# -*- coding:utf-8 -*-

def cpu_stat():
    cpu = []
    i = 0
    cpuinfo = {}
    f = open("/proc/cpuinfo")
    lines = f.readlines()
    f.close()
    for line in lines:
        if line == '\n':
            cpu.append('cpuinfo')
            i += 1
        if len(line) < 2:
            continue
        name = line.split(':')[0].rstrip()
        var = line.split(':')[1]
        cpuinfo[name] = var
    #print cpuinfo
    #print cpu
    return i,cpu,cpuinfo
if __name__ == '__main__':
    c =cpu_stat()
    print c
    print "the core number is %s " % c[2]['cache size']
    #print c



