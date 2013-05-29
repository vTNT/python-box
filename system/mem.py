#!/usr/bin/env python
# -*- coding:utf-8 -*-

def memory_stat():
    mem = {}
    f = open("/proc/meminfo")
    lines = f.readlines()
    print lines
    f.close()
    
    for line in lines:
        if len(line) < 2: continue
        name = line.split(':')[0]
        var = line.split(':')[1].split()[0]
        mem[name] = long(var) * 1024.0
    mem['Memused'] = mem['MemTotal'] - mem['MemFree'] - mem['Buffers'] - mem['cached']
    return mem
