
import argparse
import csv
import json
import time
import queue
import threading


from rich import print
from rich.table import Table

from .info.login import GetContent
from .info.post import sign as signn
from .info.search import Search

class User:
    def __init__(self,schoolcode:str,username:str,password:str) -> None:
        self.schoolcode = schoolcode
        self.username = username
        self.password = password
        self.q = queue.Queue()


    def _get_data(self,information:GetContent):
        return information.reporter()

    def __signed(self,username,password):
        info = []
        info.append(username)
        sign_content = GetContent(
            schoolcode = self.schoolcode,
            username = username,
            password = password,
        )
        cook = sign_content.rel_cookie()
        data = sign_content.reporter(cook,mylocal='0')
        ## return status
        result = signn(data,cook)
        info.append(result)
        self.q.put(info)
    
      
    
    def _output_table(self,information :list)->Table:
        table = Table(show_header=True,header_style="bold magenta")
        for i in information:
            table.add_column(i,justify="center")
        return table
    
    def _print_table(self,table:Table)->str:
        print(table)

    def _json_crate_Threads(self,jsonfile:list):
        threads=[]
        for row in jsonfile:
            user = row["username"]
            password = row["password"]
            print(user+password)
            try:
                threads.append(
                        threading.Thread(
                            target=self.__signed,
                            args=(user,password
                            )
                        )
                    )
            except:
                pass
        for t in threads:
            t.start()
        
        for t in threads:
            t.join()


    def _cvs_crate_Threads(self,rows:list):
        threads=[]
        for row in rows:
            #print(row[0],row[1])
            try:
                threads.append(
                        threading.Thread(
                            target=self.__signed,
                            args=(str(row[0]),str(row[1])
                            )
                        )
                    )
            except:
                pass
        for t in threads:
            t.start()
        
        for t in threads:
            t.join()
    
    def csv_sign(self,csvfire):
        ## 创建队列，返回队列对象
        with open(csvfire,"r") as f:
            reader = csv.reader(f)
            readlist = list(reader)
        
        res = []        
        self._cvs_crate_Threads(readlist)

        while not self.q.empty():
            res.append(self.q.get())
        

        table = self._output_table(["ID","Status","Node"])
        for i in res:
            table.add_row(i[0],i[1],"123")

        self._print_table(table)

    ## json格式
    def json_sign(self,fire):
        ## 创建队列，返回队列对象
        with open(fire,"r") as f:
            reader = json.load(f)
                
        res = []        
        self._json_crate_Threads(reader)

        while not self.q.empty():
            res.append(self.q.get())
        

        table = self._output_table(["ID","Status","Node"])
        for i in res:
            table.add_row(i[0],i[1],"hahaha")
        self._print_table(table)

    ## 查询
    def find_me(self, myclass="4",date=time.strftime("%Y-%m-%d")):
        bin = GetContent(
            schoolcode = self.schoolcode,
            username = self.username,
            password = self.password,
        )

        cook = bin.rel_cookie()
        _search = Search(user=self.username,password=self.password)
        _search.get_feedback_user(cookie=cook,classid=myclass,dafaultdate=date)
        return 
    def find_org(self,org="1",date=time.strftime("%Y-%m-%d")):
        bin = GetContent(
            schoolcode = self.schoolcode,
            username = self.username,
            password = self.password,
        )

        cook = bin.rel_cookie()
        _search = Search(user=self.username,password=self.password)
        _search.get_feedback_tree(cookie=cook,orgid=org,dafaultdate=date)
        return 
    
    def test(self,mylocal="0"):
        my = GetContent(
            schoolcode = self.schoolcode,
            username = self.username,
            password = self.password,

        )
        cook = my.rel_cookie()
        data = my.reporter(cook,mylocal)
        print(signn(data,cook))
        return        
def main():
    parser = argparse.ArgumentParser(
            description=
    "A cov cli tool for ZIT(zhengzhou Institute of Science and Technology)",
            epilog=
            "(c) 2021 mm62633482@gmail.com",
    )
    parser.add_argument("-u","--username",help="The username",required=True)
    parser.add_argument("-p","--password",help="The password",required=True)
    #parser.add_argument("-f","--file",help = "use json file",required=True) 
    subparsers = parser.add_subparsers(dest="command")
    sign = subparsers.add_parser("sign",help="Officially Signed in today")
    sign.add_argument(
            "-j",
            "--json",
            help="Load a file of type Json"
            )
    sign.add_argument(
            "-c",
            "--csv",
            help="Load a file of type CSV"
            )
    sign.add_argument(
            "-a",
            "--address",   
            help="Modify your address" 
    )
    # search report
    query = subparsers.add_parser("query",help="query history of the user report")
    query.add_argument(
            '-m',
            '--myclass',
            help= "Query the specified class"
            )
    query.add_argument(
            '-s',
            '--start_time',
            help= "the start time of report history(Year-Month-Day)"
            )

    org = subparsers.add_parser("org",help="query history of the the organization report")
    org.add_argument(
            '-g','--organization_id',
            help ="""
            search all organization report:\n
                    "13096" :   "all", \n
                    "14223" :   "体育",\n
                    "14124" :   "电气",\n 
                    "14125" :   "机械",\n
                    "14126" :   "计科",\n
                    "14127" :   "工商",\n
                    "14129" :   "艺术",\n
                    "14131" :   "中专",\n
                    "14132" :   "土木",\n
                    "14133" :   "交通",\n
                    "14134" :   "食科",\n
                    "14135" :   "舞蹈",\n
                    "14136" :   "外语",\n
                    "14137" :   "国标",\n
                    "14139" :   "空乘",\n
            """)
    org.add_argument(
            '-s','--start_time',
            help = "the start time of report history(Year-Month-Day)"
            )

    args = parser.parse_args()

    ## check command
    if not args.command or args.command not in {"query","org","sign"}:
        parser.print_help()
        exit()
    ## new a zit user obj
    user = User("zit",args.username,args.password)
    
    if args.command == "sign":
        if args.json:
            user.json_sign(args.json)
            exit()
        if args.csv:
            user.csv_sign(args.csv)
            exit()
        if args.address:
            user.test(mylocal=args.address)
            exit()
        else:
            user.test()
            exit()

    if args.command == "query":
        if args.myclass and args.start_time:
            user.find_me(myclass=args.myclass,date=args.start_time)
        if args.myclass:
            user.find_me(myclass=args.myclass)
            exit()
        if args.start_time:
            user.find_me(date=args.start_time)
            exit()
        else:
            user.find_me()
            exit()
    if args.command == "org":
        if args.organization_id and args.start_time:
            user.find_org(org=args.organization_id,date=args.start_time)
            exit()
        if args.organization_id:
            user.find_org(org=args.organization_id)
            exit()
        if args.start_time:
            user.find_org(date=args.start_time)
            exit()
        else:
            user.find_org()
        exit()

if __name__ == "__main__":
    main()
