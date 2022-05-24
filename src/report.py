from fuckzk import fuckzk
from .getverify import login
from .resportstatistic import *

def search_show(research,username,password):           
        cook = fuckzk.getid(username, password) 
        organization = login(username,password)
        organization_number = int(research)
        if (organization_number==1):
            org = organization[1]
            classmode = "tree" ## 默认查找组织  / 可查看班级
        elif(organization_number==2):
            org=organization[2]
            classmode = "tree" ## 默认查找组织  / 可查看班级
        elif(organization_number==3):
            org=organization[3]
            classmode = "tree" ## 默认查找组织  / 可查看班级
        elif(organization_number==4):
            org=organization[4]
            classmode="users"
        else:
            print("[E]you enter error!!!")
            exit(0) 
        get_report(cook,username,org,classmode)