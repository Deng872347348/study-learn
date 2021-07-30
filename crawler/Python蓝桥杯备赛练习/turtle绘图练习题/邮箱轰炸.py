smtpServer = 'smtp.126.com'  # 邮件发送帐户的smtp服务器地址
smtpPort = '25'  # 邮件发送帐户的smtp服务器发送端口
smtpUser = '******@126.com'  # 邮件发送帐户名
smtpPwd = '******'  # 邮件发送帐户密码，我这里打*号
sendTo = '798033502@qq.com'  # 接收邮箱地址

import smtplib, config, email, sys, socket, threading, time
from email.Message import Message
def connect():  # 定义一个方法，用来连接到邮箱服务器
    try:
        server = smtplib.SMTP(config.smtpServer, config.smtpPort)
        server.ehlo()
        server.login(config.smtpUser, config.smtpPwd)
        return server
    except Exception:
        print
        "无法连接到邮箱服务器！"


def sendInfo(server, to, subject, content):
    msg = Message()
    msg['Mime-Version'] = '1.0'
    msg['From'] = config.smtpUser
    msg['To'] = to
    msg['Subject'] = subject
    msg.set_payload(content)
    try:
        mailinfo = server.sendmail(config.smtpUser, to, str(msg))
    except Exception as ex:
        print("Error!邮件发送失败！%s" % ex)
    else:
        print("Goodluck！邮件发送成功！")


def myfunc():
    global contents
    print(contents)
    text = "你好，我是马化腾，感觉你人挺不错的，明天来我们公司上班吧"
    if contents != text:
        contents = text
        server = connect()
        sendInfo(server, to, subject, contents)
    t = threading.Timer(10, myfunc)
    t.start()


if __name__ == '__main__':
    while True:
        to = config.sendTo
        subject = "面试通知"
        server = connect()
        contents = "你好，我是马化腾，感觉你人挺不错的，明天来我们公司上班吧"
    sendInfo(server, to, subject, contents)
    timer = threading.Timer(10.0, myfunc)
    timer.start()
    time.sleep(1)
