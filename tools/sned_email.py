from email.mime.text import MIMEText
import smtplib
from email.header import Header
import time

def send_email(filename):
    with open(filename, 'rb') as f:
        mail_body = f.read()
        f.close()
    # 设置发件邮箱
    from_address = "847112695@qq.com"
    password = "syojdtcddfolbdee"
    # 设置邮箱服务器
    smtp_server = "smtp.qq.com"
    # 设置收件人邮箱
    rec_address = ["17826854020@163.com","lishan.yuan@yelopack.com"]

    # 邮件正文
    msg = MIMEText(mail_body, 'html', 'utf-8')
    msg['Subject'] = Header('自动化测试报告', 'utf-8').encode()
    msg['From'] = Header('袁莉姗<%s>' % from_address)
    msg['To'] = Header('技术负责人<%s>' % rec_address)
    msg['data'] = time.strftime("%a,%d %b %Y %H:%M:%S %z")

    # 发送邮件
    try:
        # SMTP协议默认端口是25
        server = smtplib.SMTP(smtp_server, 25)
        # server.set_debuglevel(1)
        server.login(from_address, password)
        server.sendmail(from_address, rec_address, msg.as_string())
        server.quit()
    except smtplib.SMTPException as e:
        raise e

if __name__ == '__main__':
    send_email(r'C:\Users\17826\PycharmProjects\2020_api_auto\test_result\html_test_report\test_reportstApiTray.html')
