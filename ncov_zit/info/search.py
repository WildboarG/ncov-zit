'''
Author: WildboarG
version: 1.0
Date: 2022-08-23 17:17:33
LastEditors: WildboarG
LastEditTime: 2022-08-24 14:32:19
Descripttion: 
'''

from . import *
from rich.table import Table
from rich import print

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
            "school":schoolcode,
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
        boost = path.split(",")
        return boost


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
        try:
            self.verify = self._get_verify()
            self.school = self._get_school()
            self.college = self._get_college()
            self.organization = self._get_organization()
            self.myclass = self._get_class()
        # print(self.school,self.college,self.organization,self.myclass)
            return 
        except:
            return "No verify"
        
    def _require_post(self,org_id):
        header = {
            'Content-Type':'application/json',
            'Cookie':self.cookie,
        }
        postdata = {
            "type":"org",
            "identity":"student",
            "para":{
            "organization_id":org_id,
            "organization_path_str":"0",
            },
            "date":self.date,
            "activityid":activityid,
            "flag":0,
            "domain":schoolcode,
            "stucode":self.user,
        }
        return requests.post(url=get_search_url,headers=header,json=postdata)

    def _mode_choose(self,idd)->str:
        if idd == "1":
            idd =str(self.organization)
        if idd == "2":
            idd =str(self.college)
        if idd == "3":
            idd = str(self.school)
        else:
            idd = str(idd)  ## 自定义id
        return idd
    ## get the punching environment
    def output_user(self,data):
        #print(data)
        try:
            allorgUserCount = data["orgUserCount"] #总人数
            allreportCount = data["reportCount"] # 已经打卡人数

            user = data.get("users")
            diagram = Table(show_header=True,header_style="Green")

            diagram.add_column("Tree_id",justify="center")
            diagram.add_column("Org_name",justify="center")
            diagram.add_column("Punch",justify="center")

            for mumber in user:
                user_name = mumber.get("user_name")
                user_sex = mumber.get("user_sex")
                isreport = mumber.get("is_report")
                diagram.add_row(str(user_name),str(user_sex),str(isreport))

            return diagram
        except:
            return 
    def output_tree(self,data):
        #print(data)
        try:
            allorgUserCount = data["orgUserCount"] #总人数
            allreportCount = data["reportCount"] # 已经打卡人数

            tree = data["tree"]
            chart = Table(show_header=True,header_style="bold magenta")

            chart.add_column("Tree_id",justify="center")
            chart.add_column("Org_name",justify="center")
            chart.add_column("Count",justify="center")
            chart.add_column("Signed",justify="center")
                
            for mumber in tree:
                tree_id = mumber["tree_id"]
                org_name = mumber["tree_name"]
                orgUserCount = mumber["orgUserCount"]
                reportCount = mumber["reportCount"]
                chart.add_row(str(tree_id),str(org_name),str(orgUserCount),str(reportCount))
            return chart
        except:
            return "[E] :Faild to get chart"
    
    ## cookie 必选
    ## orgid 可选参数 默认为class  可选 1 2 3 或者已经知道的班级或组织id
    ## orgtype 可选参数 默认是user 如 组织类型不是班级将改为tree
    ## dafaultdate 可选参数 默认是今天  格式 "2022-08-23"
    
    def get_feedback_user(self,cookie : str,dafaultdate=time.strftime("%Y-%m-%d")):
        self.set_verify()
        self.date = dafaultdate
        self.cookie = cookie
        self.org_id = self._mode_choose(str(self.myclass))
        res = json.loads(self._require_post(self.org_id).text)
        data = res.get("data")
        graphic = self.output_user(data)
        print(graphic)
       

    def get_feedback_tree(self,cookie : str, orgid :str,dafaultdate=time.strftime("%Y-%m-%d")):
        self.set_verify()
        self.date = dafaultdate
        self.cookie = cookie
        self.org_id = self._mode_choose(orgid)
        res = json.loads(self._require_post(self.org_id).text)
        data = res.get("data")
        graphic = self.output_tree(data)
        print(graphic)
       

