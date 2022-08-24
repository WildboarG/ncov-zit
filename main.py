'''
Author: WildboarG
version: 1.0
Date: 2022-05-27 15:17:19
LastEditors: WildboarG
LastEditTime: 2022-08-24 14:36:34
Descripttion: 
'''
import csv
import queue
import threading

from rich import print
from rich.table import Table

from info.login import GetContent
from info.post import sign
from info.search import Search

class User:
    def __init__(self,schoolcode:str) -> None:
        self.schoolcode = schoolcode
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
        cook = sign_content.rel_cookie
        data = self._get_data(sign_content)
        ## return status
        result = sign(data,cook)
        info.append(result)
        self.q.put(info)
    
      
    
    def _output_table(self,information :list)->Table:
        table = Table(show_header=True,header_style="bold magenta")
        for i in information:
            table.add_column(i,justify="center")
        return table
    
    def _print_table(self,table:Table)->Table:
        print(table)

    def _crate_Threads(self,rows:list):
        threads=[]
        for row in rows:
            try:
                threads.append(
                        threading.Thread(
                            target=self.__signed,
                            args=(row[0],row[1]
                            )
                        )
                    )
            except:
                pass
        for t in threads:
            t.start()
        
        for t in threads:
            t.join()
    
    def csv_sign(self):
        ## 创建队列，返回队列对象
        with open("./config/user.csv","r") as f:
            reader = csv.reader(f)
            readlist = list(reader)
        
        res = []        
        self._crate_Threads(readlist)

        while not self.q.empty():
            res.append(self.q.get())
        

        table = self._output_table(["ID","Status","Node"])
        for i in res:
            table.add_row(i[0],i[1],"123")

        self._print_table(table)
    ## 创建一个个人测试的函数
    def find(self,username,password)->str:
        bin = GetContent(
            schoolcode = self.schoolcode,
            username = username,
            password = password,
        )
        cook = bin.rel_cookie()
        #data = bin.reporter()
        #print(sign(data,cook))
        my = Search(user=username,password=password)
        my.get_feedback(cookie=cook,orgid="2",orgtype="tree",dafaultdate="2022-08-24")
if __name__ == "__main__":
    #user = User()
    user = User("zit")
    ## csv 批量打卡 
    user.csv_sign()
    ## 结果查询，传入学号密码，以及查询类型
    user.find("xxx","xxx")
