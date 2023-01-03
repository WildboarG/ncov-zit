
# ncov-zit

An automatic punch-in project based on Weishao's third-party application punch-in platform.

---

![PyPI - fuckzk](https://img.shields.io/pypi/wheel/fuckzk?label=fuckzk) ![PyPI - Python Version](https://img.shields.io/pypi/pyversions/fuckzk)  [![pypi_downloads_per_month](https://img.shields.io/pypi/dm/fuckzk)](https://pypi.org/project/fuckzk)  ![](https://img.shields.io/badge/License-MIT-reightgreen.svg) 



## 说明

基于微哨的第三方app的自动打卡“健康打卡平台”自动打卡实现 \
基于`python3`版本适用于`linux` `windows` `MacOs`

---

##### 🚀部署安装

```shell
git clone https://github.com/WildboarG/ncov-zit.git
```

##### 依赖

```shell
#python3.6+ 
pip3 install requirement.txt
```

   #####     配置

```python
/info/__init__.py
index = "所在学校的对微哨请求cookie的api"
host =  ...
refer = ...

authorityid= [自行抓包获取]
```



### 实现

- 利用`csv` 文件进行批量处理
- 利用`json` 文件进行批量处理

### 实例 

```shell
 oh_my-zit -u 学号 -p 密码 sign
```

### csv格式

```csv
学号1,密码,MIT
学号2,密码,MIT
学号3,密码,MIT
```

### json格式
```json
[
    {
        "username": "学号1",
        "password": "密码"
    },
    {
        "username": "学号2",
        "password": "密码"
    }
]
```

#### 其他

- 开箱即用
- 安装快捷脚本
```shell 
pip install ncov-zit
```
- 直接签到
```shell
oh_my-zit -u 学号 -p 密码 sign
```
- 批量签到
```shell
oh_my-zit -u 学号 -p 密码 sign -j json
oh_my-zit -u 学号 -p 密码 sign -c CSV 
```

- 修改签到地点
```shell
oh_my-zit -u 学号 -p 密码 sign -a "纽约市皇后区英格拉姆街20号"
```

## 查询
- 查询指定班级
```shell
oh_my-zit -u 学号 -p 密码 query {-m -s}
   -m 10376 班级id
   -s 为起始查询日期(Year-Month-Day)
```

- 查询指定组织/学院
```
oh_my-zit -u 学号 -p 密码 org {-g -s}
   -g 10000 组织id
   -s 为起始查询日期(Year-Month-Day)
```

## 返回值说明 
      Already Clocked 已经打卡
      Successlly 打卡成功
      其他情况视作失败，自行检查


 
## 说明
~~由于本校已经与2022年12月31日下线打卡系统，代码不再更新，感谢学校的一路陪伴。~~

## 📜 声明

---

本项目仅供学习与研究之用，请勿用于商业或非法用途。原作者不能完全保证项目的合法性，准确性和安全性，因使用不当造成的任何损失与损害，与原作者无关。请仔细阅读此声明，一旦您使用并复制了本项目，则视为已接受此声明,并承担可能引发的后果，请遵守开源协议。