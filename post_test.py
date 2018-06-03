#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
import json

url = 'http://192.168.0.107:5000/mine'
body = {"message": "测试3"}
headers = {'content-type': "application/json", 'Authorization': 'APP appid = 4abf1a,token = 9480295ab2e2eddb8'}

# print type(body)
# print type(json.dumps(body))
# 这里有个细节，如果body需要json形式的话，需要做处理
# 可以是data = json.dumps(body)
response = requests.post(url, data=json.dumps(body), headers=headers)
# 也可以直接将data字段换成json字段，2.4.3版本之后支持
# response  = requests.post(url, json = body, headers = headers)

# 返回信息
print (response.text)
# 返回响应头
print (response.status_code)
