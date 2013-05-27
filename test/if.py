#!/usr/bin/env python
# -*- coding:utf-8 -*-

### (2) mod doc ###
number = 23
guess = int(raw_input('enter an integer : '))

if guess == number:
    print 'yeah,you guest it'
elif guess < number:
    print 'no,it is a little higher than that'
else:
    print 'no, it is a little lower than that'


print 'Done!'
