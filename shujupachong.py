'''
爬虫纵横中文网排行榜,总点击，总字数，总推荐
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



findkind = re.compile(r'target="_blank">(.*?)</a>')
findstatus = re.compile(r'class="status">(.*?)</span>',re.S)
findcount = re.compile(r'class="count">(.*?)</span>',re.S)
findtime = re.compile(r'class="time">(.*?)</span>')

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
def getData(baseurl1,baseurl2):
    datalist = []
    for i in range(1,90):
        url  = str(baseurl1 + str(i) + baseurl2)
        html = geturl(url)
        soup = BeautifulSoup(html,'html.parser')
        for item in soup('li'):
            item = str(item)
            data = []
            
            
            #类型，书名，章节，作者
            kind = re.findall(findkind,item)
            kind2 = str(kind)
            kind2 =kind2.replace(' ','')
            if kind:
                data.append(kind[0])
                data.append(kind[1])
                data.append(str(kind[2]))
                data.append(str(kind[3]))
            else:
                data.append('')
                data.append('')
                data.append('')
                data.append('')

            #状态
            status = re.findall(findstatus,item)
            sta = str(status)
            sta1 = sta.replace('\\n','').replace('\\t','').replace(' ','').replace('[','').replace(']','').replace("'",'')
            if sta1:
                data.append(sta1)
            else:
                data.append('')

            #点击量
            count = re.findall(findcount,item)
            con = str(count)
            con1 = con.replace('\\n','').replace(' ','').replace('[','').replace(']','').replace("'",'')
            if con1:
                data.append(con1)
            else:
                data.append('')

            #更新时间
            time = re.findall(findtime,item)
            if time:
                data.append(time)
            else:
                data.append('')

            datalist.append(data)

            while '' in data:
                data.remove('')

    
    while [] in datalist:
        datalist.remove([])

    return datalist



#保存至excel
def tosave(path,datalist):
    #book = xlwt.Workbook()
    
    book = xlrd.open_workbook(path)
    book2 = copy(book)
    
    #sheet = book.add_sheet('总点击榜')
    sheet = book2.add_sheet('总字数榜')
    #sheet = book2.add_sheet('总推荐榜')
    
    #col = ['类型','书名','章节','作者','状态','点击量','最后更新时间']
    col = ['类型','书名','章节','作者','状态','总字数','最后更新时间']
    #col = ['类型','书名','章节','作者','状态','总推荐','最后更新时间']
    

    for i in range(len(col)):
        sheet.write(0,i,col[i])

    for i in range(len(datalist)):
        data1 = datalist[i]
        for j in range(len(col)):
            sheet.write(i+1,j,data1[j])


    #book.save(path)
    book2.save(path)

    return True


#创建数据库
def init_db(path):
    sql = '''  
        create table ZHZWW_MAN_ZZS
        (
            id integer primary key autoincrement,
            kind varchar,
            name varchar,
            chap varchar,
            author varchar,
            status varchar,
            count numeric,
            time varchar            
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
        for j in i:                                            #ZHZWW_MAN_ZDJ，ZHZWW_MAN_ZZS,ZHZWW_MAN_ZTJ,ZHZWW_WOMAN_ZDJ,ZHZWW_WOMAN_ZZS,ZHZWW_WOMAN_ZTJ

            sql = '''
                insert into ZHZWW_MAN_ZZS(kind,name,chap,author,status,count,time )    
                values(?,?,?,?,?,?,?);'''


        cur.execute(sql,(str(i[0]),str(i[1]),str(i[2]),str(i[3]),str(i[4]),str(i[5]),str(i[6])))
        conn.commit()

    cur.close()
    conn.close()

    return



#函数调用
if __name__ == '__main__':
    #不同url
    #baseurl1 = 'https://book.zongheng.com/store/c0/c0/b0/u1/p'  #m总点击
    baseurl1 = 'https://book.zongheng.com/store/c0/c0/b0/u5/p'  #m总字数
    #baseurl1 = 'https://book.zongheng.com/store/c0/c0/b0/u2/p'  #m总推荐
    #baseurl1 = 'https://book.zongheng.com/store/c0/c0/b1/u1/p'    #w总点击
    #baseurl1 = 'https://book.zongheng.com/store/c0/c0/b1/u5/p'  #w总字数
    #baseurl1 = 'https://book.zongheng.com/store/c0/c0/b1/u2/p'   #w总推荐

    baseurl2 = '/v9/s9/t0/u0/i0/ALL.html'

    #path = 'F:\\anaconda_code\\ZHZWW_man.xls'
    #path = 'F:\\anaconda_code\\ZHZWW_woman.xls'
    
    path = 'F:\\anaconda_code\\ZHZWW.db'
    
    
    datalist = getData(baseurl1,baseurl2)
    #tosave(path,datalist)
    to_db(path,datalist)
    
    print('完毕！')