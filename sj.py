import pandas as pd
import matplotlib.pylab as plt

#加载全部数据
sj = pd.read_excel(r'F:\DataAnalysis\sj.xls')

#-----------------各个学院平均分------------------
#按照各个学院进行分组
xymean = sj['总分'].groupby([sj['院系名称'],sj['语言级别']])


#计算各个学院的平均分数
xymean = xymean.mean()

#将“语言级别”从行转换为列
xymean = xymean.unstack(level='语言级别')

#使用横向柱状图显示
#xymean.plot(kind='barh')

import matplotlib as mpl
mpl.rcParams['font.sans-serif'] = ['SimHei']
mpl.rcParams['font.serif'] = ['SimHei']

#在PyCharm中需要使用，在Ipython环境中如果以--pylab形式打开就不需要
#plt.show()

#-----------------筛选出过关人数------------------
#过滤出过关人数
sjpass = sj[sj['总分'] >= 425]


#-----------------各个学院过关人数------------------

#按照各个学院进行分组
xypass = sjpass['总分'].groupby([sjpass['院系名称'],sjpass['语言级别']])


#计算各个学院的过关总人数
xypass = xypass.count()

#将语言级别作为columns
xypass = xypass.unstack(level='语言级别')

#进行绘图
#xypass.plot(kind='barh')
#plt.show()


#-----------------各个学院的年级过关人数------------------
#按照各个学院和年级进行分组
xypass = sjpass['总分'].groupby([sjpass['院系名称'],sjpass['语言级别'],sjpass['年级']])

#计算各个学院的过关总人数
xypass = xypass.count()

#将语言级别作为columns，并且将缺失值用0进行填充
xypass = xypass.unstack(level='年级').fillna(0)

#xypass.plot(kind='barh')
#plt.show()


#-----------------各个年级过关人数------------------
njpass = sjpass['总分'].groupby([sjpass['年级'],sjpass['语言级别']]).count().unstack(level='语言级别')
#njpass.plot(kind='barh')
#plt.show()

#---------------男生女生过关情况----------------------
nvpass = sjpass['总分'].groupby([sjpass['性别'],sjpass['语言级别']]).count().unstack(level='语言级别')
nvpass.plot(kind='bar')
plt.show()
