from shapely.wkt import loads
import pandas as pd
import csv
# 兴趣区域 POLYGON((32.5 15.59, 32.65 15.59, 32.65 15.69, 32.5 15.69, 32.5 15.59))
# 兴趣区域 POLYGON((-93.95 35.11, -93.69, 35.11, -93.69 35.31, -93.95 35.31, -93.95 35.11))
shp = loads("POLYGON((-93.95 35.11, -93.69 35.11, -93.69 35.31, -93.95 35.31, -93.95 35.11))")

# # # ---------------------
# f = open('E:\\Logan\\new\\sat_ob_g.csv', 'w',encoding='utf-8', newline='')
#
# csv_writer = csv.writer(f)
#     # 3. 构建列表头
# csv_writer.writerow(["s","s_url","sensor","spt","ob","st","et","t"])
#     # 打开查询文件
#     # ANSI  utf-8打开csv文件需要查看其编码方式，方法即打开方式用记事本，另存为，最下面就有编码方式
# data1 = pd.read_csv("E:\\Logan\\new\\sat_ob.csv",
#                         encoding='utf-8')  # ANSI  utf-8打开csv文件需要查看其编码方式，方法即打开方式用记事本，另存为，最下面就有编码方式
# data1_s=data1['s']
# data1_surl = data1['s_url']
# data1_sensor = data1['sensor']
# data1_spt = data1['spt']
# data1_st = data1['st']
# data1_et = data1['et']
# data1_t = data1['t']
# data1_ob = data1['ob']
#
# for j in range(len(data1_t)):
#     shp2 = loads(data1_t[j])
#     # 是否相交
#     if shp.intersects(shp2):
#         csv_writer.writerow([data1_s[j],data1_surl[j],data1_sensor[j],data1_spt[j],data1_ob[j],data1_st[j],data1_et[j],data1_t[j]])
#     j = j + 1
#     print("已经处理" + str(j) + "个文件")
# f.close()

# read_csv_to_csv()
print("完成！")
# --------------------


# -----POI与卫星的相互对比---------------
f = open('E:\\Logan\\new\\aer_sat.csv', 'w',encoding='utf-8', newline='')
csv_writer = csv.writer(f)
    # 3. 构建列表头
csv_writer.writerow(["high","s_sat"])
    # 打开查询文件
data1 = pd.read_csv("E:\\Logan\\new\\sat_ob_g.csv",
                        encoding='utf-8')  # ANSI  utf-8打开csv文件需要查看其编码方式，方法即打开方式用记事本，另存为，最下面就有编码方式
data2 = pd.read_csv("E:\\Logan\\Logan_s\\aer_g.csv",
                        encoding='utf-8')
data1_s=data1['s']
data1_t = data1['t']
 # URLsd
data2_s = data2['aer']
data2_t = data2['geo']
for j in range(len(data2_s)):
        # 4. 写入csv文件内容
    shp2=loads(data2_t[j])
    geo=[]
    for i in range(len(data1_s)):
        shp1 = loads(data1_t[i])
    # 是否相交
        if shp1.intersects(shp2):
            geo.append(data1_s[i])
        i=i+1
    csv_writer.writerow([data2_s[j],geo])
    j = j + 1
    print("已经处理" + str(j) + "个文件")
f.close()

# read_csv_to_csv()
print("完成！")
# --------------------



# ------POI与兴趣区域的相交--------------
# shp = loads("POLYGON((-93.95 35.11, -93.69 35.11, -93.69 35.31, -93.95 35.31, -93.95 35.11))")
# f = open('E:\\Logan\\high_g.csv', 'w',encoding='utf-8', newline='')
#
# csv_writer = csv.writer(f)
#     # 3. 构建列表头
# csv_writer.writerow(["high","geo"])
#     # 打开查询文件
#     # ANSI  utf-8打开csv文件需要查看其编码方式，方法即打开方式用记事本，另存为，最下面就有编码方式
# data1 = pd.read_csv("E:\\Logan\\Highway.csv",
#                         encoding='utf-8')  # ANSI  utf-8打开csv文件需要查看其编码方式，方法即打开方式用记事本，另存为，最下面就有编码方式
# data1_s=data1['high']
# data1_t = data1['geo']
#  # URLsd
# # data1_so = data1['so']
# # data1_po = data1['po']
# for j in range(len(data1_t)):
#         # 4. 写入csv文件内容
#         # data1_set_1=data1_set[j].split('"')[1]
#         # data1_st_1 = data1_st[j].split('"')[1]
#         # data1_et_1 = data1_et[j].split('"')[1]
#     shp2 = loads(data1_t[j])
#     # 是否相交
#     if shp.intersects(shp2):
#         csv_writer.writerow([data1_s[j],data1_t[j]])
#     j = j + 1
#     print("已经处理" + str(j) + "个文件")
# f.close()
#
# # read_csv_to_csv()
# print("完成！")


