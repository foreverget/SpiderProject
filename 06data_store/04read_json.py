import json
"""
从一个文件中读取json
"""
with open('a.json','r',encoding='utf-8') as fp:
    json_str = json.load(fp)
    print(json_str)