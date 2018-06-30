#!/usr/bin/env python3.6.4  
# encoding: utf-8  
# @Time    : 2018/6/24 16:15  
# @Author  : penghaibo  
# @contact: xxxx@qq.com  
# @Site    :   
# @File    : test_historyweather.py  
# @Software: PyCharm

import requests
from config import config
import unittest
import ddt
from lib import util


@ddt.ddt
class testHistoryWeather(unittest.TestCase):
    def setUp(self):
        self.key = config.appkey
        self.provice_url = config.host + "province"
        self.city_url = config.host + "citys"
        self.weather_url = config.host + "weather"
        self.province_id = 1
        pass

    def tearDown(self):
        pass

    #测试获取省份列表接口
    def test_get_provincelist(self):
        param = "key=" + self.key
        res = requests.get(self.provice_url, param)
        jsonRes = res.json()
        self.assertEqual(jsonRes.get("reason"), "查询成功")
        pass

    #测试获取城市列表接口
    def test_get_citylist(self):
        param = "key=" + self.key
        res = requests.get(self.provice_url, param)
        jsonRes = res.json()
        self.assertEqual(jsonRes.get("reason"), "查询成功")
        result = jsonRes.get("result")
        for i in range(len(result)):
            province = result[i].get('province')
            if "广东" == province:
                self.province_id = result[i].get('id')
        payload = {"key":self.key, "province_id":self.province_id}
        res = requests.post(self.city_url, data=payload)
        jsonRes = res.json()
        self.assertEqual(jsonRes.get("reason"), "查询成功")
        pass

    #测试获取历史天气接口
    @ddt.data(*util.get_testdata("./testdata/weather_param.txt"))
    # @ddt.data(['1', '2018-06-01'],
    #           ['2', '2018-06-02'],
    #           ['3', '2018-06-03'])
    @ddt.unpack
    def test_get_historyweather(self, city_id, weather_date):
        print(city_id)
        payload = {"key":self.key, "city_id":city_id, "weather_date":weather_date}
        res = requests.post(self.weather_url, data=payload)
        jsonRes = res.json()
        self.assertEqual(jsonRes.get("reason"), "查询成功")
        pass


if __name__ == "__main__":
    unittest.main()