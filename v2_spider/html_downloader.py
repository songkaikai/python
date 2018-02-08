# coding=utf-8
import urllib.request

class HtmlDownloader(object):
	def download(self, url):
		if url is None:
			return None

		#爬取结果  
		response = urllib.request.urlopen(url)

		if response.getcode() != 200:
			return None

		# print()
		return response.read()