import requests

##  打卡请求post
def post(data,cook):
    post_url = 'https://lightapp.zit.edu.cn/api/questionnaire/questionnaire/addMyAnswer'
    head = {
        'Content-Type': 'application/json',
        'Cookie': cook,
    }
    try:
        data = requests.post(url=post_url, json=data, headers=head).json()
        if data.get("errcode") == 0:
            #print("打卡成功！")
            return "[S]Successfully"
        else:
            #print("---未知的errcode\n" + str(data) + "\n")
            return "[S]Already Clocked"
    except:
        return "[E]:Unknown"

