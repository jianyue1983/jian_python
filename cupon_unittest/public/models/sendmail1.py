import urllib
import urllib3
import ssl
from bs4 import BeautifulSoup
import datetime

import sys
import codecs
import time
import sys
import smtplib
from email.mime.text import MIMEText
from email.header import Header
from email.mime.multipart import MIMEMultipart
import configparser
from config import setting
from public.models.newReport import new_report

def email(file_new):
    f = open(file_new, 'rb')
    mail_body=f.read()
    f.close()
    #发送附件
    con = configparser.ConfigParser()
    con.read(setting.CONFIG_DIR, encoding='utf-8')
    report = new_report(setting.TEST_REPORT)
    sendfile = open(report, 'rb').read()

    mail_host = "smtp.exmail.qq.com"  # ÉèÖÃ·þÎñÆ÷
    mail_user = "chenwh@valuecom.cn"  # ÓÃ»§Ãû
    mail_pass = "!QAZ2wsx"  # ¿ÚÁî
    sender = 'chenwh@valuecom.cn'
    receivers = ['woddebbmm@163.com']  # ½ÓÊÕÓÊ¼þ£¬¿ÉÉèÖÃÎªÄãµÄQQÓÊÏä»òÕßÆäËûÓÊÏä
    subject="自动化测试报告"

    att = MIMEText(sendfile, 'base64', 'utf-8')
    att["Content-Type"] = 'application/octet-stream'
    att.add_header("Content-Disposition", "attachment", filename=("gbk", "", report))

    msg = MIMEMultipart('related')
    msg.attach(att)
    msgtext = MIMEText(mail_body, 'html', 'utf-8')

    msg.attach(msgtext)
    msg['Subject'] = subject
    msg['from'] = sender
    msg['to'] = receivers




    try:
        # smtpObj = smtplib.SMTP_SSL("smtp.exmail.qq.com", port=465)
        # smtpObj.login(mail_user, mail_pass)
        # smtpObj.sendmail(sender, receivers, msg.as_string())
        server = smtplib.SMTP()
        server.connect("smtp.exmail.qq.com", port=465)
        server.starttls()
        server.login(mail_user, mail_pass)
        server.sendmail(sender, receivers, msg.as_string())
        server.quit()
        print("邮件发送成功！")

    except smtplib.SMTPException:
        print("发送失败")
