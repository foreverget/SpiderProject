import re

# 验证手机号码：手机号码的规则是以1开头，第二位可以是34587，后面那9位就可以随意了。示例代码如下：
text = "18570631587"
ret = re.match('1[34587]\d{9}',text)
print(ret.group())
# 而如果是个不满足条件的手机号码。那么就匹配不到了。示例代码如下：
# text = "1857063158"
# ret = re.match('1[34587]\d{9}',text)
# print(ret.group())
# >> AttributeError: 'NoneType' object has no attribute

#验证邮箱：邮箱的规则是邮箱名称是用数字、数字、下划线组成的，然后是@符号，后面就是域名了。示例代码如下：
text = "hynever@163.com"
ret = re.match('\w+@\w+\.[a-zA-Z\.]+',text)
print(ret.group())

#验证URL：URL的规则是前面是http或者https或者是ftp然后再加上一个冒号，再加上一个斜杠，再后面就是可以出现任意非空白字符了。示例代码如下：
text = "http://www.baidu.com/"
ret = re.match('(http|https|ftp)://[^\s]+',text)
print(ret.group())

#验证身份证：身份证的规则是，总共有18位，前面17位都是数字，后面一位可以是数字，也可以是小写的x，也可以是大写的X。示例代码如下：
# text = "3113111890812323X"
# ret = re.match('\d{17}[\dxX]',text)
# print(ret.group())

# ^（脱字号）：表示以...开始,#如果是在中括号中，那么代表的是取反操作.：
text = "hello"
ret = re.match('^h',text)
print(ret.group())


# $：表示以...结束：
# 匹配163.com的邮箱
text = "xxx@163.com"
ret = re.search('\w+@163\.com$',text)
print(ret.group())

# |：匹配多个表达式或者字符串：
text = "hello|world"
ret = re.search('hello',text)
print(ret.group())

"""
贪婪模式和非贪婪模式：
贪婪模式：正则表达式会匹配尽量多的字符。默认是贪婪模式。
非贪婪模式：正则表达式会尽量少的匹配字符。
示例代码如下：
"""
text = "0123456"
ret = re.match('\d+',text)
print(ret.group())
# 因为默认采用贪婪模式，所以会输出0123456

#可以改成非贪婪模式，那么就只会匹配到0。示例代码如下：
text = "0123456"
ret = re.match('\d+?',text)
print(ret.group())

#案例：匹配0-100之间的数字：
text = '99'
ret = re.match('[1-9]?\d$|100$',text)
print(ret.group())
