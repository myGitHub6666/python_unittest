# 导包
import requests
# 访问百度首页的接口，获取响应数据
re = requests.get("https://www.baidu.com")
print(re.text)
# 获取响应状态码
print(re.status_code)
# 获取请求url
print(re.url)
# 获取响应字符编码
print(re.encoding)
# 获取响应头数据
print(re.headers)
# 获取响应头数据中的content—type,这里忽略大小写？？？
print(re.headers.get("content-type"))
# 获取响应的cookie
print(re.cookies)
# 获取指定cookie
print(re.cookies.get("BDORZ"))
# 获取文本形式的响应内容
print(re.text)
# 获取字节形式的响应内容
print(re.content)
# 获取指定字节形式的响应内容
print(re.content.decode("utf-8"))
