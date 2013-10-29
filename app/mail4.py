#!/usr/bin/env python
# -*- coding:utf-8 -*-
#usage:python mail4.py xx

import sys
import smtplib
import os.path
from email.MIMEText import MIMEText
#from email.Utils import formatdate
from email.Header import Header
from email.MIMEMultipart import MIMEMultipart
from email.MIMEBase import MIMEBase

msg = MIMEMultipart()
 
#发送邮件的相关信息，根据你实际情况填写
smtpHost = 'smtp.xx.com'
smtpPort = '25'
sslPort  = '465'
fromMail = 'xx@xxx.com'
#toMail   = sys.argv[2]
username = 'xx@xx.com'
password = 'xxx'
user = sys.argv[1]
leader1 = 'xx@gmail.com'
toMail   = '%s@163.com' % user
#邮件标题和内容
subject  = u'%s xxxx' % user
body     = u'xxx'
 
#初始化邮件
encoding = 'utf-8'
msg['Subject'] = Header(subject,encoding)
msg['From'] = fromMail
msg['To'] = toMail
#msg['Date'] = formatdate()
msg['leader'] = leader1

att1 = MIMEText(body.encode(encoding),'plain',encoding)
msg.attach(att1)

att2 = MIMEText(open('/root/%s/%s.p12' % (user,user),'rb').read(),'base64', 'gb2312')
att2["Content-Type"] = 'application/octet-stream'
att2["Content-Disposition"] = 'attachment;filename="%s.p12"' % user
msg.attach(att2)

att3 = MIMEText(open('/root/xxx/Setup.doc','rb').read(),'base64', 'gb2312')
att3["Content-Type"] = 'application/octet-stream'
att3["Content-Disposition"] = 'attachment;filename="setup.doc"' 
msg.attach(att3)

try:
    #连接smtp服务器，明文/SSL/TLS三种方式，根据你使用的SMTP支持情况选择一种
    #普通方式，通信过程不加密
    #smtp = smtplib.SMTP(smtpHost,smtpPort)
    #smtp.ehlo()
    #smtp.login(username,password)
 
    #tls加密方式，通信过程加密，邮件数据安全，使用正常的smtp端口
    #smtp = smtplib.SMTP(smtpHost,smtpPort)
    #smtp.ehlo()
    #smtp.starttls()
    #smtp.ehlo()
    #smtp.login(username,password)
 
    #纯粹的ssl加密方式，通信过程加密，邮件数据安全
    smtp = smtplib.SMTP_SSL(smtpHost,sslPort)
    smtp.ehlo()
    smtp.login(username,password)
 
    #发送邮件
    smtp.sendmail(fromMail,[toMail,leader1],msg.as_string())
    smtp.close()
    print 'OK'
except Exception:
    print 'Error: unable to send email'
