import os
import json
import base64
import sqlite3
from win32crypt import CryptUnprotectData

def get_cookie_from_chrome(host='.luogu.com.cn'):
    cookie_path = r'C:\Program Files (x86)\Google Chrome\Chrome\Data\Default\Cookies'
    
    sql = "select host_key,name,encrypted_value from cookies where host_key='%s'" % host

    with sqlite3.connect(cookie_path) as conn:
        cu = conn.cursor()
        res = cu.execute(sql).fetchall()
        cu.close()
        cookies = {}
        for host_key, name, encrypted_value in res:
            cookies[name] = CryptUnprotectData(encrypted_value)[1].decode()
        # print(cookies)
        return cookies

print(get_cookie_from_chrome('.luogu.com.cn'))
