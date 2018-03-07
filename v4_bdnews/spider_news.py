# coding=utf-8 
# 声明编码方式 默认编码方式ASCII 参考https://www.python.org/dev/peps/pep-0263/  

import urllib.request
# python os模块 常用命令
# https://www.cnblogs.com/kaituorensheng/archive/2013/03/18/2965766.html
import os  
# Python中time模块详解(转)
# https://www.cnblogs.com/qq78292959/archive/2013/03/22/2975786.html
import time  
import re # 引入正则表达式
# windows 下载 http://www.runoob.com/python3/python3-mysql.html
# PyMySQL 是在 Python3.x 版本中用于连接 MySQL 服务器的一个库，Python2中则使用mysqldb。
# ubuntu 下载 http://blog.csdn.net/RobertChenGuangzhi/article/details/49174523
import pymysql # 引入python操作mysql的标准库

'''
本案例为抓取百度新闻词条内容
网站地址：http://news.baidu.com/
'''

'''
实现思路：
	1.
'''

# 获取当前时间 年月日时分秒
timeArr = time.localtime()
# 由于这个日和月在多个地方都要用到，所以县进行保存
subPath = str(timeArr.tm_mon) + '_' + str(timeArr.tm_mday)

# 判断当天的文件夹是否已经存在，如果没有就创新新的子文件用来保存当前的图片
print(os.listdir('./bdPicture'))

subDirPath = './bdPicture/Picture_' + subPath
if os.path.isdir(subDirPath) :
	print('[-] dir is already existence!!!')
else :
	os.mkdir(subDirPath)
	print('[+] dir Create success!!!')
	
# 服务器存放图片的文件夹 windows
# C:/xampp/htdocs/images 这个前面的路径可以随你的路径改变
serviceDir = 'C:/xampp/htdocs/images/bdPicture/Picture_' + subPath
if os.path.isdir(serviceDir) :
	print('[-] dir is already existence!!!')
else :
	os.mkdir(serviceDir)
	print('[+] dir Create success!!!')

# exit()为python内置的退出程序的函数
# exit()

# 连接数据库 user为账户 passwd为密码 db需要访问的数据库名称
conn = pymysql.connect(host="127.0.0.1",port=3306,user="root",passwd="",db="database",charset="utf8")
# 获取游标
cursor = conn.cursor()

# 创建当天的文本文件用来存储所有爬取的网页信息
textWrite = open('baidu_news_' + subPath + '.txt', 'w', encoding='utf-8') #以二进制格式写的方式打开txt文件
textWrite.write('************获取百度新闻词条信息************\r\n')

url = 'http://news.baidu.com/' # 首页路径

print('spider: ' + url) # 打印出当前要爬取的首页url

# 获取网页源码
newsPage = urllib.request.urlopen(url).read() # 下载页面并读取页面内容
# baijia.baidu.com
# 把网页内容编码成utf-8格式
# 因为百度知道是gbk编码格式的
# 先把抓取下来的内容解码成gbk
# 然后把内容里的字符集替换成utf-8
# 编码为utf-8格式.打开的网页就会已utf-8编码格式显示
# encodeStrToUtf8 = newsPage.decode('gbk').replace('charset=gbk', 'charset=utf-8', 1).encode('utf-8')
# print(encodeStrToUtf8);
# 由于初学者本来想抓取百家内容结果发现无法抓取待后续更新
newsTxt = open('baidu_news.html', 'wb') #以二进制格式写的方式打开html文件
newsTxt.write(newsPage) # 把整个抓取的页面放入txt文件
newsTxt.close() # 关闭打开的txt文件

# 打印输出当前爬取的网页内容
# print(newsPage); 

