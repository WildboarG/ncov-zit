import requests
import json


def login(user,password):
    ## @verify 验证值
    # @parent_id 页面值
    getverify_url="https://appservice.zit.edu.cn/whistlenew/index.php"
    params={
            "m":"user",
            "a":"userLogin",
            "password":password,
            "student_number":user,
            "school":"zit",
            "device_type":"android",
            }
    res = requests.get(url=getverify_url,params=params)
    respose = json.loads(res.text)
    data = respose.get("data")
    verify = data.get("verify")   ## 获得verify
    my_info=data.get("my_info")
    path = my_info.get("path")

    #print(path)
    pathcalss = path.split(",")
    all_college = pathcalss[1]
    my_college = pathcalss[2]
    my_organization = pathcalss[3]
    my_class = pathcalss[4]


    return verify,all_college,my_college,my_organization,my_class

