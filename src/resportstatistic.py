import requests
import json
import time
from prettytable import PrettyTable
def get_report(cook,stu_code,organization,mode):
    url="https://lightapp.zit.edu.cn/api/reportstatistics/reportstatistics/getStatistical"
    head = {
        'Content-Type': 'application/json',
        'Cookie': cook,
    }
    if organization==None:
        organization_id = "0"
    else:
        organization_id = str(organization)
        #print(organization_id)
    date = time.strftime("%Y-%m-%d")
    admin = stu_code
    ports = {
     "type": "org",
    "identity": "student",
    "para": {
    "organization_id": organization_id,  ## 通过组织iD获取本班级打卡详情
    "organization_path_str":"0"
    },
    "date": date,
    "activityid": "2614",
    "flag": 0,
    "domain": "zit",
    "stucode":admin
}
    
    res = requests.post(url,headers=head,json=ports)
    res = json.loads(res.text)
    data = res.get("data")
    orgUserCount = data.get("orgUserCount")
    reportCount = data.get("reportCount")
    print("实际人员:"+str(orgUserCount)+"人\n"+"已打卡:"+str(reportCount)+"人\n")
    
    if (mode=="users"):
        users = data.get("users")
        status = ""
        unsigned_name = []
        y = PrettyTable(["Name", "sex", "status"])
        for mumber in users:
            user_name = mumber.get("user_name")
            user_sex = mumber.get("user_sex")
            is_report = mumber.get("is_report")
            text1=[]
            text1.append(user_name)
            text1.append(user_sex)
            text1.append(is_report)
            y.add_row(text1)
            if(is_report != 1):
            #    print("%+3s: 已签到" %user_name)
                unsigned_name.append(user_name)
            #    print("%+3s: 未签到" %user_name)
        print(y)
        if organization_id!="0":
            print("Unsigned："+str(unsigned_name))
    else: ## mode ==="tree"
        tree = data.get("tree")
        y = PrettyTable(["Colleges/Organization", "Need-Punch", "Already-Punch"])
        for mumber in tree:
            tree_name = mumber.get("tree_name")
            orgUserCount=mumber.get("orgUserCount")
            reportCount=mumber.get("reportCount")
            #print("组织机构："+tree_name+" | 需要签到人员："+str(orgUserCount)+" | 实际签到人数："+str(reportCount))
            text = []
            text.append(tree_name)
            text.append(orgUserCount)
            text.append(reportCount)
            y.add_row(text)
        print(y)
