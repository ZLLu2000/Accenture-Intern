# -*- coding: utf-8 -*-


import pandas as pd
import matplotlib.pyplot as plt
data=pd.read_csv('data_raw')
data.head()
data.isnull().sum()

data=data.drop(['sales_record_category','competitive_category','spread_rate_category','transfer_rate_category','matain_rate_category'],axis=1)

data.isnull().sum()
cols=['undesirable_event','spread_rate', 'transfer_rate','matain_rate','positive_feedback']
data.shape
for col in cols:
    data=data.loc[(data[col]>=0)&(data[col]<=1)]
    
data.shape

data['sales_record'].plot(kind='hist')
plt.title('distribution of sales_record')
plt.show()
data['positive_feedback'].plot(kind='hist')
plt.title('distribution of positive_feedback')
plt.show()
data['undesirable_event'].plot(kind='hist')
plt.title('distribution of undesirable_event')
plt.show()

data['spread_rate'].plot(kind='hist')
plt.title('distribution of spread_rate')
plt.show()

data['transfer_rate'].plot(kind='hist')
plt.title('distribution of transfer_rate')
plt.show()
data['matain_rate'].plot(kind='hist')
plt.title('distribution of matain_rate')
plt.show()
for col in cols:
    tmp=col+'_category'
    data[tmp]='0'
    data.loc[data[col].between(0, 0.2, inclusive='left'), tmp] = '0-0.2'
    data.loc[data[col].between(0.2, 0.4, inclusive='left'), tmp] = '0.2-0.4'
    data.loc[data[col].between(0.4, 0.6, inclusive='left'), tmp] = '0.4-0.6'
    data.loc[data[col].between(0.6, 0.8, inclusive='left'), tmp] = '0.6-0.8'
    data.loc[data[col].between(0.8, 1, inclusive='left'), tmp] = '0.8-1'
    
    
for col in cols:
    plt.figure(figsize=(12,8))
    data[col+'_category'].value_counts().plot(kind = 'pie', # 选择图形类型
        autopct='%.1f%%', # 饼图中添加数值标签
        radius = 1.1, # 设置饼图的半径
        counterclock = False, # 将饼图的顺序设置为顺时针方向
        title = col, # 为饼图添加标题
        wedgeprops = {'linewidth': 1.5, 'edgecolor':'green'}, # 设置饼图内外边界的属性值
        textprops = {'fontsize':8, 'color':'black'},# 设置文本标签的属性值
        subplots=True)
    plt.show()