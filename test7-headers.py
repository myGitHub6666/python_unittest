import requests
login_url="http://ihrm-java.itheima.net/api/sys/login"
login_header ={
    "content-type":"application/json"
}
login_data={
    "mobile":"13800000002",
    "password":"123456"
}
# 发送请求
re = requests.post(url=login_url,json=login_data,headers=login_header)
print(re.json())
# {'success': True, 'code': 10000, 'message': '操作成功！', 'data': '22c1f5be-dc79-421e-abb7-43370e3f7f15'}