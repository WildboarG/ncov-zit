
from rich import print
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
        if data.get('errmsg')=='不能重复回答同一问卷':
            return "[S]Already signed"
        else:
            return "[E]error"
    
    except:
        return "[E]:Unknown"


