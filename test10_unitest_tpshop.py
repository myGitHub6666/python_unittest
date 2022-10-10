# 导包
import requests
import unittest


# 创建测试类
class TPShopLogin(unittest.TestCase):  # 必须继承unittest类
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
    def test01_success(self):
        # 发送验证码
        response = self.session.get(url=self.verify_code_url)
        # 对验证码进行断言
        self.assertEqual(200, response.status_code)
        self.assertIn("image", response.headers.get("Content-Type"))
        # 发送登录请求
        login_data = {
            "username": "15502984037",
            "password": "123456",
            "verify_code": 8888
        }
        response = self.session.post(url=self.login_url,data=login_data)
        # print(response.json())
        # 对结果进行断言
        self.assertEqual(200,response.status_code)
        self.assertEqual(1,response.json().get("status"))
        self.assertIn("登陆成功",response.json().get("msg"))

    def test02_password_error(self):
        # 发送验证码
        response = self.session.get(url=self.verify_code_url)
        # 对验证码进行断言
        self.assertEqual(200, response.status_code)
        self.assertIn("image", response.headers.get("Content-Type"))
        # 发送登录请求
        login_data = {
            "username": "15502984037",
            "password": "12345",
            "verify_code": 8888
        }
        response = self.session.post(url=self.login_url, data=login_data)
        # print(response.json())
        # 对结果进行断言
        self.assertEqual(200, response.status_code)
        self.assertEqual(-2, response.json().get("status"))
        self.assertIn("密码错误", response.json().get("msg"))


    def test03_username_is_not_exist(self):
        # 发送验证码
        response = self.session.get(url=self.verify_code_url)
        # 对验证码进行断言
        self.assertEqual(200, response.status_code)
        self.assertIn("image", response.headers.get("Content-Type"))
        # 发送登录请求
        login_data = {
            "username": "15502984038",
            "password": "123456",
            "verify_code": 8888
        }
        response = self.session.post(url=self.login_url, data=login_data)
        # print(response.json())
        # 对结果进行断言
        self.assertEqual(200, response.status_code)
        self.assertEqual(-1, response.json().get("status"))
        self.assertIn("账号不存在", response.json().get("msg"))
