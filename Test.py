import requests
import json
curl = 'https://oapi.dingtalk.com/robot/send?access_token=79bb1f7edee7cae15196270b185cb51b0fda3f6dfd4e4da668fd092766de9d4e'
headers = {
    'Content-Type': 'application/json',
    "Charset": "UTF-8"
}

# 构建请求数据，post请求
data = {
    'msgtype': 'text',
    'text': {
        'content': "域名：111"
    }
}

# 对请求的数据进行json封装
sendData = json.dumps(data)
sendData = sendData.encode('utf-8')

# 发送请求
response = requests.post(curl, data=sendData, headers=headers)
