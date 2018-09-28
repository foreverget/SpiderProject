import json
"""
json模块中除了dumps函数，还有一个dump函数，这个函数可以传入一个文件指针，直接将字符串dump到文件中。
"""
books = [
    {
        'title': '钢铁是怎样练成的',
        'price': 9.8
    },
    {
        'title': '红楼梦',
        'price': 9.9
    }
]
with open('a.json','w') as fp:
    json.dump(books,fp)