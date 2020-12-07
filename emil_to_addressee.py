import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr

my_sender = 'lee291630817@163.com'  # 发件人邮箱账号
# my_sender = '291630817@qq.com'
# my_pass = 'uhyzcdcsduuwbigd'  # 发件人邮箱密码FPPZNJTPNBEMFEHH
my_pass = 'FPPZNJTPNBEMFEHH'

my_user = '291630817@qq.com'  # 收件人邮箱账号，我这边发送给自己


def emil_mail(content,my_user,user):
    ret = True
    try:
        msg = MIMEText(content, 'html', 'utf-8')
        msg['From'] = formataddr(["老冰日报", my_sender])  # 括号里的对应发件人邮箱昵称、发件人邮箱账号
        msg['To'] = formataddr([user, my_user])  # 括号里的对应收件人邮箱昵称、收件人邮箱账号
        msg['Subject'] = "今日头条新闻"  # 邮件的主题，也可以说是标题

        server = smtplib.SMTP_SSL("smtp.163.com", 465)  # 发件人邮箱中的SMTP服务器，端口是25
        server.login(my_sender, my_pass)  # 括号中对应的是发件人邮箱账号、邮箱密码
        server.sendmail(my_sender, [my_user, ], msg.as_string())  # 括号中对应的是发件人邮箱账号、收件人邮箱账号、发送邮件
        server.quit()  # 关闭连接
    except Exception as e:  # 如果 try 中的语句没有执行，则会执行下面的 ret=False
        print(e)
        ret = False
    return ret

if __name__ == '__main__':
    ret = emil_mail(content='666',my_user='291630817@qq.com')
    if ret:
        print("邮件发送成功")
    else:
        print("邮件发送失败")
