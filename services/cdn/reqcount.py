#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
查询指定域名指定时间段内的带宽
"""
import qiniu
from qiniu import CdnManager
from configobj import ConfigObj

config = ConfigObj("../../config.ini", encoding='UTF8')
# 读配置文件
access_key = config['account']['access_key']
secret_key = config['account']['secret_key']

auth = qiniu.Auth(access_key=access_key, secret_key=secret_key)
cdn_manager = CdnManager(auth)

startDate = '2018-10-28'
endDate = '2018-10-29'
granularity = '5min'

urls = [
    'x.xxx.com'
]

ret, info = cdn_manager
print(ret)
print(info)
