import json
"""
json在dump的时候，只能存放ascii的字符，因此会将中文进行转义，这时候我们可以使用ensure_ascii=False关闭这个特性。
在Python中。只有基本数据类型才能转换成JSON格式的字符串。也即：int、float、str、list、dict、tuple。
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

json_str = json.dumps(books,ensure_ascii=False)
print(type(books))
print(type(json_str))
print(json_str)