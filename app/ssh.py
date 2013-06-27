#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Filename:		ssh1.py
# Last modified:	2013-06-27 14:11
# Author: vTNT
# Email : vbb625@gmail.com
# Description: 

import paramiko

hostname = 'xxx.xxx.xxx.xxx'
username = 'xxx'
password = 'xxx'
port = 22

def free():
    paramiko.util.log_to_file('paramiko.log')
    s = paramiko.SSHClient()
    s.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    s.connect(hostname = hostname, username = username, password = password)
    stdin,stdout,stderr = s.exec_command('free -m')

    print stdout.read()
    s.close()

if __name__ == '__main__':
    free()
