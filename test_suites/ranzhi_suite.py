#!/usr/bin/env python3.6.4  
# encoding: utf-8  
# @Time    : 2018/6/24 16:11  
# @Author  : penghaibo  
# @contact: xxxx@qq.com  
# @Site    :   
# @File    : ranzhi_suite.py  
# @Software: PyCharm

import unittest
from test_cases.test_ranzhi_login import testRanzhiLogin


def get_suite():
    suite = unittest.TestSuite()
    loader = unittest.TestLoader()

    suite.addTests(loader.loadTestsFromTestCase(testRanzhiLogin))

    return suite