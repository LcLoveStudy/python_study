# 想要判断一个变量或值的类型可以使用type()函数
print(type(123))  # <class 'int'>
print(type('123'))  # <class 'str'>
print(type(1.23))  # <class 'float'>
print(type(True))  # <class 'bool'>
print(type(None))  # <class 'NoneType'>
print(type([1, 2, 3]))  # <class 'list'>

# 判断一个变量是否是某个类型，可以使用isinstance()函数
print(isinstance(123, int))  # True
print(isinstance('123', str))  # True
print(isinstance(1.23, float))  # True
print(isinstance(True, bool))  # True