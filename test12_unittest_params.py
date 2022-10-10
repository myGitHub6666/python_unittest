# 导包
import json

import requests
import unittest
from parameterized import parameterized


# 构建测试数据
def build_data():
    test_data1 = []
    file = "./data/login.json"
    with open(file, encoding='utf-8') as f:
        json_data = json.load(f)
        for test_data in json_data:
            username = test_data.get('username')
            password = test_data.get('password')
            verify_code = test_data.get('verify_code')
            status_code = test_data.get('status_code')
            status = test_data.get('status')
            msg = test_data.get('msg')
            test_data1.append((username, password, verify_code, status_code, status, msg))
        print(test_data)
    return test_data1


print(build_data())

# 创建测试类
class TPShopLogin2(unittest.TestCase):  # 必须继承unittest类
    # 初始化方法
    def setUp(self):
        # 实例化session对象
        self.session = requests.Session()
        # 定义登录接口url
        self.login_url = "http://localhost/index.php?m=Home&c=User&a=do_login"
        # 定义验证码接口url
        self.verify_code_url = "http://localhost/index.php?m=Home&c=User&a=verify"

    # 关闭session
    def tearDown(self):
        # 关闭session对象
        self.session.close()

    # 第一条测试用例。登录成功
    @parameterized.expand(build_data())
    def test01_login(self, username, password, verify_code, status_code, status, msg):
        # 发送验证码
        response = self.session.get(url=self.verify_code_url)
        # 对验证码进行断言
        self.assertEqual(200, response.status_code)
        self.assertIn("image", response.headers.get("Content-Type"))
        # 发送登录请求
        login_data = {
            "username": username,
            "password": password,
            "verify_code": verify_code
        }
        response = self.session.post(url=self.login_url, data=login_data)
        # print(response.json())
        # 对结果进行断言
        self.assertEqual(status_code, response.status_code)
        self.assertEqual(status, response.json().get("status"))
        self.assertIn(msg, response.json().get("msg"))
