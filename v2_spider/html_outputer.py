# coding=utf-8

# def为对外提供的方法
class HtmlOutputer(object): # 编写输出器的代码

	def __init__(self):
		self.datas = [] # 放列表

	def collect_data(self, data): # 用于收集数据
		if data is None:
			return
		self.datas.append(data)

	def output_html(self): # 将收集到的数据放到一个html文件中
		fout = open('output.html', 'w', encoding='utf-8') # w是写模式

		fout.write("<html>")
		# fout.write("<head>")
		# fout.write("<meta charset='utf-8' />")
		# fout.write("</head>")
		fout.write("<body>")
		fout.write("<table>")

		# head的默认编码是ascii要转变成utf-8防止乱码
		for data in self.datas: # 每一行的数据
			# print(data['summary'].encode('gbk').decode('gbk'))
			fout.write("<tr>")
			fout.write("<td>%s</td>" % data['url']) # 第一个输出data的url
			fout.write("<td>%s</td>" % data['title']) # 第二个输出data的title
			fout.write("<td>%s</td>" % data['summary']) # 第三个输出data的summary
			fout.write("</tr>")

		fout.write("</table>")
		fout.write("</body>")
		fout.write("</html>")

		fout.close() # 关闭

