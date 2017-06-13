__author__ = 'leo'
import hashlib
import requests
url='http://www.xiaoshuxiong.com/test.php?act=setForRedis'
signs='wx_app_session_76383768'
import json
md5jm= hashlib.new("md5", signs).hexdigest()

print md5jm

test_data={
    'host':'10.0.0.150',
    'port':'6379',
    'key':'7bedb350c031ae40abab984c563d282d',
    'val':'{"unionId":"sb","userId":76383768,"userName":"3546650393"}'
}

r=requests.get(url,params=test_data)

result=r.text

try:
    js = json.loads(result)
    print(json.dumps(js,ensure_ascii=False,sort_keys=True,indent=10))
except:
    print (result)


  #  小树熊:http://wiki.corp.mama.cn/pages/viewpage.action?pageId=77435197