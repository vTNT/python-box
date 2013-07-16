#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json
import urllib2
import sys
# based url and required header

class zabbixtools:
    def __init__(self):
        self.url = "http://192.168.200.211/zabbix/api_jsonrpc.php"
        self.header = {"Content-Type": "application/json"}

# auth user and password
    def user_login(self):
        data = json.dumps(
                {
                    "jsonrpc": "2.0",
                    "method": "user.login",
                    "params": {
                        "user": "Admin",
                        "password": "zabbix"
                        },
                    "id": 0
                    })

                # create request object
        request = urllib2.Request(self.url,data)
        for key in self.header:
            request.add_header(key,self.header[key])

# auth and get authid
        try:
            result = urllib2.urlopen(request)
        except URLError as e:
            print "Auth Failed, Please Check Your Name And Password:",e.code
        else:
            response = json.loads(result.read())
            result.close()
            authID = response['result']
            return authID

    def host_get(self):
        authID = self.user_login()
        data = json.dumps(
                {
                    "jsonrpc": "2.0",
                    "method": "host.get",
                    "params": {
                        "output":["hostid","name","status"],
                        #"filter":{"host":""}
                        },
                    "auth": authID,
                    "id": 1,
                    })
                # create request object
        request = urllib2.Request(self.url,data)
        for key in self.header:
            request.add_header(key,self.header[key])
        # get host list
        try:
            result = urllib2.urlopen(request)
        except URLError as e:
            if hasattr(e, 'reason'):
                print 'We failed to reach a server.'
                print 'Reason: ', e.reason
            elif hasattr(e, 'code'):
                print 'The server could not fulfill the request.'
                print 'Error code: ', e.code
        else:
            response = json.loads(result.read())
            result.close()
            print "\033[1;32;40m%s\033[0m" % "Number Of Hosts: ", "\033[1;31;40m%d\033[0m" % len(response['result'])
            for host in response['result']:
                print "\t","Host ID:",host['hostid'],"\t","Host Name:",host['name'].encode('GBK'),"\tstatus",host['status']

    def host_create(self,hostip,groupid,templateid):
        authID = self.user_login()
        data = json.dumps(
                {
                    "jsonrpc": "2.0",
                    "method": "host.create",
                    "params": {
                        "host": hostip,
                        "interfaces": [
                            {
                                "type": 1,
                                "main": 1,
                                "useip": 1,
                                "ip": hostip,
                                "dns": "",
                                "port": "10050"
                            }
                        ],
                        "groups": [
                            {
                                "groupid": groupid
                            }
                        ],
                        "templates": [
                            {
                                "templateid": templateid
                            }
                        ],
                },
                    "auth": authID,
                    "id": 1,
                    })
                # create request object
        request = urllib2.Request(self.url,data)
        for key in self.header:
            request.add_header(key,self.header[key])
        # get host list
        try:
            result = urllib2.urlopen(request)
        except URLError as e:
            if hasattr(e, 'reason'):
                print 'We failed to reach a server.'
                print 'Reason: ', e.reason
            elif hasattr(e, 'code'):
                print 'The server could not fulfill the request.'
                print 'Error code: ', e.code
        else:
            response = json.loads(result.read())
            result.close()
            print "Successful to create host %s " % hostip

    def host_delete(self,hostid):
        authID = self.user_login()
        data = json.dumps(
                {
                    "jsonrpc": "2.0",
                    "method": "host.get",
                    "params":[ 
                        {"hostid": hostid}
                        ],
                    "auth": authID,
                    "id": 1,
                    })
                # create request object
        request = urllib2.Request(self.url,data)
        for key in self.header:
            request.add_header(key,self.header[key])
        # get host list
        try:
            result = urllib2.urlopen(request)
        except URLError as e:
            if hasattr(e, 'reason'):
                print 'We failed to reach a server.'
                print 'Reason: ', e.reason
            elif hasattr(e, 'code'):
                print 'The server could not fulfill the request.'
                print 'Error code: ', e.code
        else:
            response = json.loads(result.read())
            result.close()
            print  "the host have been deleted !!!" 

    def hostgroup_get(self):
        authID = self.user_login()
        data = json.dumps(
                {
                    "jsonrpc": "2.0",
                    "method": "hostgroup.get",
                    "params": {
                        "output": "extend",
                        #"filter":{"host":""}
                        },
                    "auth": authID,
                    "id": 1,
                    })
                # create request object
        request = urllib2.Request(self.url,data)
        for key in self.header:
            request.add_header(key,self.header[key])
        # get host list
        try:
            result = urllib2.urlopen(request)
        except URLError as e:
            if hasattr(e, 'reason'):
                print 'We failed to reach a server.'
                print 'Reason: ', e.reason
            elif hasattr(e, 'code'):
                print 'The server could not fulfill the request.'
                print 'Error code: ', e.code
        else:
            response = json.loads(result.read())
            result.close()
            print "\033[1;32;40m%s\033[0m" % "Number Of Hostgroups: ","\033[1;31;40m%d\033[0m" % len(response['result'])
            for hostgroup in response['result']:
                print "\t","HostGroup_id:",hostgroup['groupid'],"\t","HostGroup_Name:",hostgroup['name'].encode('GBK')

    def hostgroup_create(self,hostgroup):
        authID = self.user_login()
        data = json.dumps(
                {
                    "jsonrpc": "2.0",
                    "method": "hostgroup.create",
                    "params": {
                        "name": hostgroup,
                        #"filter":{"host":""}
                        },
                    "auth": authID,
                    "id": 1,
                    })
                # create request object
        request = urllib2.Request(self.url,data)
        for key in self.header:
            request.add_header(key,self.header[key])
        # get host list
        try:
            result = urllib2.urlopen(request)
        except URLError as e:
            if hasattr(e, 'reason'):
                print 'We failed to reach a server.'
                print 'Reason: ', e.reason
            elif hasattr(e, 'code'):
                print 'The server could not fulfill the request.'
                print 'Error code: ', e.code
        else:
            response = json.loads(result.read())
            result.close()
            print "the %s hostgroup have been created !!!" % hostgroup

    def hostgroup_delete(self,hostgroupid):
        authID = self.user_login()
        data = json.dumps(
                {
                    "jsonrpc": "2.0",
                    "method": "hostgroup.delete",
                    "params": [
                         hostgroupid
                        #"filter":{"host":""}
                        ],
                    "auth": authID,
                    "id": 1,
                    })
                # create request object
        request = urllib2.Request(self.url,data)
        for key in self.header:
            request.add_header(key,self.header[key])
        # get host list
        try:
            result = urllib2.urlopen(request)
        except URLError as e:
            if hasattr(e, 'reason'):
                print 'We failed to reach a server.'
                print 'Reason: ', e.reason
            elif hasattr(e, 'code'):
                print 'The server could not fulfill the request.'
                print 'Error code: ', e.code
        else:
            response = json.loads(result.read())
            result.close()
            print "the %s hostgroup have been deleted !!!" % hostgroupid

    def template_get(self):
        authID = self.user_login()
        data = json.dumps(
                {
                    "jsonrpc": "2.0",
                    "method": "template.get",
                    "params": {
                        "output": "extend",
                        #"filter":{"host":""}
                        },
                    "auth": authID,
                    "id": 1,
                    })
                # create request object
        request = urllib2.Request(self.url,data)
        for key in self.header:
            request.add_header(key,self.header[key])
        # get host list
        try:
            result = urllib2.urlopen(request)
        except URLError as e:
            if hasattr(e, 'reason'):
                print 'We failed to reach a server.'
                print 'Reason: ', e.reason
            elif hasattr(e, 'code'):
                print 'The server could not fulfill the request.'
                print 'Error code: ', e.code
        else:
            response = json.loads(result.read())
            result.close()
            print "\033[1;32;40m%s\033[0m" % "Number Of Templates: ","\033[1;31;40m%d\033[0m" % len(response['result'])
            for template in response['result']:
                print "\t","Template_id:",template['templateid'],"\t","Template_Name:",template['name'].encode('GBK')

    def template_delete(self,templateid):
        authID = self.user_login()
        data = json.dumps(
                {
                    "jsonrpc": "2.0",
                    "method": "template.delete",
                    "params": [
                         templateid
                        #"filter":{"host":""}
                        ],
                    "auth": authID,
                    "id": 1,
                    })
                # create request object
        request = urllib2.Request(self.url,data)
        for key in self.header:
            request.add_header(key,self.header[key])
        # get host list
        try:
            result = urllib2.urlopen(request)
        except URLError as e:
            if hasattr(e, 'reason'):
                print 'We failed to reach a server.'
                print 'Reason: ', e.reason
            elif hasattr(e, 'code'):
                print 'The server could not fulfill the request.'
                print 'Error code: ', e.code
        else:
            response = json.loads(result.read())
            result.close()
            print "the %s template have been deleted !!!" % templateid

