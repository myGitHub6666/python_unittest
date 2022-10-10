# 导包
import requests
# 发送请求
url1="http://localhost/index.php?m=Home&c=User&a=do_login"
login_data={
    "username":"15502984037",
    "password":"123456",
    "verify_code":"1234"
}
response = requests.post(url=url1,data=login_data)
# 响应数据
print(response.json())  # {'status': 0, 'msg': '验证码错误'}