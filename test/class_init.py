#!/usr/bin/env python
# -*- coding:utf-8 -*-

class Person:
    def __init__(self, name):
        self.name1 = name
    def sayHi(self):
        print 'xxxx', self.name1

p = Person('Swaroop')
p.sayHi()
