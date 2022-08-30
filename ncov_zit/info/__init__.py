'''
Author: WildboarG
version: 1.0
Date: 2022-05-27 15:23:10
LastEditors: WildboarG
LastEditTime: 2022-08-24 22:32:02
Descripttion: 
'''


import requests
import json
import time

schoolcode="zit"
authorityid=["10025","10081","10214","10263"]
activityid ="2614"

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

