#  String 字符串  str
str1 = 'hello'
str2 = str() # 空字符串
str2 = 'world'

str3 = '''hello world
hello python''' # 三引号可以换行

# 字符串的拼接
str4 = str1 + ' ' + str2 # hello world

# 字符串的重复
str5 = str1 * 3 # hellohellohello

# 字符串的索引
str6 = 'hello world'
print(str6[0]) # h
print(str6[-1]) # d

# 字符串的切片
print(str6[0:5]) # hello, 左闭右开,不取右边的值
print(str6[6:]) # world, 不写右边的值,默认取到字符串的末尾
print(str6[:6]) # hello, 不写左边的值,默认从0开始
print(str6[::2]) # hlo, 步长为2

# 字符串反转
print(str6[::-1]) # dlrow olleh