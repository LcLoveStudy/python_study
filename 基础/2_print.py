# 基础打印
print('-'*10,'下面是基础的打印格式','-'*10)
print(2024) # 2024 int
print(3.14) # 3.14 float
print('hello world') # str

# 设置打印间隔
print('\n','-'*10,'下面是设置打印间隔','-'*10)
print(2024, "hello world") # 2024 hello world , 两个变量之间用逗号隔开,会自动在变量之间添加空格
print(2024, "hello world", sep="") # 2024helloworld , 两个变量之间用 sep 参数指定分隔符

# 设置打印换行
print('\n','-'*10,'下面是设置打印换行','-'*10)
print(2023)
print(2024,end='') # end 参数指定结尾字符,默认是换行符('\n')
print(2025)

# 格式化输出
'''
%s 字符串
%d 整数, %02d 表示不足两位数用0补齐, %3d 表示不足三位数用空格补齐
%f 浮点数, %.2f 表示小数点后保留两位
%% %
'''
print('\n','-'*10,'下面是格式化输出','-'*10)
year = 2024
month = 2
day = 20
week = '一'
print('今天是%d年%02d月%d日,星期%s' % (year,month,day,week)) # 今天是2024年2月20日,星期一