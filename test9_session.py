import requests
# 创建session对象
session = requests.Session()
print("---------------------------",session)
# session 取验证码
session.get("http://localhost/index.php?m=Home&c=User&a=verify")
print("******************************************",session)
# 登录
login_url = "http://localhost/index.php?m=Home&c=User&a=do_login"
login_data={
    "username":"15502984037",
    "password":"123456",
    "verify_code":8888
}
# print(login_data)
session.post(url=login_url,data=login_data)
print(session)
# print(response.json())
# 我的订单。每次进行操作的时候，必须携带cookies信息
re1 = session.get("http://localhost/Home/Order/order_list.html")
print(re1.text)