'''
Author: WildboarG
version: 1.0
Date: 2022-05-27 15:23:10
LastEditors: WildboarG
LastEditTime: 2022-08-02 20:33:30
Descripttion: 
'''
from info import *

index = "https://api.xxx.edu.cn"      # 获取cook的host
host = "https://lightapp.xxx.edu.cn"  # 所在学校调用微哨的host
refer = 'lightapp.xxx.edu.cn'         # host
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
authorityid=["xxxx","xxx"]
