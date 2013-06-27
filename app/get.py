#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Filename: get.py
# Last modified: 2013-06-27 16:53
# Author: vTNT
# Email : vbb625@gmail.com
# Description:将远端的remote_dir的内容下载到本地的local_dir 

import paramiko
import os
import datetime

hostname='xxx.xxx.xxx.xxx'
username='xxx'
password='xxx'
port=22
local_dir='/tmp/a/'
remote_dir='/tmp/test/'


### (7) main    ###
def get():
    try:
        t=paramiko.Transport((hostname,port))
        t.connect(username=username,password=password)
        sftp=paramiko.SFTPClient.from_transport(t)
        files=sftp.listdir(remote_dir)
        for f in files:
            print ''
            print '#########################'
            print 'Beginning to download file from %s %s ' % (hostname,datetime.datetime.now())
            print 'Downloading file:',os.path.join(remote_dir,f)

            sftp.get(os.path.join(remote_dir,f),os.path.join(local_dir,f))

            print 'Download file success %s ' % datetime.datetime.now()
            print ''
            print '#########################'

    except Exception:
        print "error"
        t.close()

if __name__ == '__main__':
    get()
