# smtplib 用于邮件的发信动作
import smtplib
#构建邮件头
from email.header import Header
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
#引用csv模块。
import csv

data = [['代大帅 ', '295454688@qq.com']]
#内容
text = '''亲爱的学员，你好！
​    我是吴枫老师，能遇见你很开心。
​    希望学习Python对你不是一件困难的事情！

人生苦短，我用Python
'''
#主机、域名
smtp_server = 'smtp.qq.com'
#端口
port = 465
encoding = 'utf-8'
#用户名/发信邮箱
from_addr = '295454688@qq.com'
#密码/授权码
password = 'mfhorcmupefgbici'
#接收人
to_addr = '295454688@qq.com'
#待写入csv文件的内容
with open('to_addrs.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    for row in data:
        writer.writerow(row)

# 读取收件人数据，并启动写信和发信流程
with open('to_addrs.csv', 'r') as f:
    reader = csv.reader(f)
    for row in reader: 
        to_addrs=row[1]
        msg = MIMEText(text,'plain','utf-8')
        msg['From'] = Header(from_addr)
        msg['To'] = Header(to_addrs)
        msg['Subject'] = Header('python test')
        server = smtplib.SMTP_SSL(smtp_server)
        server.connect(smtp_server,port)
        server.login(from_addr, password)
        try:
            server.sendmail(from_addr, to_addrs, msg.as_string())
            print('恭喜，发送成功')
        except:
            print('发送失败，请重试')

# 关闭服务器
server.quit()