'''
Author: WildboarG
version: 1.0
Date: 2022-08-23 17:17:33
LastEditors: WildboarG
LastEditTime: 2022-08-23 21:47:15
Descripttion: 
'''

import requests
import json
import time
school = "zit"
get_verify_url = "https://appservice.{}.edu.cn/whistlenew/index.php".format(school)
get_search_url = "https://lightapp.zit.edu.cn/api/reportstatistics/reportstatistics/getStatistical"
class Search:
    def __init__(self, user : str,password  : str) -> None:
        self.user = user
        self.password = password
        self.s = requests.session()
        self.params = {
            "m":"user",
            "a":"userLogin",
            "password":self.password,
            "student_number":self.user,
            "school":"zit",
            "device_type":"android"
        }
    
    def _require_verify(self):
        return self.s.get(url=get_verify_url,params=self.params)
    
    def _handle_verify(self) -> json:
        return json.loads(self._require_verify().text)
    
    def _parse_data(self) -> dict:
        return self._handle_verify().get("data")
    
    def _get_verify(self) -> str:
        return self._parse_data()["verify"]
        
    
    def _get_path(self)->list:
        my_info = self._parse_data()["my_info"]
        path = my_info["path"]
        return path.split(",")

    ## school
    def _get_school(self)->str:
        return self._get_path()[1]

    ## college
    def _get_college(self) ->str:
        return self._get_path()[2]

    ## organization
    def _get_organization(self) ->str:
        return self._get_path()[3]
    
    ## my class
    def _get_class(self) ->str:
        return self._get_path()[4]
    
    ## get verify school college organization myclass
    def set_verify(self):
        self.verify = self._get_verify()
        self.school = self._get_school()
        self.college = self._get_college()
        self.organization = self._get_organization()
        self.myclass = self._get_class()
        
    def _require_post(self,id):
        header = {
            'Content-Type':'application/json',
            'Cookie':self.cookie,
        }
        postdata = {
            "type":"org",
            #"identity":"student",
            "para":{
                "organization_id":id,
                "organization_path_str":"0"
            },
            "date":self.date,
            "activityid":"2614",
            "flag":0,
            "domain":school,
            #"stucode":self.user,
        }
        return self.s.post(url=get_search_url,headers=header,json=postdata)
    ## get the punching environment
    def get_feedback(self,cookie:str,mode="0", dafaultdate=time.strftime("%Y-%m-%d"))->str:
        self.set_verify()
        self.date = dafaultdate
        self.cookie = cookie


        if mode == '1':
            classmode = "tree"
            id =str(self.organization)
        if mode == '2':
            classmode = "tree"
            id =str(self.college)
        if mode == '3':
            classmode = "tree"
            id = str(self.school)
        else:
            classmode = "user" ## defalut
            id = str(self.myclass)
        print(id)
        res = json.loads(self._require_post(id).text)
        data = res.get("data")
        orgUserCount = data.get("orgUserCount") #总人数
        reportCount = data.get("reportCount") # 已经打卡人数
        print(data)
        if mode != "0":
            tree = data.get("tree")
            print(tree)
            for mumber in tree:
                name = mumber.get("tree_name")
                orgUserCount = mumber.get("orgUserCount")
                
                reportCount = mumber.get("reportCount")
                print(name,orgUserCount,reportCount)
        else:
            user = data.get("users")
            for mumber in user:
                user_name = mumber.get("user_name")
                user_sex = mumber.get("user_sex")
                isreport = mumber.get("is_report")
                print(user_name,user_sex,isreport)




if __name__ == "__main__":
    my = Search(user="202122100120",password="046430")
