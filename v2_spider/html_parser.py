# coding=utf-8

from bs4 import BeautifulSoup
import re
import urllib.parse

class HtmlParser(object):

	def _get_new_urls(self, page_url, soup): # 获取所有url连接
		new_urls = set() # 将结果传到一个列表里面
		# /item/GPL
		links = soup.find_all('a', href=re.compile(r'/item/\w+'))
		for link in links:
			new_url = link['href']
			# new_full_url = urlparse.urljoin(page_url, new_url) # 得到新的全的url
			new_full_url = urllib.parse.urljoin(page_url, new_url) # 得到新的全的url
			new_urls.add(new_full_url) # 
		return new_urls # 获取到页面中所有其他url的词条

	def _get_new_datas(self, page_url, soup): # 解析数据
		res_data = {} # 存放数据 词典

		# url也放入词典
		res_data['url'] = page_url

		# <dd class="lemmaWgt-lemmaTitle-title"><h1>Python</h1>
		title_node = soup.find('dd', class_='lemmaWgt-lemmaTitle-title').find('h1')
		res_data['title'] = title_node.get_text() # 获取标签里面的内容

		# <div class="lemma-summary" label-module="lemmaSummary">
		summary_node = soup.find('div', class_="lemma-summary")
		# summary_node = soup.find('title')
		res_data['summary'] = summary_node # 获取标签里面的内容
		# res_data['summary'] = summary_node.get_text() # 获取标签里面的内容
		# print(summary_node)

		return res_data

	# 解析出新的url列表和数据
	def parse(self, page_url, html_cont):
		if page_url is None or html_cont is None:
			return

		soup = BeautifulSoup(html_cont, 'html.parser')
		new_urls = self._get_new_urls(page_url, soup) # 解析出新的url列表
		new_data = self._get_new_datas(page_url, soup) # 解析出新的数据
		return new_urls, new_data # 并且返回