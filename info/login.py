'''
Author: WildboarG
version: 1.0
Date: 2022-05-27 15:28:40
LastEditors: WildboarG
LastEditTime: 2022-05-28 11:49:56
Descripttion: 
'''
from info import *
import requests
import json
class GetMe:
    def __init__(self, schoolcode : str ,usernamme : str,password : str):
        self.username = usernamme
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

    def login(self):

        get_cook = self.s.get(endpoint["login"])
        cook =get_cook.headers.get("Set-Cookie")

        self.headers["Cookie"] = cook
        try:
            self.s.post(
                url=endpoint["login"],
                headers=self.headers,
                data=self.data,
                allow_redirects=False
            )
            spaserver = self.s.get(
                url=endpoint["authorize"],
                headers=self.headers,
                params=self.params,
                allow_redirects=False
            )
            realcook = spaserver.text[22:]
            cookie =self.s.get(
                url = str(realcook),
                headers = self.headers,
                allow_redirects = False
            ).headers["set-cookie"]
            return cookie
        
        except:

            return None
    def get_lastdata(self):
        cookie = self.login()
        if not cookie:
            return None
        else:
            head = {
                #'Content-Type': 'application/json',
                'Cookie': cookie
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
        try:
            ## 获取上次的info
            data = self.s.get(
                url = api["getQuestionNaireList"],
                headers = head,
                params = self.params1,
            ).json().get("data")[0]

            activityid = data.get("activityid")
            authorityid = data.get("authorityid")

        except:
            return None
        
        try:
            ## 获取问卷的详细信息
            self.params2 = {
                "sch_code": self.schoolcode,
                "stu_code": self.username,
                "activityid":json.dumps(activityid),
                "can_repeat":"1",
                "page_from":"onpublic",
                "private_id":"0"
            }
            info = self.s.get(
                url = api["getQuestionDetail"],
                headers = head,
                params = self.params2,

            ).json().get("data")
        except:
            return None

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
            data = {
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
            return cookie,data
        ## 没有解析出问卷的信息
        except:
            return None

