import urllib.request
url = "https://www.baidu.com"

# url组成
# https://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=1&rsv_idx=1&tn=baidu&wd=%E5%91%A8%E6%9D%B0%E4%BC%A6
# http/https   www.baidu.com    80/443      s        wd = 周杰伦       #
#    协议           主机          端口号      路径         参数          锚点
# http 80
# https 443
# mysql 3306
# oracle 1521
# redis 637
# mongodb 27017

headers = {"User-Agent":
           "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 Edg/108.0.1462.54"}

# 因为urlopen方法中不能存储字典 所以headers不饿能传递进去
# 请求对象的定制
request = urllib.request.Request(url=url, headers=headers)
response = urllib.request.urlopen(request)
content = response.read().decode("UTF-8")
print(content)
