#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Filename: mail2.py
# Last modified: 2013-06-25 23:26
# Author: vTNT
# Email : vbb625@gmail.com
# Description: 
#!/usr/bin/python 
#coding:utf-8 
 
 
import smtplib 
from email.mime.text import MIMEText 
import sys 
 
mail_host = 'smtp.163.com' 
mail_user = 'username' 
mail_pass = 'password' 
mail_postfix = '163.com' 
 
def send_mail(to_list,subject,content): 
    me = mail_user+"<"+mail_user+"@"+mail_postfix+">" 
    msg = MIMEText(content) 
    msg['Subject'] = subject 
    msg['From'] = me 
    msg['to'] = to_list 
     
    try: 
        s = smtplib.SMTP() 
        s.connect(mail_host) 
        s.login(mail_user,mail_pass) 
        s.sendmail(me,to_list,msg.as_string()) 
        s.close() 
        return True 
    except Exception,e: 
        print str(e) 
        return False 
     
if __name__ == "__main__": 
    """
传入的三个参数：接收用户，邮件主题，邮件内容
    """
    send_mail(sys.argv[1], sys.argv[2], sys.argv[3]) 
