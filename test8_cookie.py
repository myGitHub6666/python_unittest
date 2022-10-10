import requests
# 获取验证码
re = requests.get("http://localhost/index.php?m=Home&c=User&a=verify")
print(re.cookies)
PHPSESSID=re.cookies.get("PHPSESSID")
# print(PHPSESSID)
# 设置cookies
cookies = {
    "PHPSESSID":PHPSESSID
}
# print(cookies)
# 登录
login_url = "http://localhost/index.php?m=Home&c=User&a=do_login"
login_data={
    "username":"15502984037",
    "password":"123456",
    "verify_code":8888
}
# print(login_data)
response = requests.post(url=login_url,data=login_data,cookies=cookies)
# print(response.json())
# 我的订单。每次进行操作的时候，必须携带cookies信息
re1 = requests.get("http://localhost/Home/Order/order_list.html",cookies=cookies)
print(re1.text)