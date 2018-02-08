# coding=utf-8

from bs4 import BeautifulSoup
import re

html_doc = "<p class='title'>The BeautifulSoup4 title 你好</p><a href='http://www.baidu.com'>i want to baidu.com</a><a href='http://www.douyu.com'>my name is douyu.com</a><a href='http://www.taobao.com'></a><a href='http://www.yy.com'></a>";

# 创建对象
# soup = BeautifulSoup(html_doc, 'html.parser', from_encoding='urf-8')
soup = BeautifulSoup(html_doc, 'html.parser')

print('获取所有链接')
links = soup.find_all('a')
for link in links:
	print(link.name, link['href'], link.get_text())

print('获取baidu的链接')
link_node = soup.find('a', href='http://www.baidu.com')
print(link_node.name, link_node['href'], link_node.get_text())
print(link_node)

print('正则匹配')
link_re = soup.find('a', href=re.compile(r'dou'))
print(link_re.name, link_re['href'], link_re.get_text())

print('获取P段落文字')
p_node = soup.find('p', class_='title')
print(p_node.name, p_node.get_text())

str = "菜鸟教程";
str_utf8 = str.encode("UTF-8")
str_gbk = str.encode("GBK")

print(str)

print("UTF-8 编码：", str_utf8)
print("GBK 编码：", str_gbk)

print("UTF-8 解码：", str_utf8.decode('UTF-8','strict'))
print("GBK 解码：", str_gbk.decode('GBK','strict'))