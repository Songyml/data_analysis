'''
统计点击月榜中简介出现的词频，分析词汇出现频率
'''
import xlwt
import xlrd
from xlutils.copy import copy
import jieba
import sqlite3
from collections import Counter



#从数据库读取信息
conn = sqlite3.connect('F:\\anaconda_code\\ZHZWW.db')
cur = conn.cursor()

#sql = 'SELECT info FROM ZHZWW_MAN_DJYB;'
sql = 'SELECT info FROM ZHZWW_WOMAN_DJYB;'

data = cur.execute(sql)
text = ""
for item in data:
    text = text + item[0]

cur.close()
conn.close()


#停用词设置
stopwords = [line.strip() for line in open('F:\\anaconda_code\\stopwords.txt',encoding='UTF-8').readlines()]
#stopwords.update(['我','的',' ','，','。','…','！','：','—','“','”','了','是','他','在','、','？','一个','有','…','群','为','号','公众','都','我','人','；','《','》','“','”'])


#分词
cut = jieba.lcut_for_search(text)

#停用词去除    
outstr = []
for word in cut:
    if word not in stopwords:
        outstr.append(word)

#词频统计
counts= []
for i in outstr:
    counts.append(i)

c = Counter(counts)

list1 = list(c.items())

#写入excel
#book = xlwt.Workbook()

books = xlrd.open_workbook('F:\\anaconda_code\\简介词频.xls')
book = copy(books)

sheet = book.add_sheet('点击月榜简介词频统计-女')

col = ['词语','出现次数']
for i in range(len(col)):
    sheet.write(0,i,col[i])

for i in range(len(c)):
    for j in range(len(col)):
        sheet.write(i+1,j,list1[i][j])


book.save('F:\\anaconda_code\\简介词频.xls')

print('词频统计完毕！')

