# coding=utf-8  
# 声明编码方式 默认编码方式ASCII 参考https://www.python.org/dev/peps/pep-0263/  
import urllib.request
import time  
import re  
import os  
  
''''' 
Python下载游迅网图片 BY:Eastmount 
'''  
  
''''' 
************************************************** 
#第一步 遍历获取每页对应主题的URL 
#http://pic.yxdown.com/list/1_0_1.html 
#http://pic.yxdown.com/list/1_0_75.html 
************************************************** 
'''  

# print(re.findall('([0-9][a-z])',"fdskfj1323jfkdj"))
p = re.compile('(one|two|three)')
print(p.sub('num','one word two words three wordsapple', 3))

fileurl=open('yxdown_url.txt','w', encoding='utf-8')  
# fileurl=open('yxdown_url.txt','w')  
fileurl.write('****************获取游讯网图片URL*************\n\n')   
# print(fileurl.read())
#建议num=3 while num<=3一次遍历一个页面所有主题,下次换成num=4 while num<=4而不是1-75   
num=10  
while num<=10:  
	# http://pic.yxdown.com/list/1_0_1.html
    temp = 'http://pic.yxdown.com/list/1_0_'+str(num)+'.html'  
    content = urllib.request.urlopen(temp).read() 
    print('yxdown_'+str(num)+'.html')
    open('yxdown_'+str(num)+'.html','wb').write(content)  
    print(temp)  
    # soup = BeautifulSoup(content, 'html.parser')  
    # print(soup.encode('gbk').decode('gbk'))
    # print(content.decode('utf-8'))
    # print(content)
    fileurl.write('****************第'+str(num)+'页*************\n\n')  
  
    #爬取对应主题的URL  
    #<div class="cbmiddle"></div>中<a target="_blank" href="/html/5533.html" >  
    count=1 #计算每页1-75中具体网页个数  
    res_div = r'<div class="cbmiddle">(.*?)</div>'   
    m_div = re.findall(res_div,content.decode('utf-8'),re.S|re.M)  
    # print(m_div)
    for line in m_div:  
        #fileurl.write(line+'\n')  
        #获取每页所有主题对应的URL并输出  
        if "_blank" in line: #防止获取列表list/1_0_1.html list/2_0_1.html  
            #获取主题  
            fileurl.write('\n\n********************************************\n\n')  
            title_pat = r'<b class="imgname">(.*?)</b>'  
            title_ex = re.compile(title_pat,re.M|re.S)  
            # print(title_ex)
            # title_obj = re.search(title_ex, line)  
            title_obj = title_ex.search(line)  
            # print(title_obj)
            # print(title_obj.group(1))
            # print(title_obj.group())
            title = title_obj.group(1)  
            # print(title)
            # print(unicode(title,'utf-8'))  
            # print(type(title_obj.span()))
            fileurl.write('************* ' + title + ' *************\n')  
            #获取URL  
            res_href = r'<a target="_blank" href="(.*?)"'  
            m_linklist = re.findall(res_href,line)  
            # print(m_linklist)
            #print unicode(str(m_linklist),'utf-8')  
            for link in m_linklist:  
                fileurl.write(str(link)+'\n') #形如"/html/5533.html"  
                ''''' 
                ************************************************** 
                #第二步 去到具体图像页面 下载HTML页面 
                #http://pic.yxdown.com/html/5533.html#p=1 
                #注意先本地创建yxdown 否则报错No such file or directory 
                ************************************************** 
                '''  
                #下载HTML网页无原图 故加'#p=1'错误  
                #HTTP Error 400. The request URL is invalid.  
                html_url = 'http://pic.yxdown.com'+str(link)  
                print(html_url)  
                html_content = urllib.request.urlopen(html_url).read() #具体网站内容  
                #可注释它 暂不下载静态HTML  
                # 请现在当前根目录下创建yxdown文件夹
                open('yxdown/yxdown_html'+str(count)+'.html','wb').write(html_content)  
  
  
                ''''' 
                #第三步 去到图片界面下载图片 
                #图片的链接地址为http://pic.yxdown.com/html/5530.html#p=1 #p=2 
                #点击"查看原图"HTML代码如下 
                #<a href="javascript:;" style=""onclick="return false;">查看原图</a> 
                #通过JavaScript实现 而且该界面存储所有图片链接<script></script>之间 
                #获取"original":"http://i-2.yxdown.com/2015/3/18/6381ccc..3158d6ad23e.jpg" 
                '''  
                
                html_script = r'<script>(.*?)</script>'  
                m_script = re.findall(html_script,html_content.decode('utf-8'),re.S|re.M)  
                for script in m_script:  
                    res_original = r'"original":"(.*?)"' #原图  
                    m_original = re.findall(res_original,script)  
                    # print(m_original)
                    for pic_url in m_original:  
                        print(pic_url)  
                        fileurl.write(str(pic_url)+'\n')  
                        # print(time.ctime())
                        ''''' 
                        #第四步 下载图片 
                        #如果浏览器存在验证信息如维基百科 需添加如下代码 
                            class AppURLopener(urllib.FancyURLopener): 
                                version = "Mozilla/5.0" 
                            urllib._urlopener = AppURLopener() 
                        #参考 http://bbs.csdn.net/topics/380203601 
                        #http://www.lylinux.org/python使用多线程下载图片.html 
                        '''  
                        filename = os.path.basename(pic_url) #去掉目录路径,返回文件名  
                        #No such file or directory 需要先创建文件Picture3  
                        urllib.request.urlretrieve(pic_url, 'E:\\pythonDemo\\v3_loadImg\\Picture3\\'+filename)  
                        #http://pic.yxdown.com/html/5519.html  
                        #IOError: [Errno socket error] [Errno 10060]   
                        # time.sleep(2)
                  
                #只输出一个URL 否则输出两个相同的URL  
                break   
              
            #当前页具体内容个数加1  
            count=count+1  
            time.sleep(0.1)    
        else:  
            print('no url about content')  
          
    time.sleep(1)    
    num=num+1  
else:  
    print('Download Over!!!')  