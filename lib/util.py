#!/usr/bin/env python3.6.4  
# encoding: utf-8  
# @Time    : 2018/6/24 17:22  
# @Author  : penghaibo  
# @contact: xxxx@qq.com  
# @Site    :   
# @File    : util.py  
# @Software: PyCharm

def get_testdata(file_path):
    data4ddt = []
    with open(file_path, encoding='utf-8') as f:
        dataset = f.readlines()
        for data in dataset:
            data4ddt.append(data.strip().split(","))
    return data4ddt