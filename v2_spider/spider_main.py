# coding=utf-8

# from v2_spider import url_manager, html_downloader, html_parser, html_outputer
import url_manager
import html_downloader
import html_parser
import html_outputer

class SpiderMain(object):
	def __init__(self):
		self.urls = url_manager.UrlManager() # url管理器
		self.downloader = html_downloader.HtmlDownloader() # 下载器
		self.parser = html_parser.HtmlParser() # 解析器
		self.outputer = html_outputer.HtmlOutputer() # 输出器

	def craw(self, root_url):
		count = 1 # 记录当爬取的是第几个url
		self.urls.add_new_url(root_url) # root_url添加进入url管理器
		# url管理器里面有了带爬取的url，我们就可以启动爬虫的循环
		while self.urls.has_new_url(): #当url管理器里面有待爬取的url的时候
			try: # 百度百科 很多页面没有摘要数据 要么就是某个url页面已经无法访问 因此要加入一个异常处理
				new_url = self.urls.get_new_url() # 就获取新的url
				print('craw %d : %s'%(count, new_url))
				html_cont = self.downloader.download(new_url) # 启动下载器来下载页面。
				# 下载好了页面我们调用解析器来解析这个页面数据
				# 得到新的url列表 以及新的数据 传入两个参数（当前爬取的url，以及下载好的页面数据）
				new_urls, new_data = self.parser.parse(new_url, html_cont) 
				self.urls.add_new_urls(new_urls) # 新的url添加进入url管理器
				self.outputer.collect_data(new_data) # 收集数据

				if count == 100: # 本代码的目标是爬取1000个页面 所以加一个判断
					break

				count = count + 1
			except: # 出现问题
				print('craw failed') # 代表爬取失败

			# 这样的话 如有有一个待爬取的url的话 我们的循环可以爬取相关的所有的页面
		self.outputer.output_html() # 调用这个方法来输出收集好的数据

if __name__ == '__main__': # 创建一个main函数
	root_url = 'https://baike.baidu.com/item/Python/407313?fr=aladdin' # 要爬去的入口url
	obj_spider = SpiderMain() # 创建一个spiderMain
	obj_spider.craw(root_url) # 调用craw来启动爬虫