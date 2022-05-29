# ncov-zit

An automatic punch-in project based on Weishao's third-party application punch-in platform.

---

![PyPI - fuckzk](https://img.shields.io/pypi/wheel/fuckzk?label=fuckzk) ![PyPI - Python Version](https://img.shields.io/pypi/pyversions/fuckzk)  [![pypi_downloads_per_month](https://img.shields.io/pypi/dm/fuckzk)](https://pypi.org/project/fuckzk)  ![](https://img.shields.io/badge/License-MIT-reightgreen.svg) 



## 说明

基于微哨的第三方app的自动打卡“健康打卡平台”的一个`CLI工具`实现 \
适用于大部分基于微哨开发的第三方合作平台。\
稍作修改即可食用用 \
基于`python3`版本适用于`linux` `windows` `MacOs`

---

##### 🚀部署安装

```shell
git clone https://github.com/WildboarG/ncov-zit.git
```

##### 依赖

```shell
#python3.6+ whth pip
pip3 install requirement.txt
```

##### 参数

```python3
-h : 查看帮助信息
-v ：版本号
-r : 查询打卡信息 参数为 （1,2,3,4）
-f : 添加本地的json文件
-m : 添加要打卡的表
-s : 添加推送方式 
-u ：学号
-p : 密码
```

🔏`json配置`字段说明

| 属性名 |  类型  | 必填 | 说明 |
|--------|-------|------|:-----|
|name|string|是|任意昵称用于打印输出的定位|
|stu_code|string|是|学号|
|password|string|是|密码|

`json`配置范例：
```json
[
    
  {
		"name":"用户1",
		"stu_code":"学号",
		"password":"密码"
  },
  {
		"name":"用户1",
		"stu_code":"学号",
		"password":"密码"
  }
    
]
```


## 实现

---

* 单步个人打卡

* 批量打卡

  * 使用`json`文件
  * 使用`mysql`

* 查询

  * 查询班级打卡

  * 查看你所在组织的打卡

  * 查看你所在学院的打卡

  * 查看所有学院的打卡

    

### CLI 工具

---

#### 上报功能

- 个人单步打卡

  ```shell
   python3 main.py -u 学号 -p 密码
  # 一般用来测试添加人员信息是否正确 也可以用来设置打卡
  ```

  

- 使用json文件实现批量打卡

  ```shell
  python3 main.py -f users.json
  ```

  

- 使用数据库实现批量打卡

  ```shell
  python3 main.py -m table ## table 是你存放数据的表
  # 数据库请自行配置config.ini 文件  tools目录下提供有工具
  ```

  

#### 查询上报情况

* 查询本班级打卡情况（未打卡名单会被返回）

  ```bash
  $ python3 main.py -r 4 -u 学号 -p 密码
  ```

  
#### 🔔消息通知
* 打卡结果会进行通知
  支持平台：
  
  ||用户通知|全局推送|备注|
  |---|:-:|:-:|---|
  |pushplus|✅|✅|需要微信订阅[pushplus](https://www.pushplus.plus/)公众号|
  |企业微信||||
  |Server 酱||✅|需要订阅[方糖](https://sct.ftqq.com/upgrade?fr=sc)|
   |CQHTTP|✅|✅|基于[go-cqhttp](https://github.com/Mrs4s/go-cqhttp)|
  |Qmsg 酱||||
  
  消息模板实例：
  ```text
    [S] Load user configuration....
    +-----------+--------------+------------------+
    |    Name   |    Userid    |      Status      |
    +-----------+--------------+------------------+
    |   大帅比  |  xxxxxxxxxxx | [S]Successfully  |
    |   大傻比  |  xxxxxxxxxxx | [S]Successfully  |
    +-----------+--------------+------------------+
  ```
  
  

#### 帮助

```shell
$ usage: main.py -h -v  [-m <tables> -f <users.json> -r <mode> -u <username> -p <password> -s <pushmode>]
 -h: Print help info
 -f: Add and use jsonfile
 -v: Print version information
 -m: Add yours database
 -s: Select any push method
 -r: Check today's clock out
      1.All college
      2.Whole colleges
      3.Organization
      4.Your's class
```

## 📜 声明
---
本项目仅供学习与研究之用，请勿用于商业或非法用途。原作者不能完全保证项目的合法性，准确性和安全性，因使用不当造成的任何损失与损害，与原作者无关。请仔细阅读此声明，一旦您使用并复制了本项目，则视为已接受此声明,并承担可能引发的后果，请遵守开源协议。
