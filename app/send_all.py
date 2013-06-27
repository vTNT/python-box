#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Filename:		send_all.py
# Last modified:	2013-06-27 17:48
# Author: vTNT
# Email : vbb625@gmail.com
# Description:批量主机上传文件,主机列表:config.ini 从本地local_dir 传输到remote_dir 

import paramiko 
import os 
import datetime 
from ConfigParser import ConfigParser 

ConfigFile='config.ini' 
config=ConfigParser() 
config.read(ConfigFile) 
hostname1=''.join(config.get('IP','ipaddress')) 
address=hostname1.split(';') 
print address 
username='xxx' 
password='xxx' 
port=22 
local_dir='/tmp/a/' 
remote_dir='/tmp/test/' 

def send_all():
    try: 
        for ip in address: 
            t=paramiko.Transport((ip,port)) 
            t.connect(username=username,password=password) 
            sftp=paramiko.SFTPClient.from_transport(t) 
#                files=sftp.listdir(dir_path) 
            files=os.listdir(local_dir) 
            print files 
            for f in files: 
                print '####################################################' 
                print 'Begin to upload file  to %s ' % ip 
                print 'Uploading ',os.path.join(local_dir,f) 

                print datetime.datetime.now() 
                sftp.put(os.path.join(local_dir,f),os.path.join(remote_dir,f)) 
                print datetime.datetime.now() 
                print '####################################################' 

    except Exception:
        print "error!"
        t.close()

if __name__=="__main__": 
    send_all()
