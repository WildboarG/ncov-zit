'''
Author: WildboarG
version: 1.0
Date: 2022-05-27 15:28:40
LastEditors: WildboarG
LastEditTime: 2022-08-23 21:16:43
Descripttion: 
'''
from . import *
import requests
import json
class GetContent:

    def __init__(self, schoolcode : str ,username : str,password : str):
        self.username = username
        self.password = password
        self.schoolcode = schoolcode
        self.authorityid = authorityid
        self.verify = "{}_{}".format(self.username,self.schoolcode)
        self.s = requests.session()

        self.headers = {
                "Content-Type":"application/x-www-form-urlencoded"
            }

        self.data = {
                "schoolcode": schoolcode,
                "username": self.username,
                "password": self.password,
                "verifyValue":"", 
                "verifyKey": self.verify,
                "ssokey":""
            }
        self.params = {
                "response_type":"code",
                "client_id":"pqZ3wGM07i8R9mR3",
                "redirect_uri":redirect_uri,
                "scope":"base_api",
                "state":"ruijie"
                }
        self.params1 = {
            "sch_code":self.schoolcode,
            "stu_code": self.username,
            "authorityid": json.dumps(self.authorityid),
            "type": '1',
            "pagenum": '1',
            "pagesize": '20',
            "stu_range": '999',
            "searchkey": ""
        }

    def _get_cookie(self,realcook:str)->str:
        return self.s.get(
                url = str(realcook),
                headers = self.headers,
                allow_redirects = False
            ).headers["set-cookie"]

    def _get_realcook(self) -> str:
        spaserver = self.s.get(
                url=endpoint["authorize"],
                headers=self.headers,
                params=self.params,
                allow_redirects=False
            )
        return spaserver.text[22:]

    def _get_addr(self):
        self.s.post(
                url=endpoint["login"],
                headers=self.headers,
                data=self.data,
                allow_redirects=False
            )

    def _get_init_cook(self)->str:
        return self.s.get(endpoint["login"]).headers.get("Set-Cookie")
    
    def rel_cookie(self) -> str:
        cook = self._get_init_cook()
        self.headers["Cookie"] = cook
        try:
            self._get_addr()            
            realcook = self._get_realcook()
            cookie =self._get_cookie(realcook)

            return cookie
        
        except:
            return None

    def _get_yesterday_info(self,header :str,params2 :str) -> str:
        return self.s.get(
                url = api["getQuestionDetail"],
                headers = header,
                params = params2,
            ).json().get("data")

    def _get_yesterday_data(self,header)->str:
        return self.s.get(
                url = api["getQuestionNaireList"],
                headers = header,
                params = self.params1,
            ).json().get("data")[0]

    def _handle_info(self,info,head,activityid)->str:
        try:
            questions = info.get("question_list")
            private_id = info.get("last_private_id")
            flag = 0
            answers = []
            while flag < len(questions):
                answer = {
                    "questionid": questions[flag].get("questionid"),
                    "optionid": questions[flag].get("user_answer_optionid"),
                    "optiontitle": 0,
                    "question_sort": 0,
                    'question_type': questions[flag].get("question_type"),
                    "option_sort": 0,
                    'range_value': "",
                    "content": questions[flag].get("user_answer_content"),
                    "isotheroption": questions[flag].get("otheroption"),
                    "otheroption_content": questions[flag].get("user_answer_otheroption_content"),
                    "isanswered": questions[flag].get("user_answer_this_question"),
                    "answerid": questions[flag].get("answerid"),
                }
                jump = 0
                type = answer["question_type"]
                #print(answer.get("optionid"))
                if type == 1:
                    for i in questions[flag].get("option_list"):
                        if answer["optionid"].isdigit() and i.get("optionid") == int(answer["optionid"]):
                            answer["optiontitle"] = i.get("title")
                            if questions[flag].get("hsjump"):
                                jump = i.get("jumpid") - 1

                elif type in [3, 4, 7, 8, 9]:
                    answer["optionid"] = 0
                answer["answered"] = answer["isanswered"]
                answers.append(answer)
                if jump:
                    flag = jump
                else:
                    flag += 1

            flag = 0
            totalArr = []
            while flag < len(questions):
                answer = {
                    "questionid": questions[flag].get("questionid"),
                    "optionid": questions[flag].get("user_answer_optionid"),
                    "optiontitle": 0,
                    "question_sort": 0,
                    'question_type': questions[flag].get("question_type"),
                    "option_sort": 0,
                    'range_value': "",
                    "content": questions[flag].get("user_answer_content"),
                    "isotheroption": questions[flag].get("otheroption"),
                    "otheroption_content": questions[flag].get("user_answer_otheroption_content"),
                    "isanswered": questions[flag].get("user_answer_this_question")
                }
                type = answer['question_type']

                if type == 1 and answer["optionid"] != "":
                    for i in questions[flag].get("option_list"):
                        if answer["optionid"].isdigit() and i.get("optionid") == int(answer["optionid"]):
                            answer["optiontitle"] = i.get("title")
                elif type in [3, 7]:
                    answer["optionid"] = 0

                if questions[flag].get("user_answer_this_question"):
                    answer["isanswered"] = True
                    answer["answerid"] = questions[flag].get("answerid")
                    answer["answered"] = answer["isanswered"]
                else:
                    answer["hide"] = True
                    answer["optionid"] = 0
                    answer["isanswered"] = ''
                    answer["answered"] = False

                totalArr.append(answer)
                flag += 1

            head['Referer'] = refer
            userinfo = requests.get(
                    url = api["userInfo"],
                    headers=head
                ).json().get("data")
            return  {
                "sch_code": userinfo.get("schcode"),
                "stu_code": userinfo.get("stucode"),
                "stu_name": userinfo.get("username"),
                "identity": userinfo.get("identity"),
                "path": userinfo.get("path"),
                "organization": userinfo.get("organization"),
                "gender": userinfo.get("gender"),
                "activityid": activityid,
                "anonymous": 0,
                "canrepeat": 1,
                "repeat_range": 1,
                "question_data": answers,
                "totalArr": totalArr,
                "private_id": private_id
            }
        except:
            return None

    def _get_params2(self,actionid:str)->str:
            return {
                "sch_code": self.schoolcode,
                "stu_code": self.username,
                "activityid":json.dumps(actionid),
                "can_repeat":"1",
                "page_from":"onpublic",
                "private_id":"0"
            }
    def _get_lastdata(self,cookie :str)->str:
        if not cookie:
            return None
        head = {
            #'Content-Type': 'application/json',
            'Cookie': cookie
        }
        try:
            ## 获取上次的info
            data = self._get_yesterday_data(head)
            activityid = data.get("activityid")
            params2 = self._get_params2(activityid)
        except:
            return None
        
        try:
            ## 获取问卷的详细信息
            info = self._get_yesterday_info(head,params2)
            return self._handle_info(info,head,activityid)
        except:
            return None
    # 
    def reporter(self):
        cookie = self.rel_cookie()
        return self._get_lastdata(cookie)
        
        

