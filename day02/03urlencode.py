

from urllib import parse

params = {"wd":"周杰伦"}
result = parse.urlencode(params)
print(result)
result2 = parse.parse_qs(result)
print(result2)
