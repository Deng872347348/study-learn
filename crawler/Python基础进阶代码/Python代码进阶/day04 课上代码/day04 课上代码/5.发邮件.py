"""
1. 申请一个邮箱。
2. 进入配置
    - 授权码（密码）
    - SMTP地址：smtp.126.com
3. 代码去发邮件
"""
import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr


content = """<h1 style="color:red;">   二狗子Alex  </h1>"""

# 定义发送的内容：头部、内容
msg = MIMEText(content, 'html', 'utf-8')
msg['From'] = formataddr(["路飞学成", "wptawy@126.com"])
msg['Subject'] = "嫂子好看"

# 126服务器
server = smtplib.SMTP_SSL("smtp.126.com")
# 登录，账户和授权码（非密码）
server.login("wptawy@126.com", "WIYSAILOVUKPQGHY")
# 发送邮件
server.sendmail("wptawy@126.com", ["@qq.com", ], msg.as_string())
server.quit()