# 要抓取的内容段
'''
	<ul class="ulist bdlist">
	<li class="bold-item"><a href="https://baijia.baidu.com/s?id=1589357928177452138" target="_blank" mon="a=9">用户隐私不可侵犯，但巨头也有躺枪的时候！</a><a href="" target="_blank" mon="a=9" class="name"></a></li>
	<li><a href="https://baijia.baidu.com/s?id=1589353527783164460" target="_blank" mon="a=9">面对“水涨船高”的数字货币，谷歌、亚马逊等巨头也不淡定了？</a><a href="" target="_blank" mon="a=9" class="name"></a></li>
	<li><a href="https://baijia.baidu.com/s?id=1589348252860670209" target="_blank" mon="a=9">高潮之后面临困境，无人货架的出路何在？</a><a href="" target="_blank" mon="a=9" class="name"></a></li>
	<li><a href="https://baijia.baidu.com/s?id=1589347652686032193" target="_blank" mon="a=9">估值70亿的得到APP，能等到上市吗？</a><a href="" target="_blank" mon="a=9" class="name"></a></li>
	<li><a href="https://baijia.baidu.com/s?id=1589345000820801027" target="_blank" mon="a=9">CES2018不是手机主场 但却是中国手机品牌的主场</a><a href="" target="_blank" mon="a=9" class="name"></a></li>
	</ul>
	<ul class="ulist bdlist" style="padding-top:5px">
	<li class="bold-item"><a href="https://baijia.baidu.com/s?id=1589342675394214097" target="_blank" mon="a=9">区块链技术赋能，数字货币或将迎来大发展</a><a href="" target="_blank" mon="a=9" class="name"></a></li>
	<li><a href="https://baijia.baidu.com/s?id=1589340807175135294" target="_blank" mon="a=9">美团滴滴摩拜约战，出行秩序会再次洗牌吗？</a><a href="" target="_blank" mon="a=9" class="name"></a></li>
	<li><a href="https://baijia.baidu.com/s?id=1589316342933916757" target="_blank" mon="a=9">王思聪撒币，冲顶大会登顶、直播答题带来的中国互联网加速</a><a href="" target="_blank" mon="a=9" class="name"></a></li>
	<li><a href="https://baijia.baidu.com/s?id=1589271212991619642" target="_blank" mon="a=9">库克向巴菲特推荐iPhone遭拒绝：全世界的人都买了我再买</a><a href="" target="_blank" mon="a=9" class="name"></a></li>
	<li><a href="https://baijia.baidu.com/s?id=1589271092424685515" target="_blank" mon="a=9">华为手机借AT&amp;T进军美国失败，为何苹果成为中国打不死的小强</a><a href="" target="_blank" mon="a=9" class="name"></a></li>
	</ul>
'''
# 编写需要抓取的内容的正则表达式
# res_box = r'<ul class="ulist bdlist"(( style="padding-top:5px")?>.*?)</ul>'
res_box = r'<ul class="ulist bdlist"(.*?)</ul>'
# 进行抓取匹配的内容,内容先解码成utf-8
m_box = re.findall(res_box, newsPage.decode('utf-8'), re.S|re.M)
# print(m_box)
# 把获取到的匹配内容写入txt文件
# textWrite.write(str(m_box)) 

