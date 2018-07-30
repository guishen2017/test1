#-*- coding:utf-8 -*-
import re

def filte(html):
    reg = re.compile('<[^>]*>')
    content = reg.sub('', html).replace('\n', '')
    return content
