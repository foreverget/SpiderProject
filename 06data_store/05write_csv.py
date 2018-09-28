import csv

"""
写入数据到csv文件，需要创建一个writer对象，主要用到两个方法。
一个是writerow，这个是写入一行。一个是writerows，这个是写入多行。
"""
headers = ['name','age','classroom']
values = [
    ('zhiliao',18,'111'),
    ('wena',20,'222'),
    ('bbc',21,'111')
]
with open('test.csv','w',newline='') as fp:
    writer = csv.writer(fp)
    writer.writerow(headers)
    writer.writerows(values)