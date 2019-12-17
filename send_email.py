import smtplib
from email.mime.text import MIMEText

from email.mime.multipart import MIMEMultipart
from email.header import Header

# 第三方 SMTP 服务
mail_host = "smtp.qq.com"  # SMTP服务器

mail_user = 'username'  # 用户名
mail_pass = 'password'  # 密码/授权码

sender = 'xxxx@qq.com'  # 发件人邮箱
receivers = ['BBBB@qq.com']  # 接收人邮箱



'''
不需要添加附件
'''
content = 'Python Send success!'
title = 'Python test'  # 邮件主题
message = MIMEText(content, 'plain', 'utf-8')  # 内容, 格式, 编码
message['From'] = "{}".format(sender)
message['To'] = ",".join(receivers)
message['Subject'] = title


'''
需要添加附件
'''
reportPath = 'file path'
with open(reportPath) as f:
    mail_body = f.read()

msg = MIMEMultipart()
msg['Subject'] = Header('Python test' , 'utf-8')
msg['From'] = "{}".format(sender)
msg['To'] = ",".join(receivers)

# 编写html类型的邮件正文，MIMEtext()用于定义邮件正文
# 发送正文
text = MIMEText(mail_body, 'html', 'utf-8')
msg.attach(text)

# 发送附件
msg_file = MIMEText(mail_body, 'html', 'utf-8')
msg_file['Content-Type'] = 'application/octet-stream'
msg_file['Content-Disposition'] = 'attachment; filename="Report.html"'
msg.attach(msg_file)
#添加附件部分

try:
    smtpObj = smtplib.SMTP_SSL(mail_host, 465)  # 启用SSL发信, 端口一般是465
    smtpObj.login(mail_user, mail_pass)  # 登录验证
    smtpObj.sendmail(sender, receivers, msg.as_string())  # 发送
    print("mail has been send successfully.")
except smtplib.SMTPException as e:
    print(e)