# 循环获取每段匹配内容的标题和url路径
for line in m_box:
	# 编写获取当前内容块的每条数据的正则表达式
	res_li = r'<li>(.*?)</li>'
	li_box = re.findall(res_li, line, re.S|re.M)
	# print(str(li_box)) 
	# 获取每条数据的内容
	for detail in li_box:
		title_str = r'<a href="(.*?)" target="_blank" mon="a=9">(.*?)</a>'
		# 把表达式字符串变异成表达式对象,可以反复使用
		title_ex = re.compile(title_str, re.S|re.M)
		# 获取里面的标题和url
		title_obj = title_ex.search(detail)
		print(title_obj.group(2) + ' ----- ' + title_obj.group(1) + '\r\n') # 标题 ----- url
		# 把标题和url写入baidu_news.txt
		textWrite.write(title_obj.group(2) + ' ----- ' + title_obj.group(1) + '\n')
		# 延缓0.2s在进行下一次匹配，为了执行速度没那么快而设置
		time.sleep(0.2)
		# 下载新闻页面并读取页面内容
		headers = { # 'Host':'baike.baidu.com',  
                    'Connection':'keep-alive',  
                    'Cache-Control':'max-age=0',  
                    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
                    # 'Accept-Encoding': 'gzip, deflate, br',
                    # 'X-Requested-With': 'XMLHttpRequest',  
                    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36',  
                    # 'DNT':'1',  
                    # 'Referer': 'http://example.com/',  
                    # 'Accept-Encoding': 'gzip, deflate, sdch',  
                    # 'Accept-Language': 'zh-CN,zh;q=0.8,ja;q=0.6'  
				  };  
		data = None
		req = urllib.request.Request(title_obj.group(1), data, headers)
		newsContent = urllib.request.urlopen(req).read()
		# print(newsContent)
		newsDetail = open('news/' + title_obj.group(2) + '.html', 'wb')
		newsDetail.write(newsContent)
		newsDetail.close() # 关闭打开的html文件

		''' 这是要抓取的标题
			<section class="info">
			<h1 class="title">用户隐私不可侵犯，但巨头也有躺枪的时候！</h1> <<<------- 标题
			<div class="other-info">
			<input id="app_id" type="hidden" value="1536766152960704" />
			<input id="article_id" type="hidden" value="1589357928177452138" />
			<span class="author">
			<a href="/u?app_id=1536766152960704&wfr=pc&fr=new_dtl" target="_blank">罗超频道</a>
			</span>
			<span class="time">2018-01-12 12:03</span> <<<----- 添加时间
			<span class="data">阅读：391 </span> <<<----- 阅读数
			</div>
			</section>
		'''

		''' 这是要抓取的内容主体
			<section class="news-content"> <<<---- 正则匹配开头
			(-----------     <div class="abstract">
			摘要：近日，江苏消保委对百度涉嫌违法获取消费者个人信息发起消费民事公益诉讼。
			百度已第一时间召开媒体沟通会，回应称“百度APP不会、
			也没有能力’监听电话’，而百度APP敏感权限均需授权，且用户可自由关闭”。当
			</div><p>近日，江苏消............</p> -------- ) <<<----这是要匹配的内容主体
			<p></p><div class="rights"> <<<---- 正则匹配结尾
		'''
		# 接下来开始匹配需要存入数据库的数据
		reNews = newsContent.decode('utf-8') # 对二进制流进行utf-8解码，因为你网上抓取的内容先要解码
		create_time = time.strftime("%Y-%m-%d %X", time.localtime()) # 创建时间
		news_title = re.search(r'<section class="info">\n<h1 class="title">(.*?)</h1>', reNews, re.S|re.M).group(1)
		# print(news_title)
		news_add_time = re.search(r'<span class="time">(.*?)</span>', reNews, re.S|re.M).group(1)
		# print(news_add_time)
		news_read_count = re.search(r'<span class="data">(.*?)</span>', reNews, re.S|re.M).group(1)
		news_content = re.search(r'<section class="news-content">(.*?)</section>', reNews, re.S|re.M).group(1)
		pic_array = [] # 创建一个保存图片的空数组
		# 取出主体内容里面所有的图片
		img_arr = re.findall(r'<img(.*?) src="(.*?)src=(.*?)"', news_content, re.S|re.M)
		for img in img_arr:
			'''
				urllib库里面有个urlencode函数，可以把key-value这样的键值对转换成我们想要的格式，
				返回的是a=1&b=2这样的字符串，比如：
				import urllib.parse
				values={}
				values['username']='02蔡彩虹'
				values['password']='ddddd?'
				url="http://www.baidu.com"
				data=urllib.parse.urlencode(values)
				print(data)

				如果只想对一个字符串进行urlencode转换，怎么办？urllib提供另外一个函数：quote()
				import urllib.parse
				s='长春'
				s=urllib.parse.quote(s)
				print(s)
			'''
			if img[2] : # 判断当前图片路径存不存在
				# 对url字符串进行urldecode解码。python里面解码对应的函数是urllib库下的parss.unquote()函数
				url_parse = urllib.parse.unquote(img[2])
				# 只获取图片的src
				textWrite.write('\n' + str(url_parse))
				print('[+] file url --- ' + str(url_parse))
				filename = os.path.basename(url_parse) #去掉目录路径,返回文件名
				
				# fileurl 图片存放的路径(你可以替换成你本地的路径)
								
				# 正则表达式匹配反斜杠"\"，为什么是"\\\\"或是 r"\\"呢？因为在正则表达式中\为特殊符号，
				# 为了取消它在正则表达式中的特殊意义需要加一个\就变成了\\，但是问题又来了，
				# \也是字符串中的特殊字符，所以又要分别对两个\取消其特殊意义，即为\\\\。
				#Python中有一个原始字符串操作符，用于那些字符串中出现特殊字符，在原始字符串中，
				#没有转义字符和不能打印的字符。这样就可以取消了\在字符串中的转义功能，即r"\\"。
				
				# windows下的绝对路径
				fileurl = 'E:\\pythonDemo\\v4_bdnews\\bdPicture\\Picture_' + subPath + '\\' + filename
				# 把图片存到服务器路径下
				fileurl2 = '/bdPicture/Picture_' + subPath + '/' + filename
				# 把图片存储到本地路径下
				#No such file or directory 需要先创建文件newsPicture
				addPicRes = urllib.request.urlretrieve(url_parse, fileurl)
				addPicRes2 = urllib.request.urlretrieve(url_parse, 'C:/xampp/htdocs/images' + fileurl2)
				# windows下的绝对路径
				pic_array.append(fileurl2)

				# ---------------------------------------------
				# ---------------------------------------------
				# ---------------------------------------------
				# ---------------------------------------------

				# linux下的相对路径
				# fileurl = '/bdPicture/Picture_' + subPath + '/' + filename
				# 把图片存储到本地路径下
				#No such file or directory 需要先创建文件newsPicture
				# addPicRes = urllib.request.urlretrieve(url_parse, '.' + fileurl)
				# 在列表末尾添加新的对象(压入图片路径)
				# linux下的相对路径
				# pic_array.append(fileurl) 
				
				# print(addPicRes)
				# print('[+] file name --- ' + filename)
			else :
				pic_array.append("/error.jpg")
				print('[-] Picture add failed!!!')
			time.sleep(0.15)
		# print(pic_array)
		# 转译符
		strinfo = re.compile(r'<img(.*?)>')
		news_content = strinfo.sub('<img src="javascript:void(0)" />', news_content)
		
		# 替换文本到正常的本地存储的路径
		count = 0
		beg = 0
		boolean = True
		# 防止有其他没有抓取到的图片而报错下标没找到
		pic_len = len(pic_array)
		while boolean :
			# 因为下标是0开始的所以等于数组长度的时候就直接退出
			if count == pic_len :
				boolean = False
			else :
				res = news_content.find('<img src="javascript:void(0)" />', beg, len(news_content))
				if res != -1 :
					# 替换当前图片数组中相对应下标的路径 注意含头不含尾 而且"这边之前的双引号也要舍掉
					news_content = news_content[0 : res + 9] + pic_array[count] + news_content[res + 29 : len(news_content)]
					beg = res + 1 # 每次都要+1不然会死循环
					count += 1 # 每次+1获取下个图片的地址
				else :
					boolean = False
		# print('\n--- 查询替换结束 ---')
		
		# 文本存入数据库的时候一定要把"双引号进行\\转码
		news_content = news_content.replace('"', '\\"').replace('\n', '')
		# 把文本内容输入到baidu_news_x_xx.txt文本
		# textWrite.write('\n\n' + news_content.replace('"', '\\"').replace('\n', '') + '\n\n')
		# 输入要txt文件的时候。可以不用转码
		textWrite.write('\n\n' + news_content.replace('\n', '') + '\n\n')

		# 将数组转变为字符串在存入数据库
		pic_array = ','.join(str(i) for i in pic_array)
		
		# add_content = '<p class="test">测试<span>123</span></p>'
		# 把所需要的数据存入数据库
		# sql = "insert into baijia_news (title, content, add_time, read_count) values ('name', 'content', 'addTime', 15)"
		sql = 'insert into baijia_news (title, content, pic_array, create_time, add_time, read_count) values ("%s", "%s", "%s", "%s", "%s", "%s")' % (news_title, news_content, pic_array, create_time,news_add_time, news_read_count)
		
		# 异常处理
		try:
			# 执行sql语句
			cursor.execute(sql)
			# 提交到数据库执行
			conn.commit()
		# IOError(输入/输出错误)
		# except (IOError ,ZeroDivisionError):
		except Exception as e: # 打印当前错误
			# 发生错误是回滚
			conn.rollback()
			print('[-] add database failed!!!')
			print(e)
		else: # 打印添加数据成功
			print('[+] add database true!!!')

textWrite.close() # 关闭打开的txt文件

cursor.close() # 关闭游标
conn.close() # 关闭数据库链接,释放内存

