import xlwt
import xlrd
from xlutils.copy import copy
import jieba
import sqlite3


#从数据库读取信息
conn = sqlite3.connect('F:\\anaconda_code\\ZHZWW.db')
cur = conn.cursor()

sql = '''
    SELECT ZHZWW_MAN_ZDJ.id,ZHZWW_MAN_DJYB.id,ZHZWW_MAN_DJYB.kind,ZHZWW_MAN_DJYB.name,ZHZWW_MAN_DJYB.author,ZHZWW_MAN_ZDJ.status,ZHZWW_MAN_ZDJ.time
    FROM ZHZWW_MAN_ZDJ
    INNER JOIN ZHZWW_MAN_DJYB
    ON ZHZWW_MAN_ZDJ.name = ZHZWW_MAN_DJYB.name;
'''

# sql = '''
#     SELECT ZHZWW_WOMAN_ZDJ.id,ZHZWW_WOMAN_DJYB.id,ZHZWW_WOMAN_DJYB.kind,ZHZWW_WOMAN_DJYB.name,ZHZWW_WOMAN_DJYB.author,ZHZWW_WOMAN_ZDJ.status,ZHZWW_WOMAN_ZDJ.time
#     FROM ZHZWW_WOMAN_ZDJ
#     INNER JOIN ZHZWW_WOMAN_DJYB
#     ON ZHZWW_WOMAN_ZDJ.name = ZHZWW_WOMAN_DJYB.name;
# '''

cur.execute(sql)
data = cur.fetchall()

cur.close()
conn.close()


#存入excel
# book = xlwt.Workbook()

books = xlrd.open_workbook('F:\\anaconda_code\\榜单对比.xls')
book = copy(books)

sheet = book.add_sheet('点击榜对比-男')
#sheet = book.add_sheet('点击榜对比-女')

col = ['总点击排名','点击月榜排名','类型','名字','作者','状态','最后更新时间']
for i in range(len(col)):
    sheet.write(0,i,col[i])

for i in range(len(data)):
    for j in range(len(col)):
        sheet.write(i+1,j,data[i][j])

book.save('F:\\anaconda_code\\榜单对比.xls')

print('榜单对比完成！')


