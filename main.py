'''
Author: WildboarG
version: 1.0
Date: 2022-05-27 15:17:19
LastEditors: WildboarG
LastEditTime: 2022-05-28 13:37:19
Descripttion: 
'''
import sys
import json
import os
import csv
import getopt
import queue
import threading

from rich import print
from rich.table import Table

from info.login import GetMe
from info.post import sign

class User:
    def __init__(self,schoolcode:str) -> None:
        self.schoolcode = schoolcode
        self.q = queue.Queue()

    def __signed(self,username,password):
        info = []
        info.append(username)
        getme = GetMe(
            schoolcode = self.schoolcode,
            usernamme = username,
            password = password
        )

        cook,data = getme.get_lastdata()
        ## return status
        result = sign(data,cook)
        info.append(result)
        self.q.put(info)
    
    def adduser(self,username,password):
        print("[+]Add User: \nid:{}\npassword:{}\n".format(username,password))
        status = self.__signed()
        if str(status[1]) != "S":
            print("[red]添加失败：请检查帐号密码！[red]")
            return 
        else:
            ## 使用服务器定时时，要改为绝对路径
            with open("./config/user.csv","a") as f: 
                writter = csv.writer(f)
                writter.writerows([[self.username,self.password,self.schoolcode]])
                print("[green]添加成功！[green]")        
    def csv_sign(self):
        ## 创建队列，返回队列对象
        with open("./config/user.csv","r") as f:
            reader = csv.reader(f)
            readlist = list(reader)
        threads=[]
        res = []
        for row in readlist:
            try:
                # res = self.__signed(row[0],
                #             row[1]
                #     )
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

        while not self.q.empty():
            res.append(self.q.get())
        
        table = Table(show_header=True,header_style="bold magenta")
        table.add_column("Date",style="dim",width=12)
        table.add_column("Id",justify="center")
        table.add_column("Status",justify="center")
        for i in res:
            print(i)
            table.add_row(" Apr 14 2022",i[0],i[1])
        
        print(table)
    ## 创建一个个人测试的函数
    def test(self):
        pass
if __name__ == "__main__":
    #user = User()
    user = User("zit")
    user.csv_sign()