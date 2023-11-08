'''
长尾分布分析：

    数据集：Delicious、CiteULike
    图1（2-3）：展示二者物品流行度分布曲线
        横坐标：物品流行度K（物品流行度K：对物品产生过行为的用户总数）
        纵坐标：流行度K的物品的总数
        即：横坐标：人数；纵坐标：物品总数。

    图2（2-4）：展示二者用户活跃度的分布曲线
        横坐标：用户活跃度K（用户活跃度K：用户产生过行为的物品总数）
        纵坐标：活跃度为K的用户总数
        即：横坐标：物品总数；纵坐标：用户数。
'''

import pandas as pd
import pyecharts.options as opts
from pyecharts.charts import Scatter

data = pd.read_csv("..\\工程1\\user_taggedbookmarks-timestamps.dat",sep='\t')

#画图：2-3
#抓取横坐标：对物品产生过行为的用户总数1-100000
# da1= data["userID"][1:20]]
# da1= data["userID"]
# count = 1
# list = []
# dic = {}
# userId = None
# for x in da1:
#     # print(x,"B")
#     if x==userId:
#         count+=1
#         # print("userId:",userId,"\t","count:",count)
#         userId = x
#     else:
#         dic = {"ID": userId, "count": count}
#         list.append(dic)
#         count = 1
#         userId = x
#         # print("else")
# dic = {"ID": userId, "count": count}
# list.append(dic)
#
# da2 = list[0:20]
# for x in da2:
#     print(x)

#抓取纵坐标：流行度K的物品总数
y_data= data["bookmarkID"]

count = 0
tag = 0
y_list = []
y_list_dic = []
dic = {}
bookmarkId = None
#为方便统计，将数据改成{count，1}的形式
for x in y_data:
    # count+=1
    dic = {"bookMarkId": x, "count": 1}
    y_list.append(dic)

y_list = y_list[0:1000]
# y_list = y_list[:10000]
#用于实现计数功能，目标实现{mookmarkId,x}形式数据，最终形成y洲坐标数据
for x in y_list:
    for j in y_list_dic:        #判断当前值是否已经查询
        if x["bookMarkId"]==j["bookMarkId"]:
            tag = 1
            continue
    if tag == 1:    #已经查询的跳过当前查询步骤，进入下一次循环便利
        tag = 0
        continue
    if tag == 0:    #当前还未查询统计，进行查询便利
        for y in y_list:
            if x["bookMarkId"] == y["bookMarkId"]:
                count+=1
        dic = {"bookMarkId": x["bookMarkId"], "count": count}
        y_list_dic.append(dic)
        count = 0

#测试数据
for y in y_list_dic:
    print(y)
#流行度为k的物品总数：通过对已有列表y_list_dic来实现统计功能，同上
k_item_total= y_list_dic
# print(k_item_total)
k_final_item_count = []
count = 0
for x in k_item_total:  #######这里错了，要改过来
    for j in k_final_item_count:        #判断当前值是否已经查询
        if x["count"]==j["initial_count"]:
            tag = 1
            continue
    if tag == 1:    #已经查询的跳过当前查询步骤，进入下一次循环便利
        tag = 0
        continue
    if tag == 0:    #当前还未查询统计，进行查询便利
        for y in k_item_total:
            if x["count"] == y["count"]:
                count+=1
        dic = {"initial_count": x["count"], "item_total_count": count}
        k_final_item_count.append(dic)
        count = 0
print("xxxxxxxx")

#纵坐标统计结果:  y_list_dic[{"bookMarkId": x, "count": x}]
for y in k_final_item_count:
    print(y)
print("xxxxxxxx1")

#画散点图
y_data = []
for x in k_final_item_count:
    y_data.append(x["item_total_count"])
# data = k_final_item_count
# data.sort(key=lambda x: x[0])
# x_data = [d[0] for d in data]
# y_data = [d[1] for d in data]
x_data = [0,10,50,100,500,1000,2000,5000,10000]
# y_data = [0,10,20,50,100,200,400,800,1000,2000]


(
    Scatter()
    .add_xaxis(xaxis_data=x_data)
    .add_yaxis(
        series_name="",
        y_axis=y_data,
        symbol_size=20,
        label_opts=opts.LabelOpts(is_show=False),
    )
    .set_series_opts()
    .set_global_opts(
        xaxis_opts=opts.AxisOpts(
            type_="value", splitline_opts=opts.SplitLineOpts(is_show=True)
        ),
        yaxis_opts=opts.AxisOpts(
            type_="value",
            axistick_opts=opts.AxisTickOpts(is_show=True),
            splitline_opts=opts.SplitLineOpts(is_show=True),
        ),
        tooltip_opts=opts.TooltipOpts(is_show=False),
    )
    .render("basic_scatter_chart_k_item_count.html")
)



# for x in da.columns:
#     print(x,++a)

# print(da.head(0))
