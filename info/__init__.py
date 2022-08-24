'''
Author: WildboarG
version: 1.0
Date: 2022-05-27 15:23:10
LastEditors: WildboarG
LastEditTime: 2022-08-24 14:37:33
Descripttion: 
'''
from info import *
import requests
import json
import time
## yours school
authorityid=["xxxx","xxxx","xxxx","xxxx"]
schoolcode = ""
activityid = "xxxx"

index = "https://api.{}.edu.cn".format(schoolcode)      # 获取cook的host
host = "https://lightapp.{}.edu.cn".format(schoolcode)  # 所在学校调用微哨的host
refer = 'lightapp.{}.edu.cn'.format(schoolcode)         # host
redirect_uri = host+"/check/questionnaire"

endpoint ={
    "login": index + "/login",
    "authorize": index + "/oauth/authorize",
}
api = {
    "getQuestionNaireList" : host + "/api/questionnaire/questionnaire/getQuestionNaireList",
    "getQuestionDetail": host + "/api/questionnaire/questionnaire/getQuestionDetail",
    "userInfo": host + "/userInfo",
    "sign_url" : host + '/api/questionnaire/questionnaire/addMyAnswer'
}



## about verify
get_verify_url = "https://appservice.{}.edu.cn/whistlenew/index.php".format(schoolcode)
get_search_url = "https://lightapp.{}.edu.cn/api/reportstatistics/reportstatistics/getStatistical".format(schoolcode)

