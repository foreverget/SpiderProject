import csv

"""
使用字典的方式把数据写入进去。
这时候就需要使用DictWriter了
"""
headers = ['name','age','classroom']
values = [
    {"name":'wenn',"age":20,"classroom":'222'},
    {"name":'abc',"age":30,"classroom":'333'}
]
with open('test.csv','w',newline='') as fp:
    writer = csv.DictWriter(fp,headers)
    writer = csv.writeheader()
    writer.writerow({'name':'zhiliao',"age":18,"classroom":'111'})
    writer.writerows(values)