'''
Author: WildboarG
version: 1.0
Date: 2022-05-02 10:27:13
LastEditors: WildboarG
LastEditTime: 2022-05-24 12:49:26
Descripttion: 
'''
# -*- coding:UTF-8 -*-
from configparser import ConfigParser
import requests
import os

## 每日打卡推送
## connect 根据推送格式修改
def pushall(message):
    config = ConfigParser()
    file_path = os.path.join(os.path.abspath('./config'),'config.ini')
    print(file_path)
    if not os.path.exists(file_path):
        raise FileNotFoundError("No found config file")
    config.read(file_path,encoding='utf-8')
    token= config.get('pushplus','token')

    sign,all,unsign_pron= message
    pushurl = "http://www.pushplus.plus/send"

    tables = """
#### 健康填报平台\n
---
\n
|打卡人数|成功人数|失败人数|
|:---:|:---:|:---:|
|{}|{}|{}|
\n
失败人员名单：\n
{}
    """.format(all,sign,all-sign,unsign_pron)
    
    json={
        "token":token,## token
        "title":"健康打卡推送", ## title
        "content":tables,     ## content
        "template":"markdown",## text html markdown json
        "topic":""     ## 群组推送 不加默认个人推送
        }

    res=requests.post(pushurl,data=json)
    print(res)
