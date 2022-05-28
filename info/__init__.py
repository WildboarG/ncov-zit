'''
Author: WildboarG
version: 1.0
Date: 2022-05-27 15:23:10
LastEditors: WildboarG
LastEditTime: 2022-05-28 11:46:50
Descripttion: 
'''
from info import *
index = "https://api.zit.edu.cn"
host = "https://lightapp.zit.edu.cn"
refer = 'lightapp.zit.edu.cn/'
redirect_uri = "https://lightapp.zit.edu.cn/check/questionnaire"
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
authorityid=["10025","10081","10214","10263"]