s = '2024'
f = 3.14 
b = True
i = 2024 

# 转化成整数int  
sToNum = int(s) # 字符串转整数,必须是数字
fToNum = int(f) # 浮点数转整数,直接去掉小数点
bToNum = int(b)# 布尔值转整数, True转1, False转0

# 转化成浮点数float
sToFloat = float(s) # 字符串转浮点数,必须是数字
iToFloat = float(i) # 整数转浮点数,直接在后面加.0
bToFloat = float(b) # 布尔值转整数, True转1.0, False转0.0

# 转化成布尔值bool
sToBool = bool(s) # 字符串转布尔值,非空字符串转True,空字符串转False
iToBool = bool(i) # 整数转布尔值,非0整数转True,0转False
fToBool = bool(f) # 浮点数转布尔值,非0浮点数转True,0.0转False

# 转换为字符串str
iToStr = str(i) # 整数转字符串
fToStr = str(f) # 浮点数转字符串
bToStr = str(b) # 布尔值转字符串, True转'True', False转'False'