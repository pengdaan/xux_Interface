__author__ = 'leo'
import requests
import json
url='http://www.xiaoshuxiong.com/test.php?act=genXsxToken'
Test_data={
    'uid':'43507844'
}

r=requests.get(url,params=Test_data)

result=r.text

try:
    js = json.loads(result)
    print(json.dumps(js,ensure_ascii=False,sort_keys=True,indent=10))
except:
    print (result)