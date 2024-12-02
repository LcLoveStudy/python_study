# 整数 Integers int
# 整数是正数、负数或零，没有小数部分。它们可以是任意大小。
num = 10 
num2 = -10

print(isinstance(num,int)) # True
print(type(num2)) # <class 'int'>

# 整数运算
num3 = '20' # 这里的num3是str
# total =  num + num2 + num3 # 这样写是错误的,需要将num3转换为int
total =  num + num2 + int(num3) # 这样写是正确的
print(total)