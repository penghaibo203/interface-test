#!/usr/bin/env python3.6.4  
# encoding: utf-8  
# @Time    : 2018/6/24 16:16  
# @Author  : penghaibo  
# @contact: xxxx@qq.com  
# @Site    :   
# @File    : test_ranzhi_login.py  
# @Software: PyCharm

import requests
import hashlib
import re
import unittest

class testRanzhiLogin(unittest.TestCase):
    def setUp(self):
        self.url = "http://127.0.0.1/ranzhi/www/sys/user-login-L3JhbnpoaS93d3cvc3lzLw==.html"
        self.username = "admin"
        self.password = "1234"
        pass

    def tearDown(self):
        pass

    def test_ranzhi_login(self):
        #1. 请求登录页
        res = requests.get(self.url)
        #2. 通过正则表达式获取v.random的值
        pattern = "(?=v.random = \").*(?=;<)"
        result = re.search(pattern, res.text).group()
        random_str = result.replace('v.random = "', '').replace('"', '')
        #3. 对password进行加密
        step1 = hashlib.md5(random_str.encode('utf-8')).hexdigest()
        tempstr = step1 + self.username
        step2 = hashlib.md5(tempstr.encode('utf-8')).hexdigest()
        tempstr = step2 + random_str
        newpassword = hashlib.md5(tempstr.encode('utf-8')).hexdigest()
        #newpassword = hashlib.md5(hashlib.md5(hashlib.md5(random_str.encode('utf-8')) + self.username.encode('utf-8')) + random_str.encode('utf-8'))
        rawpassword = hashlib.md5(newpassword.encode('utf-8')).hexdigest()
        #4. 构造请求参数
        payload = {"account":self.username,"password":newpassword,"referer":"/","rawPassword":rawpassword,"keepLogin":"false"}
        #5. 发送请求
        res = requests.post(self.url, json=payload)
        #6. 校验结果
        self.assertIn('<html>', res.text)
        pass

if __name__ == "__main__":
    unittest.main()