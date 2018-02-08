# coding=utf-8  

# 追加新内容
# addNewTxt = open('baijia_baidu_news.txt','ab') # 以追加的方式打开文件
# addNewTxt.write('\n\n 我是来垫底的。。。'.encode('utf-8')) # 把内容写入文件
# addNewTxt.close() # 关闭文件

# 读取内容
readTxt = open('baijia_baidu_news.txt','rb')
txtContent = readTxt.read().decode('utf-8')
readTxt.close() # 关闭文件

print(txtContent)