#!/usr/bin/env python3
# -*- coding:UTF-8 -*-

# 求圆形面积 S=πr²
r1 = 1
r2 = 2
r3 = 3

s1 = 3.14 * r1 * r1
s2 = 3.14 * r2 * r2
s3 = 3.14 * r3 * r3

print(r1)
print(r2)
print(r3)

r = float(input('请输入圆的半径:'))
S = 3.14 * r * r
print('圆的面积是: ' + '%.3f' % S)


# 1到100求和
def sum():
    sum = 0
    x = 1
    while x < 101:
        x = x + 1
        sum = sum + x
    return sum


print(sum())


# 从n到n+1求和
a = int(input('a= '))
b = int(input('b= '))


def sum():
    sum=0
    x = a
    while x<b+1:
        x=x+1
        sum=sum+x
    return sum


print(sum())

c = int(input('c= '))
d = int(input('d= '))


def sum():
    sum=0
    for n in range(c, d+1):
        sum=sum+n
    return sum


print(sum())

m = max(-3, 3, 4, 500)  # 变量m指向max函数
print("最大值= %.3f" % m)  # 通过m调用max函数

