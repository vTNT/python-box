#!/usr/bin/env python
# -*- coding:utf-8 -*-
import MySQLdb
def getdata():
    try:
        conn = MySQLdb.connect(host='localhost',user='root',passwd='xxx',port=3306)
        cur = conn.cursor()
        
        cur.execute('select user,host from mysql.user')
        cur.close()
        conn.close()
    except MySQLdb.Error,e:
        print "Mysql Error %d: %s" % (e.args[0],e.args[1])

if __name__ == '__main__':
    getdata()
