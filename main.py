# -*- coding:UTF-8 -*-
import sys
import json
import time
import os
import getopt


from tools import *
from src import *
from fuckzk import fuckzk
from prettytable import PrettyTable 
from configparser import ConfigParser
import threading
import queue

## 引入线程队列使得程序可以并行运行大幅度节省时间

## use mysql-test-myclass database
def get_config():
    config = ConfigParser()
    file_path = os.path.join(os.path.abspath('/root/work/github/ncov-zit/config'),'config.ini')
    print(file_path)
    if not os.path.exists(file_path):
        raise FileNotFoundError("No found config file")
    config.read(file_path)
    DBHOST = config.get('db','dbhost')
    DBNAME = config.get('db','dbname')
    DBPASS = config.get('db','dbpass')
    DBUSER = config.get('db','dbuser')
    return DBHOST,DBNAME,DBPASS,DBUSER

## Get information from myclass
## Call the login module to get cookies ,Take COOKIES to get yesterday's information when call the getdata module, Reorganize submitted information, And Call the post module .
## Return the result and print it beautifully


def version(): 
    print(" ncov-zit-report v0.1    \n by: mm62633482@gmail.com")

def usage():
    print("\nusage: main.py -h -q -v -m [-r <mode> -u <username> -p <password>]\n -h: Print help info \n -v: Print version information \n -m: Use database tables \n -s Push respose connect [pushplus,pushqq]\n -r: Check today's clock out \n      1.All college\n      2.Whole colleges\n      3.Organization\n      4.Your's class")

q = queue.Queue()

def runandpretty(name,username,password):
    cook = fuckzk.getid(username,password)
    mydata = fuckzk.getme(username,cook)
    res = post(mydata,cook)
    text = []
    text.append(name)
    text.append(username)
    text.append(res)
    if res[0:3]=="[S]":   
        sign = 1
        
    else:
        sign = 0 
    text.append(sign) 
    if res[0:3]=="[E]":
        unpron = username
        text.append(unpron)
    else:
        pass


    q.put(text)
 

def sql_report(tables):
    data = get_config()
    try:
        db = pymysql.connect(data[0],data[1],data[2],data[3],charset='utf8')
        print("[S]: Successfully connected to database.")
        cur = db.cursor()
        sql ='SELECT * FROM {}'.format(tables)
        cur.execute(sql)
        results = cur.fetchall()
        print("[S]: Successfully get myclass.")
        table = PrettyTable(["Name","Userid","Status"]) 
        sign=0
        unpron=[]
        threads = []
        result = list
        start = time.time()
        for row in results:
            name,qq,username,password =row
            threads.append(
                        threading.Thread(target=runandpretty,args=(name,username,password))
                    )
            
        
        for thread in threads:
            thread.start()
            
            
        for thread in threads:
            thread.join()
        
        while not q.empty():
            result.append(q.get()) 

        for item in result: 
            try:
                table.add_row([item[0],item[1],item[2]])
                sign += item[3]
                if item[4] == 0:
                    unpron.append(item[4])          
            except Exception as e:
                pass

        print("\n") 
        end = time.time()     
        print(table)
        print("time:",end-start)
    except pymysql.Error as e:
        print("[E]:"+str(e))
    db.close() ## shutdown database
    return sign,len(results),unpron

def main(argv):
    try:
        opts,args = getopt.getopt(argv,"hvm:s:f:r:u:p:",["help","version","multi=","send=","filee=","research=","username=","password="])
    except getopt.GetoptError:
        usage()
        sys.exit(2)
    
    for opt,arg in opts:
        if opt in ("-h","--help"):
            usage()
            sys.exit()
        elif opt in ("-v", "--version"):
            version()
            sys.exit()
        elif opt in ("-m","--multi"):
            multi = arg
        elif opt in ("-s","--send"):
            send = arg
        elif opt in("-f","--filee"):
            filee = arg
        elif opt in ("-r", "--research"):
            research = arg
        elif opt in ("-u", "--username"):
            username = arg
        elif opt in ("-p", "--password"):
            password = arg
    
    def usertest(username,password):
        table = PrettyTable(["Name","Userid","Status"])
        name ="TESTER"
        text = runandpretty(name,username,password)
        table.add_row(text)
        print(table)
        sys.exit()
           
    def all_report(filename):
        start = time.time()
        path = os.getcwd()
        if path.find("/ncov-zit") == -1:
            path+="/ncov-zit"
        info =json.load(open(path + "/config/"+"users.json",encoding="utf-8")) 
        print("[S] Load user configuration....")
        table = PrettyTable(["Name","Userid","Status"])  
        unpron = []
        sign = 0
        threads = []
        result = []
        for item in info:
            #print(item)
            name = item.get('name')
            password=item.get("password")
            username = item.get('stu_code')
         
            threads.append(
                        threading.Thread(target=runandpretty,args=(name,username,password))
                    )
        
        for thread in threads:
            thread.start()
            
            
        for thread in threads:
            thread.join()
            
        while not q.empty():
            result.append(q.get()) 

        for item in result: 
            try:
                table.add_row([item[0],item[1],item[2]])
                sign += item[3]
                if item[4] == 0:
                    unpron.append(item[4])          
            except Exception as e:
                pass
        print(table)
        end = time.time()
        print("time:",end-start)
        return  sign,len(info),unpron

    if 'username' in locals().keys() and 'password' in locals().keys():
        if 'research' in locals().keys():  ## 查询方式1,2,3,4
            search_show(research, username, password) 
            sys.exit() 
        else:  ## 单步打卡
            usertest(username,password)
        sys.exit()

    if 'filee' in locals().keys():  ## 传入json文件方式批量打卡
        if 'send' in locals().keys():
            if send=="pushqq":
                message = all_report(filee)
                sendgroup(message)
            if send == "pushplus":
                message = all_report(filee)
                pushall(message) # use markdown
            if send == "serverchan":
                message = all_report(filee)
                push(message) # use markdown  
            sys.exit()
        else:
            all_report(filee)
            sys.exit()
    if 'multi' in locals().keys():  ## 传入传入数据库中的某一张表 批量打卡 multi 为表的名字
        if 'send' in locals().keys():
            if send=="pushqq":
                message = sql_report(multi)
                sendgroup(message)
            if send == "pushplus":
                message = sql_report(multi)
                pushall(message) # use markdown
            if send == "serverchan":
                message = sql_report(multi)
                push(message) # use markdown  
            sys.exit()
        else:
            sql_report(multi)
            sys.exit()

    else:
        usage()
        
if __name__=="__main__":
    main(sys.argv[1:])
