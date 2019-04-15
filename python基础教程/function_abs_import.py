#!usr/bin/env python3
# -*- coding:UTF-8 _-*-

# 从其它模块中导致并调用函数
from function_abs_test import my_abs

i = my_abs(-8)
print(i)

# 比较: 调用自定义的函数 与 调用python内置函数

# e = my_abs('E') # 自定义的my_abs没有参数检查，会导致if语句出错
# print(e)
# TypeError: '>=' not supported between instances of 'str' and 'int'

f = abs('F')
print(f) # TypeError: bad operand type for abs(): 'str'

