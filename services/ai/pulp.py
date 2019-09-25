#!/usr/bin/python
# -*- coding: utf-8 -*-

from qiniu import QiniuMacAuth
from qiniu import http
import json
from configobj import ConfigObj

config = ConfigObj("../../.config.ini", encoding='UTF8')
# 读配置文件
access_key = config['account']['access_key']
secret_key = config['account']['secret_key']

q_auth = QiniuMacAuth(access_key, secret_key)
data_json = "{\"data\":{\"uri\":\"http://7xlv47.com1.z0.glb.clouddn.com/pulpsexy.jpg\"}" + "}"
url = "http://argus.atlab.ai/v1/pulp"
content_type = "application/json"
# data = data_json.encode('utf-8')
authorization = "Qiniu " + q_auth.token_of_request("POST", "argus.atlab.ai", url, "", content_type, data_json)
headers = {}
headers["Host"] = "argus.atlab.ai"
headers["Content-Type"] = content_type
ret, info = http._post_with_qiniu_mac(url, json.loads(data_json), q_auth)
print(info)
