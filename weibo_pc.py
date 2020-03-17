#coding=utf-8
import re
import requests
import smtplib
from email.header import Header
from email.mime.text import MIMEText

mail_host="smtp.qq.com"
mail_user="" #使用者邮箱
mail_pass="" #smtp码

sender=‘’ #代发者邮箱
receivers=[‘’
            ]
url="https://s.weibo.com/top/summary"
headers={"User-Agent":"",
         "Cookie":""
         }
rr=re.compile("<a href=\"(\S+)\" target=\"_blank\">(\S+)</a>")
def spider():
    htm=requests.get(url,headers=headers)
    txt=re.findall(rr,htm.text)
    return txt

def writein(href,txt):    
    with open('weibo_resou.html','w')as f:
        f.write("""<!doctype html>\n
<head></head>\n<body>""")
        for i in txt:
            f.write("%d. <a href=%s>%s</a><br>"%(txt.index(i)+1,href[txt.index(i)],i[1]))
        f.write("</body>")
        
def repair_url(url):
    return "https://s.weibo.com"+url

def mail(mail_host,mail_user,mail_pass,sender,receivers):
    with open('weibo_resou.html','r') as f:
        mail_msg=f.read(-1)
    message=MIMEText(mail_msg, 'html', 'gbk')
    message['From'] = Header("微博爬虫", 'gbk')
    message['TO'] = Header("群员", 'gbk')
    try:        
        smtpObj = smtplib.SMTP_SSL(mail_host,465)
        smtpObj.login(mail_user,mail_pass)
        smtpObj.sendmail(sender, receivers, message.as_string())
    except smtplib.SMTPException:
        print ("Error: 无法发送邮件")
        
        
        
if __name__=='__main__':
    txt=spider()
    href=[0 for i in range(len(txt))]
    for i in range(len(txt)):
        href[i]=repair_url(txt[i][0])
    writein(href,txt)
    mail(mail_host,mail_user,mail_pass,sender,receivers)
