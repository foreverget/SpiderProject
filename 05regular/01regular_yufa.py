
# 1、匹配某个字符串
import re
text = 'hello'
ret = re.match('he',text)
print(ret.group())

# 2、点（.）匹配任意的字符,点（.）不能匹配不到换行符：
text = "ab"
ret = re.match('.',text)
print(ret.group())
# text = "ab"
# ret = re.match('.',text)
# print(ret.group())
# >> AttributeError: 'NoneType' object has no attribute 'group'

# 3、\d匹配任意的数字：
text = "123"
ret = re.match('\d',text)
print(ret.group())

# 4、\D匹配任意的非数字：
text = "a"
ret = re.match('\D',text)
print(ret.group())

# 5、\s匹配的是空白字符（包括：\n，\t，\r和空格）：
text = "\t"
ret = re.match('\s',text)
print(ret.group())

# 6、\w匹配的是a-z和A-Z以及数字和下划线：
text = "_"
ret = re.match('\w',text)
print(ret.group())

# 7、\W匹配的是和\w相反的：
text = "+"
ret = re.match('\W',text)
print(ret.group())

# 8、[]组合的方式，只要满足中括号中的某一项都算匹配成功：
text = "0731-88888888"
ret = re.match('[\d\-]+',text)
print(ret.group())

# 9、*：可以匹配0或者任意多个字符。
text = "0731"
ret = re.match('\d*',text)
print(ret.group())

# 9、+：可以匹配1个或者多个字符。最少一个。
text = "abc"
ret = re.match('\w+',text)
print(ret.group())

# 10、 ?：匹配的字符可以出现一次或者不出现（0或者1）。
text = "123"
ret = re.match('\d?',text)
print(ret.group())

# 11、{m}：匹配m个字符。
text = "123"
ret = re.match('\d{2}',text)
print(ret.group())

# 12、{m,n}：匹配m-n个字符。在这中间的字符都可以匹配到。
text = "123"
ret = re.match('\d{1,2}',text)
print(ret.group())



