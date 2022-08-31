'''
Author: WildboarG
version: 1.0
Date: 2022-05-28 10:26:28
LastEditors: WildboarG
LastEditTime: 2022-08-23 21:17:06
Descripttion: 
'''

import requests
from info import *
##  打卡请求post
def sign(data,cook):
    headers = {
        'Content-Type': 'application/json',
        'Cookie': cook,
    }
    #print(data)
    try:
        data = requests.post(
            url=api["sign_url"],
            json=data, 
            headers=headers
        ).json()
        #print(data)
        if data.get("errcode") == 0:
            return "[S]Successfully"
        if data.get('errmsg')=='不能重复回答同一问卷':
            return "[S]Already signed"
        else:
            return "[E]error"
    
    except:
        return "[E]:Unknown"


