#!/usr/bin/env python
# -*- coding:utf-8 -*-

name = 'swaroop'

if name.startswith('swa'):
    print 'yes'

if 'a' in name:
    print 'yes'

if name.find('war') != -1:
    print 'yes'

delimiter = '_*_'
mylist = ['aaa', 'bbb', 'ccc']
print delimiter.join(mylist)
