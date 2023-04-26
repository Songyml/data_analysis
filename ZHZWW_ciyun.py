'''
绘制词云图片,分析男,女总点击榜作品名称出现最多的词汇
'''
#encoding:utf-8
import jieba
import numpy as np
import sqlite3
from matplotlib import pyplot as plt
from wordcloud import WordCloud
from PIL import Image  #图片处理


con = sqlite3.connect('F:\\anaconda_code\\ZHZWW.db')

#引入数据
cur = con.cursor()
#sql = "select name from ZHZWW_MAN_ZDJ;"
sql = "select name from ZHZWW_WOMAN_ZDJ;"

data = cur.execute(sql)
text = ""
for item in data:
    text = text + item[0]

cur.close()
con.close()


#分词
cut = jieba.cut(text)
string = ' '.join(cut)


#设置背景图
# img = Image.open('F:\\anaconda_code\\c.jpg')
# img_array = np.array(img)

#停用词
stopwords = set('')
stopwords.update(['这','有','还','给','我','的','之','在','了','是','从','你','她','又','后','微信','公众','号','他','公众号','群','书友','有一个','人','一','个','一个','为','就','也','都','不','被','着','u3000','却','中','微信公众','要','上','小','对'])

wc = WordCloud(
    background_color = 'white',
    # mask= img_array,
    font_path='C:/Windows/Fonts/STXINGKA.TTF ',
    stopwords=stopwords,
    scale=3
)

wc.generate_from_text(string)

#绘制图片
fig = plt.figure(1)
plt.imshow(wc)
plt.axis('off')

#plt.savefig('F:\\anaconda_code\\总点击词云-男.jpg')
plt.savefig('F:\\anaconda_code\\总点击词云-女.jpg')



print('图片生成成功！')