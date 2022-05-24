'''
Author: WildboarG
version: 1.0
Date: 2022-05-02 10:27:13
LastEditors: WildboarG
LastEditTime: 2022-05-24 12:49:55
Descripttion: 
'''
from configparser import ConfigParser
import requests
import os

def push(message):
    config = ConfigParser()
    file_path = os.path.join(os.path.abspath('./config'),'config.ini')
    if not os.path.exists(file_path):
        raise FileNotFoundError("No found config file")
    config.read(file_path,encoding="utf-8")
    sendkey= config.get('serverchan','sendkey')
    
    sign,all,unsign_pron= message
    
    
    sendurl = "https://sctapi.ftqq.com/{}.send?title=messagetitle".format(sendkey)
    connect = """
###  健康填报平台

---
打卡人数：{} \n
成功人数：{} \n
          \n
失败人数：{} \n
失败人员名单：\n
 {}\n
    """.format(all,sign,all-sign,unsign_pron)
    
    data = {
        "title":"ncov-health",
        "desp":connect,
        "channel":"9"   
    }
    res=requests.post(sendurl,data=data)
    print(res)
