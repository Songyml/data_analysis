'''
作者产量统计  总点击，总推荐，点击月榜，推荐月榜
'''
import sqlite3
import matplotlib.pyplot as plt
import numpy as np


def sum():

    conn = sqlite3.connect('F:\\anaconda_code\\ZHZWW.db')

    cur = conn.cursor()

    # sql1 = '''
    #     SELECT author AS 作者,count(author) AS 数量
    #     from ZHZWW_MAN_ZDJ
    #     GROUP BY author
    #     ORDER BY count(author) DESC;
    # '''


    # sql2 = '''
    #     SELECT author AS 作者,count(author) AS 数量
    #     from ZHZWW_MAN_DJYB
    #     GROUP BY author
    #     ORDER BY count(author) DESC;
    # '''

    # sql3 = '''
    #     SELECT author AS 作者,count(author) AS 数量
    #     from ZHZWW_MAN_TJYB
    #     GROUP BY author
    #     ORDER BY count(author) DESC;
    # '''


    sql1 = '''
        SELECT author AS 作者,count(author) AS 数量
        from ZHZWW_WOMAN_ZDJ
        GROUP BY author
        ORDER BY count(author) DESC;
    '''

    sql2 = '''
        SELECT author AS 作者,count(author) AS 数量
        from ZHZWW_WOMAN_DJYB
        GROUP BY author
        ORDER BY count(author) DESC;
    '''

    sql3 = '''
        SELECT author AS 作者,count(author) AS 数量
        from ZHZWW_WOMAN_TJYB
        GROUP BY author
        ORDER BY count(author) DESC;
    '''

    datalist = []


    cur.execute(sql1)
    data = cur.fetchall()
    datalist.append(data)

    cur.execute(sql2)
    data = cur.fetchall()
    datalist.append(data)

    cur.execute(sql3)
    data = cur.fetchall()
    datalist.append(data)

    conn.close()

    return datalist


def table(data):
    plt.rcParams['font.sans-serif']=['SimHei']

    plt.figure(figsize=(10,9),dpi=120) 


    #总点击
    plt.subplot(1,3,1)
    col=['作者','作品数量']
    vals = []

    for j in range(len(data[0])):
        if data[0][j][1] > 4:
            vals.append(data[0][j])

    tab = plt.table(cellText=vals, 
                colLabels=col,
                loc='center', 
                rowLoc='center')
    tab.scale(1,2)
    plt.axis('off')
    plt.title('总点击榜作者作品数-女')
    #plt.title('总点击榜作者作品数-男')



    #点击月榜
    plt.subplot(1,3,2)
    col=['作者','作品数量']
    vals = []
    for j in range(len(data[1])):
        if data[1][j][1] > 2:
            vals.append(data[1][j])

    tab = plt.table(cellText=vals, 
                colLabels=col,
                loc='center', 
                rowLoc='center')
    tab.scale(1,2)
    plt.axis('off')
    plt.title('点击月榜作者作品数-女')
    #plt.title('点击月榜作者作品数-男')


    #推荐月榜
    plt.subplot(1,3,3)
    col=['作者','作品数量']
    vals = []

    for j in range(len(data[2])):
        if data[2][j][1] > 1:
            vals.append(data[2][j])

    tab = plt.table(cellText=vals, 
                colLabels=col,
                loc='center', 
                rowLoc='center')
    tab.scale(1,2) 
    plt.axis('off')
    plt.title('推荐月榜作者作品数-女')
    #plt.title('推荐月榜作者作品数-男')



    plt.savefig('F:\\anaconda_code\\作者作品数对比-女.jpg')
    #plt.savefig('F:\\anaconda_code\\作者作品数对比-男.jpg')



    return True


if __name__ == '__main__':
    data = sum()
    table(data)
    print('绘制表格完成！')