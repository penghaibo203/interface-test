#!/usr/bin/env python3.6.4  
# encoding: utf-8  
# @Time    : 2018/6/24 16:34  
# @Author  : penghaibo  
# @contact: xxxx@qq.com  
# @Site    :   
# @File    : weather_suite.py  
# @Software: PyCharm

import unittest
from test_cases.test_historyweather import testHistoryWeather


def get_suite():
    suite = unittest.TestSuite()
    loader = unittest.TestLoader()

    testcases = loader.loadTestsFromTestCase(testHistoryWeather)
    # testcases = [testHistoryWeather("test_a_get_provincelist"),
    #              testHistoryWeather("test_b_get_citylist"),
    #              testHistoryWeather("test_c_get_historyweather")]
    suite.addTests(testcases)

    return suite