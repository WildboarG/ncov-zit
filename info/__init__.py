'''
Author: WildboarG
version: 1.0
Date: 2022-05-27 15:23:10
LastEditors: WildboarG
LastEditTime: 2022-08-23 21:16:10
Descripttion: 
'''
from info import *
import requests
import json

school = "zit"
index = "https://api.{}.edu.cn".format(school)      # 获取cook的host
host = "https://lightapp.{}.edu.cn".format(school)  # 所在学校调用微哨的host
refer = 'lightapp.{}.edu.cn'.format(school)         # host
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

## yours school
authorityid=["10025","10081","10214","10263"]

## about verify
get_verify_url = "https://appservice.{}.edu.cn/whistlenew/index.php".format(school)

