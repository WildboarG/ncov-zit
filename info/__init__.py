'''
Author: WildboarG
version: 1.0
Date: 2022-05-27 15:23:10
LastEditors: WildboarG
LastEditTime: 2022-05-28 11:46:50
Descripttion: 
'''
from info import *
index = ""  ## 获取cook的host
host = ""  ## 所在学校调用微哨的host
refer = '' ## host去掉协议
redirect_uri = host+"/check/questionnaire"
## 一些登录请求的url
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
authorityid=[]   ## 学校归属
