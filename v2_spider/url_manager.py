# coding=utf-8

class UrlManager(object):
	# 构造函数
	def __init__(self): # url管理器要维护两个列表 
		self.new_urls = set() # 一个是没有爬取过的列表
		self.old_urls = set() # 一个是已经爬取过的列表

	def add_new_url(self, url): # 像管理器中添加新的url
		# print(url)
		if url is None:
			return
		if url not in self.new_urls and url not in self.old_urls:
			# print(url)
			self.new_urls.add(url) # 添加一个新的url
			# print(self.new_urls)

	def add_new_urls(self, urls): # 像管理器中批量添加新的url
		if urls is None or len(urls) == 0:
			return
		for url in urls:
			self.add_new_url(url)

	def has_new_url(self): # 判断是否有新的url
		# print(len(self.new_urls))
		return len(self.new_urls) != 0

	def get_new_url(self):
		new_url = self.new_urls.pop() # pop这个方法会从列表中获取一个url，切移除这个url
		self.old_urls.add(new_url)
		return new_url

	