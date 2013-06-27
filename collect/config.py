#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Filename: config.py
# Last modified: 2013-06-25 11:49
# Author: vTNT
# Email : vbb625@gmail.com
# Description: 

import MySQLdb

from libs.load import PluginLoad

def status():
    try:
        load = PluginLoad.load_stat()
        MYSQL_CONFIG = {
            'host': 'localhost',
            'user': 'root',
            'passwd': 'xxx',
            'port': 3306,
        }

        conn=MySQLdb.connect(host = MYSQL_CONFIG['host'],user = MYSQL_CONFIG['user'] ,passwd = MYSQL_CONFIG['passwd'],port = MYSQL_CONFIG['port'])
        cur = conn.cursor()

        cur.execute('create database if not exists system')
        conn.select_db('system')
        cur.execute(sql= "inseret into %s (%s) values (%s)" % ("loadload",",".join([k for k in load.keys()]),",".join([v for v in load.values()])))
        conn.commit()
        cur.close()
        conn.close()
    except MySQLdb.Error,e:
        print "Mysql Error %d: %s" % (e.args[0],e.args[1])


### (7) main    ###
if __name__ == '__main__':
    status()

