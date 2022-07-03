#pip3 install requests
import requests
#pip3 install baidu_aip
from aip import AipOcr

image = requests.get('https://static.pandateacher.com/7b5d6d8d9dea5691705d04fef2306b52.png').content
#https://ai.baidu.com/tech/speech/tts，点击立即使用并登录百度智能云
#https://console.bce.baidu.com/ai/?_=1631439642026#/ai/speech/app/list
APP_ID = '24838083'
API_KEY = 'g8UoYNCBWBAaQwGRn0MMfhNu'
SECRET_KEY = 'yzepvbTBIU0LT19Npzq8FOig9q8z01gX'

client = AipOcr(APP_ID, API_KEY, SECRET_KEY)
res = client.basicGeneral(image)
if 'words_result' in res.keys():
    for item in res['words_result']:
        print(item['words'])
else:
    print(res)