#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Filename: send.py
# Last modified: 2013-06-27 15:36
# Author: vTNT
# Email : vbb625@gmail.com
# Description:把本地local_dir的文件传输到remote_dir 

import paramiko
import os
import datetime

hostname='xxx.xxx.xxx.xxx'
username='xxx'
password='xxx'
port=22

local_dir='/tmp/a'
remote_dir='/tmp/test/'

### (7) main    ###
def send():
    try:
        t=paramiko.Transport((hostname,port))
        t.connect(username=username,password=password)
        sftp=paramiko.SFTPClient.from_transport(t)
        files=os.listdir(local_dir)
        for f in files:
            print ''
            print '########################'
            print 'Beginning to upload file %s ' % datetime.datetime.now()
            print 'Uploading file:',os.path.join(local_dir,f)

            sftp.put(os.path.join(local_dir,f),os.path.join(remote_dir,f))

            print 'Upload file success %s ' % datetime.datetime.now() 
            print ''     
            print '##########################################' 
    except Exception:
        print"error"
        t.close()
if __name__ == '__main__':
    send()
