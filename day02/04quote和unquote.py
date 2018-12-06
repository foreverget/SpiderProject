

from urllib import parse

query_string = parse.quote("https://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=0&rsv_idx=1&tn=baidu&wd=张卫健")
print(query_string)
origin_string = parse.unquote(query_string)
print(origin_string)