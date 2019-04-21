#!/usr/bin/env python3
# -*- coding:UTF-8 -*-

# 定义一个取绝对值函数


def my_abs(x):
    if x >= 0:
        return x
    else:
        return -x


'''
数据类型检查可以用内置函数isinstance()实现：
def my_abs(x):
    if not isinstance(x, (int, float)):  # 对参数类型做检查，只允许整数和浮点数类型的参数
        raise TypeError('bad operand type')
    if x >= 0:
        return x
    else:
        return -x
'''
