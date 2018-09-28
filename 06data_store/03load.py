import json
"""
将一个json字符串load成python对象
"""
json_str = '[{"title": "钢铁是怎样练成的", "price": 9.8}, {"title": "红楼梦", "price": 9.9}]'
books = json.loads(json_str,encoding='utf-8')
print(type(books))
print(type(json_str))
print(books)