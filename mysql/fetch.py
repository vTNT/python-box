#!/usr/bin/env python
# -*- coding:utf-8 -*-

import MySQLdb

try:
    conn=MySQLdb.connect(host='localhost',user='root',passwd='xxx',port=3306)
    cur = conn.cursor()

    conn.select_db('python')

    count = cur.execute('select * from test')
    print 'there has %s rows record' % count

    result = cur.fetchone()
    print result
    print 'ID: %s info %s' % result

    results = cur.fetchmany(5)
    for r in results:
        print

    print '=='*10
    cur.scroll(0,mode='absolute')

    results = cur.fetchall()
    for r in results:
        print r[1]

    conn.commit()
    cur.close()
    conn.close()

except MySQLdb.Error,e:
    print "Mysql Error %d: %s" % (e.args[0],e.args[1])
