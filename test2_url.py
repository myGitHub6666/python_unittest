# 导包
import requests
# 发送请求
# response = requests.get("http://localhost/Home/Goods/search.html?q=iphone")
# 传递字符串
urlA="http://localhost/Home/Goods/search.html"
string1 = 'iphone'
response = requests.get(url=urlA,params= string1)
# 传递字典
dict1 = {'q':'iphone'}
response = requests.get(url=urlA,params= dict1)
# 查看响应
print(response.text)