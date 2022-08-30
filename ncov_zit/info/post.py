'''
Author: WildboarG
version: 1.0
Date: 2022-05-28 10:26:28
LastEditors: WildboarG
LastEditTime: 2022-08-23 21:17:06
Descripttion: 
'''

import requests
import json
from . import *
##  打卡请求post
def sign(data,cook):
    headers = {
        'Content-Type': 'application/json',
        'Cookie': cook,
    }
    try:
        data = requests.post(
            url=api["sign_url"],
            json=data, 
            headers=headers
        ).json()
        #print(data)
        if data.get("errcode") == 0:
            return "[S]Successfully"
        else:
            return "[S]Already Clocked"
    
    except:
        return "[E]:Unknown"


