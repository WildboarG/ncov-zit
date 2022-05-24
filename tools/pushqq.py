import requests
## qq群推送
##  配合go-cqhttp框架使用
def sendgroup(message):
    url = "http://127.0.0.1:5700/send_group_msg"
    data={
            "group_id":"xxxxxxxxx",##群号
            "message":message,
            "auto_escape":"false"
        }

    res = requests.post(url,data=data)
    print(res.text)
