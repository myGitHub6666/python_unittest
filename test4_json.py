# 导包
import requests
# 发出请求
# 目前接口地址变了。把test改成java
url1="http://ihrm-java.itheima.net/api/sys/login"
login_data={
    "mobile":"13800000002",
    "password":"123456"
}
response=requests.post(url=url1,json=login_data)
# 响应数据
print(response.json())
# {'success': True, 'code': 10000, 'message': '操作成功！', 'data': '8652639b-af9f-4bb3-9a34-590ef57933a9'}