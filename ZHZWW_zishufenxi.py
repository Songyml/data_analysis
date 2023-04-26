'''
男,女生看小说字数分类
'''
import sqlite3
from matplotlib import pyplot as plt


#查询数据库并统计小说字数区间
def getCount():

    #连接数据库
    conn = sqlite3.connect('F:\\anaconda_code\\ZHZWW.db')

    cur = conn.cursor()


    #查询并写入数据
    sql1 = '''
            SELECT count(id) AS 数量
            FROM ZHZWW_WOMAN_ZZS
            WHERE count
            BETWEEN '0' AND '300000';
    '''

    sql2 = '''
            SELECT count(id) AS 数量
            FROM ZHZWW_WOMAN_ZZS
            WHERE count
            BETWEEN '300001' AND '500000';
    '''

    sql3 = '''
            SELECT count(id) AS 数量
            FROM ZHZWW_WOMAN_ZZS
            WHERE count
            BETWEEN '500001' AND '1000000';
    '''

    sql4 = '''
            SELECT count(id) AS 数量
            FROM ZHZWW_WOMAN_ZZS
            WHERE count
            BETWEEN '1000001' AND '2000000';
    '''


    sql5 = ''' 
            SELECT count(id) AS 数量
            FROM ZHZWW_WOMAN_ZZS
            WHERE count > 2000001;
    '''


    datalist = []

    cur.execute(sql1)
    data = cur.fetchall()
    datalist.append(data[0])
    cur.close

    cur.execute(sql2)
    data = cur.fetchall()
    datalist.append(data[0])
    cur.close

    cur.execute(sql3)
    data = cur.fetchall()
    datalist.append(data[0])
    cur.close

    cur.execute(sql4)
    data = cur.fetchall()
    datalist.append(data[0])
    cur.close

    cur.execute(sql5)
    data = cur.fetchall()
    datalist.append(data[0])
    cur.close

    conn.close()

 
    return datalist



#绘制饼图显示小说篇幅
def pie(datalist):

    #显示中文
    plt.rcParams['font.sans-serif']=['SimHei']

    #画布的大小宽，高，分辨率
    plt.figure(figsize=(8,7),dpi=120) 

    #标签统计
    labels = ['0-30万','30万-50万','50万-100万','100万-200万','200万以上']
    sizes = []
    explode = []

    for i in datalist:
        str0 = str(i[0])
        str1 = str0.replace(',','')
        sizes.append(str1)
        explode.append(0.01)
    
    plt.pie(
                        sizes,
                        explode=explode,
                        labels=labels,
                        #labeldistance = 1.2,#图例距圆心半径倍距离
                        autopct = '%3.2f%%', #数值保留固定小数位
                        shadow = False, #无阴影设置
                        pctdistance = 0.6, #数值距圆心半径倍数距离
                        textprops={
                            'fontsize':12,#文本大小
                        }
                        ) 

    plt.axis('equal')
    plt.legend(
          title="字数范围",
          bbox_to_anchor=(0.1,0.7),
          )
    plt.rcParams.update({'font.size': 12}) 
   
    
    #plt.title('总字数榜分类-男',fontsize = 18)
    plt.title('总字数榜分类-女',fontsize = 18)


    #plt.savefig(r"F:\\anaconda_code\\总字数榜分类-男.jpg")
    plt.savefig(r"F:\\anaconda_code\\总字数榜分类-女.jpg")



if __name__ == '__main__':
    datalist = getCount()
    pie(datalist)
    print('饼图绘制完成！')
