# smtplib 用于邮件的发信动作
import smtplib
#构建邮件头
from email.header import Header
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
#引用csv模块。
import csv


# msg：文本内容，可自定义
# type：文本类型，默认为plain（纯文本）
# chartset：文本编码，中文为“utf-8”
msg = MIMEText('send by python','plain','utf-8')

#server = smtplib.SMTP()
#开启发信服务，这里使用的是加密传输 如果端口是用SSL加密，请这样写代码。其中server是变量名 默认25

#server.connect('smtp.qq.com', 25)
#主机、域名
host = 'smtp.qq.com'
#端口
port = 465
encoding = 'utf-8'
#用户名/发信邮箱
from_addr = '295454688@qq.com'
#密码/授权码
password = 'mfhorcmupefgbici'
#接收人
to_addr = '295454688@qq.com'
#内容
text = '''亲爱的学员，你好！
​    我是吴枫老师，能遇见你很开心。
​    希望学习Python对你不是一件困难的事情！

人生苦短，我用Python
'''
to_addrs = ['葫芦娃','爷爷']
msg = MIMEText(text,'plain','utf-8')
msg['From'] = Header('诛仙')
msg['to'] = Header(",".join(to_addrs)) 
msg['Subject'] = Header('python test')

server = smtplib.SMTP_SSL(host)
server.connect(host, port)
server.login(from_addr, password) 
server.sendmail(from_addr, to_addr, msg.as_string()) 
server.quit() 