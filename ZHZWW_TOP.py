'''
爬虫纵横中文网排行榜,总推荐月榜，总点击月榜
'''
#encoding:utf-8
import urllib.response,urllib.request,urllib.error
import xlwt
import re
import requests
import random
from bs4 import BeautifulSoup
import pandas as pd
import xlrd
from xlutils.copy import copy
import sqlite3



findname= re.compile(r'class="rank_d_b_name" title="(.*?)"')
findauthor = re.compile(r'class="rank_d_b_cate" title="(.*?)">')
findkind = re.compile(r'<a target="_blank">(.*?)</a>',re.S)
findinfo = re.compile(r'<div class="rank_d_b_info">(.*?)</div>',re.S)

#获取url
def geturl(baseurl):
    
    headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:106.0) Gecko/20100101 Firefox/106.0'
    }
    ip = {
        #'http':'61.216.156.222',
        'http':'112.194.88.136'
    }

    res = requests.get(url=baseurl,headers=headers,proxies=ip)
    respone = res.content

    return respone


#获取数据
def getData(baseurl):
    datalist = []
    for i in range(1,11):
        url  = str(baseurl + str(i))
        html = geturl(url)
        soup = BeautifulSoup(html,'html.parser')
        for item in soup('div',class_="rank_d_book_intro fl"):
            item = str(item)
            data = []

            

            #类型
            kind = re.findall(findkind,item)[0]
            kind1 = str(kind)
            kind2 = kind1.replace('[','').replace(']','').replace("'",'')
            if kind2:
                data.append(kind2)
            else:
                data.append('')

            #书名
            name = re.findall(findname,item)
            name1 = str(name)
            name2 = name1.replace('[','').replace(']','').replace("'",'')
            if name2:
                data.append(name2)
            else:
                data.append('')

            #作者
            author = re.findall(findauthor,item)
            auth1= str(author)
            auth2 = auth1.replace('[','').replace(']','').replace("'",'')
            if auth2:
                data.append(auth2)
            else:
                data.append('')

            #简介
            info = re.findall(findinfo,item)
            info1= str(info)
            info2 = info1.replace('[','').replace(']','').replace("'",'').replace('\\n','').replace('\\r','')
            if info2:
                data.append(info2)
            else:
                data.append('')
            
            datalist.append(data)


    return datalist



# # 保存至excel
# def tosave(path,datalist):
#     #book = xlwt.Workbook()
    
#     book = xlrd.open_workbook(path)
#     book2 = copy(book)
    
#     #sheet = book2.add_sheet('点击月榜')
#     sheet = book2.add_sheet('推荐月榜')

    
#     col = ['类型','书名','作者','简介']
    

#     for i in range(len(col)):
#         sheet.write(0,i,col[i])

#     for i in range(len(datalist)):
#         data1 = datalist[i]
#         for j in range(len(col)):
#             sheet.write(i+1,j,data1[j])


#     #book.save(path)
#     book2.save(path)

#     return True


#创建数据库表
def init_db(path):
    sql = '''  
        create table ZHZWW_WOMAN_DJYB
        (
            id integer primary key autoincrement,
            kind varchar,
            name varchar,
            author varchar,
            info varchar            
        )   
    '''
    conn = sqlite3.connect(path)
    cursor = conn.cursor()
    cursor.execute(sql)
    conn.commit()
    conn.close()



#保存至数据库
def to_db(path,datalist):
    init_db(path)
    conn = sqlite3.connect(path)
    cur = conn.cursor()

    for i in datalist:
        for j in i:                                            #ZHZWW_MAN_ZDJ，ZHZWW_MAN_YHZDJ,ZHZWW_MAN_ZTJ,ZHZWW_WOMAN_ZDJ,ZHZWW_WOMAN_YHZDJ,ZHZWW_WOMAN_ZTJ,ZHZWW_MAN_DJYB,ZHZWW_MAN_TJYB

            sql = '''
                insert into ZHZWW_WOMAN_DJYB(kind,name,author,info )    
                values(?,?,?,?);'''


        cur.execute(sql,(str(i[0]),str(i[1]),str(i[2]),str(i[3])))
        conn.commit()

    cur.close()
    conn.close()

    return



#函数调用
if __name__ == '__main__':
    #不同url

    #baseurl = 'https://www.zongheng.com/rank/details.html?rt=5&d=1&r=&i=2&c=0&p='   #男点击月榜
    #baseurl = 'https://www.zongheng.com/rank/details.html?rt=6&d=1&r=&i=2&c=0&p='   #男推荐月榜
    baseurl = 'https://huayu.zongheng.com/rank/details.html?rt=5&d=1&r=&i=2&c=0&p='  #女点击月榜
    #baseurl = 'https://huayu.zongheng.com/rank/details.html?rt=6&d=1&r=&i=2&c=0&p='   #女推荐月榜


    #path = 'F:\\anaconda_code\\ZHZWW_man.xls'
    #path = 'F:\\anaconda_code\\ZHZWW_woman.xls'
    
    path = 'F:\\anaconda_code\\ZHZWW.db'
    
    datalist = getData(baseurl)
    #tosave(path,datalist)
    to_db(path,datalist)
    
    print('完毕！')