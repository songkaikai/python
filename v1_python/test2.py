# coding=utf-8
#第一个示例：简单的网页爬虫 
#爬取豆瓣首页 
  
import urllib.request  
import bs4
  
#网址  
url = "http://wwe.song2k.com/superStar"  
  
#请求  
request = urllib.request.Request(url)  
  
#爬取结果  
response = urllib.request.urlopen(request)  
  
data = response.read()  
  
#设置解码方式  
# data = data.decode('utf-8')  
  
#打印结果  
print(len(data))  
print(data)  
  
#打印爬取网页的各类信息  
  
print(type(response))  
print(response.geturl())  
print(response.info())  
print(response.getcode())  
print(bs4, 'cc')  
