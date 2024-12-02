# Floading Point Number 浮点型 float
n1 = 0.1
n2 = 0.2
print(n1 + n2)  # 0.30000000000000004 浮点数精度问题

# 处理浮点数精度问题
n3 = round(n1 + n2, 2)  # 保留两位小数
print(n3)  # 0.3

import math
math.ceil(0.1 + 0.2)  # 1 向上取整
math.floor(0.1 + 0.2)  # 0 向下取整