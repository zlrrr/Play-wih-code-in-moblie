# coding: utf-8
import requests
r = requests.get("http://www.baidu.com")
r.status_code
r.encoding = 'utf-8'
r.text
type(r)
r.headers
