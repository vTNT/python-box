#!/usr/bin/env python
# -*- coding:utf-8 -*-

number = 23
running = True

while running:
    guess = int(raw_input('enter an integer : '))

    if guess == number:
        print 'yeah,you get it'
        running = False
    elif guess < number:
        print 'no, it is a little higher than that'
    else:
        print 'no, it is a little lower than that'

else:
    print 'the wile loop is over'

print 'Done'

