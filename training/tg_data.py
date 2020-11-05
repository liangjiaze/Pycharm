import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import matplotlib

# 官方文档：https://matplotlib.org/gallery/index.html

# 设置matplotlib正常显示中文和负号
matplotlib.rcParams['font.sans-serif'] = ['SimHei']  # 用黑体显示中文
matplotlib.rcParams['axes.unicode_minus'] = False  # 正常显示负号

file_path = 'E:/bigdata/data/tg_ppq&upq.csv'

file = pd.read_csv(file_path)
df = pd.DataFrame(file)

qudf = df[(df['LINELOSS_RATE'] > 0) & (df['LINELOSS_RATE'] < 10) & (df['PPQ'] < 200000)]
count = qudf['STAT_DATE'].value_counts(normalize=True)
ppq = qudf['PPQ']
upq = qudf['UPQ']
lineloss_rate = qudf['LINELOSS_RATE']

pldf = qudf[['PPQ', 'LINELOSS_RATE']]
uldf = qudf[['UPQ', 'LINELOSS_RATE']]
# print(df.index)
# print(df.columns)
print(df.info())
# print(count)


"""
计算供电量与线损率的相关行系数
"""

# s1 = pldf.corr()
# sppq = pldf[['PPQ']].corr(pldf[['LINELOSS_RATE']])
#
# print(sppq)


# x = np.arange(1,11)
# y = 2 * x + 5

"""
绘制折线图
"""
# plt.plot(lineloss_rate,ppq)


"""
绘制直方图
data:必选参数，绘图数据
bins:直方图的长条形数目，可选项，默认为10
normed:是否将得到的直方图向量归一化，可选项，默认为0，代表不归一化，显示频数。normed=1，表示归一化，显示频率。
facecolor:长条形的颜色
edgecolor:长条形边框的颜色
alpha:透明度
"""
# plt.hist(pldf, bins=10, normed=0, facecolor="blue", edgecolor="black", alpha=0.7)
# plt.title("供电量与线损率关系图")
# plt.xlabel('供电量')
# plt.ylabel('线损率')


# label_list = ['1', '2', '3', '4','5','6','7','8','9','10']    # 横坐标刻度显示值
# num_list1 = [20, 30, 15, 35]      # 纵坐标值1
# x = range(len(num_list1))
"""
绘制条形图
left:长条形中点横坐标
height:长条形高度
width:长条形宽度，默认值0.8
label:为后面设置legend准备
"""
# rects1 = plt.bar(left=x, height=num_list1, width=0.4, alpha=0.8, color='red', label="一部门")
# plt.ylim(0, 10)     # y轴取值范围
# plt.ylabel("数量")
# """
# 设置x轴刻度显示值
# 参数一：中点坐标
# 参数二：显示值
# """
# plt.xticks([index + 0.2 for index in x], label_list)
# plt.xlabel("年份")
#
# plt.legend()     # 设置题注
# # 编辑文本
# for rect in rects1:
#     height = rect.get_height()
#     plt.text(rect.get_x() + rect.get_width() / 2, height+1, str(height), ha="center", va="bottom")


"""
绘制散点图
"""
# y = pldf[['PPQ']]
# x = pldf[['LINELOSS_RATE']]
# plt.title("供电量与线损率关系图")
# plt.ylabel('供电量')
# plt.xlabel('线损率')

y = uldf[['UPQ']]
x = uldf[['LINELOSS_RATE']]
plt.title("售电量与线损率关系图")
plt.ylabel('售电量')
plt.xlabel('线损率')
plt.scatter(x, y, s=1., c=None, marker=None, cmap=None, norm=None, vmin=None, vmax=None, alpha=None, linewidths=None,
            verts=None, edgecolors=None, hold=None, data=None)

plt.show()
