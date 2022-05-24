import re
import pymysql
from configparser import ConfigParser
import os

def create():  ## 创建一张表
    config = ConfigParser()
    file_path = os.path.join(os.path.abspath('./config/'),'config.ini')
    if not os.path.exists(file_path):
        raise FileNotFoundError("No found config file")
    config.read(file_path)
    DBHOST = config.get('db','dbhost')
    DBNAME = config.get('db','dbname')
    DBPASS = config.get('db','dbpass')
    DBUSER = config.get('db','dbuser')
    try:
        db = pymysql.connect(DBHOST,DBUSER,DBPASS,DBNAME,charset='utf8')
        print("数据库链接成功！")
        cur = db.cursor()
        cur.execute("DROP TABLE IF EXISTS dbtest")
        sql ='CREATE TABLE dbmyclass(Name CHAR(20) NOT NULL, Userid CHAR(12) NOT NULL, Password CHAR(32))'
        cur.execute(sql)
        print("表格创建成功！！")
    except pymysql.Error as e:
        print("表格创建失败："+str(e))
    db.close()
def insert():
    try:
        db = pymysql.connect(DBHOST,DBUSER,DBPASS,DBNAME,charset='utf8')
        print("数据库链接成功！")
        cur = db.cursor()
        sql ='INSERT INTO dbmyclass(Name, Userid, Password) VALUE (%s,%s,%s)'
        value=('大帅比','学号','密码')
        cur.execute(sql,value)
        db.commit()
        print("插入成功！！")
        db.close()
        return "添加成功"
    except pymysql.Error as e:
        print("表格插入失败："+str(e))
        db.rollback()
        db.close()
        return "添加失败"
    
def select():
    try:
        db = pymysql.connect(DBHOST,DBUSER,DBPASS,DBNAME,charset='utf8')
        print("数据库链接成功！")
        cur = db.cursor()
        sql ='SELECT * FROM dbmyclass'
        cur.execute(sql)
        results = cur.fetchall()
        for row in results:
            name=row[0]
            userid=row[1]
            password=row[2]
        print("name : %s\nuserid:%s\npassword:%s"%(name,userid,password))
    except pymysql.Error as e:
        print("表格查询失败："+str(e))
    
    db.close()
def update():
    try:
        db = pymysql.connect(DBHOST,DBUSER,DBPASS,DBNAME,charset='utf8')
        print("数据库链接成功！")
        cur = db.cursor()
        sql ='update dbmyclass set Name=%s where Name=%s'
        value=('wildboarG','大帅比')
        cur.execute(sql,value)
        db.commit()
        print("数据更新成功！！")
    except pymysql.Error as e:
        print("表格更新失败："+str(e))
    db.close()
def delete():
    try:
        db = pymysql.connect(DBHOST,DBUSER,DBPASS,DBNAME,charset='utf8')
        print("数据库链接成功！")
        cur = db.cursor()
        sql ='delete from dbmyclass where Name!=NULL'
        #value=('大帅比')
        cur.execute(sql)
        db.commit()
        print("数据删除成功！！")
    except pymysql.Error as e:
        print("表格删除失败："+str(e))
def insertt(name,userid,password):
    try:
        db = pymysql.connect(DBHOST,DBUSER,DBPASS,DBNAME,charset='utf8')
        print("数据库链接成功！")
        cur = db.cursor()
        sql ='INSERT INTO dbmyclass(Name, Userid, Password) VALUE (%s,%s,%s)'
        value=(name,str(userid),str(password))
        cur.execute(sql,value)
        db.commit()
        print("插入成功！！")
    except pymysql.Error as e:
        print("表格插入失败："+str(e))
        db.rollback()
    db.close()

if __name__ == "__main__":
    #create()
    #insert()
    #update()
    #delete()
    select()