if __name__ == "__main__":
    test = zabbixtools()
    try:
        while True:
            show_menu = '''\033[32;40;1m----------------------Menu list--------------------------
                1, show host
                2, create host
                3, delete host
                4, show hostgroup
                5, create hostgroup
                6, delete hostgroup
                7, show template
                8, create template
                9, delete template
                10, Quit
----------Input number of you want to exec command----------------\033[0m'''
            try:
                print show_menu
                memu_choice = raw_input('please input you choice:')
                if memu_choice == '1':
                    test.host_get()
                    continue
                elif memu_choice == '2':
                    while True:
                        ip = raw_input('Enter your:Host_ip :')
                        groupid = raw_input('Enter your:Group_id :')
                        tempateid = raw_input('Enter your:Tempate_id :')
                        if ip and groupid and tempateid:
                            test.host_create(ip,groupid,tempateid)
                        else:
                            print "\033[1;31;40m%s\033[0m" % "Enter Error: ip or groupid or tempateid is NULL,please check it!"
                    continue
                elif memu_choice == '3':
                    while True:
                        hostid = raw_input('Enter the hostid to delete :')
                        choice = raw_input('Y/N ?')
                        if choice == 'Y' or choice == 'y':
                            test.host_delete(hostid)
                        else:
                            print "please check again"
                    continue
                elif memu_choice == '4':
                    test.hostgroup_get()
                    continue
                elif memu_choice == '5':
                    while True:
                        hostgroup = raw_input('Enter the new hostgroup name:')
                        choice = raw_input('Y/N ?')
                        if choice == 'Y' or choice == 'y':
                            test.hostgroup_create(hostgroup)
                        else:
                            print "please check again"
                    continue
                elif memu_choice == '6':
                    while True:
                        hostgroupid = raw_input('Enter the hostgroup id to delete:')
                        choice = raw_input('Y/N ?')
                        if choice == 'Y' or choice == 'y':
                            test.hostgroup_delete(hostgroupid)
                        else:
                            print "please check again"
                    continue
                elif memu_choice == '7':
                    test.template_get()
                    continue
                elif memu_choice == '8':
                    continue
                elif memu_choice == '9':
                    while True:
                        templateid = raw_input('Enter the template id to delete:')
                        choice = raw_input('Y/N ?')
                        if choice == 'Y' or choice == 'y':
                            test.template_delete(templateid)
                        else:
                            print "please check again"
                    continue
                elif memu_choice =='10':
                    break
                elif memu_choice == 'exit' or memu_choice == 'quit' or memu_choice == 'q':
                    break

            except KeyboardInterrput:
                print ''
                print 'you command is CTRL+C go back'
            except EOFError:
                print ''
                print 'you command is CTRL+D to quit'
    except:
        print ''
