#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import linecache
from antlr4 import *
from antlr.MemInfoParser import MemInfoParser
from antlr.MemInfoLexer import MemInfoLexer
from antlr.MemInfoParserVisitor import MemInfoParserVisitor


class MemInfo:
    mem_available = 0

    def __init__(self) -> None:
        mem_available_size = get_mem_available_size()
        antlr4_parser(mem_available_size)
        self.mem_available = mem_size


class MyVisitor(MemInfoParserVisitor):
    def visitSizeStatHandler(self, ctx):
        global mem_size
        mem_size = int(ctx.getText())


def antlr4_parser(parser_str: str):
    """
    antlr4解析器
    :param parser_str:
    :return:
    """
    mem_info = InputStream(parser_str)
    # lexer
    lexer = MemInfoLexer(mem_info)
    stream = CommonTokenStream(lexer)
    # parser
    parser = MemInfoParser(stream)
    tree = parser.prog()
    visitor = MyVisitor()
    visitor.visit(tree)


def get_mem_available_size():
    """
    获取剩余内存大小
    :return:
    """
    file_path = '/proc/meminfo'
    line_number = 3
    return linecache.getline(file_path, line_number).strip()


def send_email():
    """
    发送邮件
    :return:
    """
    from email.mime.text import MIMEText
    from email.header import Header
    from smtplib import SMTP_SSL

    # qq邮箱smtp服务器
    host_server = 'smtp.qq.com'
    # sender_qq为发件人的qq号码
    sender_qq = 'xxx'
    # pwd为qq邮箱的授权码
    pwd = 'xx'
    # 发件人的邮箱
    sender_qq_mail = 'xx@qq.com'
    # 收件人邮箱
    receiver = 'xx@qq.com'
    # 邮件的正文内容
    mail_content = '告警,内存不够了'
    # 邮件标题
    mail_title = '告警!'

    # ssl登录
    smtp = SMTP_SSL(host_server)
    smtp.ehlo(host_server)
    smtp.login(sender_qq, pwd)

    msg = MIMEText(mail_content, "plain", 'utf-8')
    msg["Subject"] = Header(mail_title, 'utf-8')
    msg["From"] = sender_qq_mail
    msg["To"] = receiver
    smtp.sendmail(sender_qq_mail, receiver, msg.as_string())
    smtp.quit()


def main():
    # send email
    mem = MemInfo()
    if mem.mem_available < 16777216:
        send_email()


if __name__ == '__main__':
    main()
