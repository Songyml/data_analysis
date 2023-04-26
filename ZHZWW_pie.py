'''
男女点击月榜及总点击榜分类比例对比
'''
from matplotlib import pyplot as plt
from matplotlib import mlab
import sqlite3
import numpy as np


#从数据库中查出类型及对应数量
def read_db(db_path):

    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    
    sql1 = '''
        SELECT kind AS 类型,count(id) AS 数量
        from ZHZWW_MAN_ZDJ
        GROUP BY kind
        ORDER BY count(id) DESC;
     '''

    # sql1 = '''
    #     SELECT kind AS 类型,count(id) AS 数量
    #     from ZHZWW_MAN_DJYB
    #     GROUP BY kind
    #     ORDER BY count(id) DESC;
    # '''

    sql2 = '''
        SELECT kind AS 类型,count(id) AS 数量
        from ZHZWW_wOMAN_ZDJ
        GROUP BY kind
        ORDER BY count(id) DESC;
    '''

    # sql2 = '''
    #     SELECT kind AS 类型,count(id) AS 数量
    #     from ZHZWW_WOMAN_DJYB
    #     GROUP BY kind
    #     ORDER BY count(id) DESC;
    # '''


    cur.execute(sql1)
    data1 = cur.fetchall()

    cur.execute(sql2)
    data2 = cur.fetchall()
    cur.close

    conn.close()

    datalist = []
    datalist.append(data1)
    datalist.append(data2)

    return datalist


#绘制饼图并存储
def pie(datalist):

    #显示中文
    plt.rcParams['font.sans-serif']=['SimHei']

    #画布的大小宽，高，分辨率
    plt.figure(figsize=(10,8),dpi=120) 



    plt.subplot(1,2,1)
    #标签统计
    labels = []
    sizes = []
    explode = []

    for i in datalist[0]:
        labels.append(i[0])
        sizes.append(i[1])
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
            'fontsize':10   #文本大小
                        }
                        ) 

    plt.axis('equal')
    plt.legend(
          title="类型",
          bbox_to_anchor=(1.1,0.12),
          ncol = int (len(datalist[0]) / 4 )
          )
    plt.rcParams.update({'font.size': 8}) 
    plt.title('总点击榜分类-男',fontsize = 18)
   # plt.title('点击月榜分类-男',fontsize = 18)


    plt.subplot(1,2,2)
    #标签统计
    labels = []
    sizes = []
    explode = []

    for i in datalist[1]:
        labels.append(i[0])
        sizes.append(i[1])
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
            'fontsize':10,#文本大小
                        }
                        ) 

    plt.axis('equal')
    plt.legend(
          title="类型",
          bbox_to_anchor=(1,0.12),
          ncol = int (len(datalist[1]) / 3 )
          )
    plt.rcParams.update({'font.size': 15}) 
   
    


    plt.title('总点击榜分类-女',fontsize = 18)
    #plt.title('点击月榜分类-女',fontsize = 18)



    plt.savefig(r"F:\\anaconda_code\\总点击榜分类对比.jpg")
    #plt.savefig(r"F:\\anaconda_code\\点击月榜分类对比.jpg")

    return




if __name__ == '__main__':
    
    db_path = 'F:\\anaconda_code\\ZHZWW.db'
    datalist = read_db(db_path)
    pie(datalist)
    print('绘制饼图完成！')