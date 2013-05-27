#!/usr/bin/env python
# -*- coding:utf-8 -*-

def printmax(x, y):
    '''print the max of two numbers.
    the two values must be integers.'''
    x = int(x)
    y = int(y)

    if x > y:
        print x, 'is max'
    else:
        print y, 'is max'

printmax(3, 5)
#print printmax.__doc__
