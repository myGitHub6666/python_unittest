# 导包
import requests
# 发送请求
response = requests.get("https://baidu.com")
# 查看响应
print(f"原始的数据编码格式是：{response.encoding}")
print(f"设置前的响应数据：{response.text}")
# 设置响应数据格式
response.encoding = "utf-8"
print(f"设置后的响应格式是：{response.encoding}")
print(f"设置后的响应数据是：{response.text}")