# -*- coding: utf-8 -*-

"""
非可变类型的共享机制
数字、字符串完全相同的值用的是同一片内存

某些情况下，字符串中包含有特殊字符:空格等，就不会共享
"""

"""
********************************************************************
字符串
********************************************************************
"""
str1 = "hello world"
print(id(str1))

#删掉str1，地址不会和str1的一样
#del str1
str2 = "hello world"
print(id(str2))

print("*" * 100)
"""
********************************************************************
字符和小整形

单个字符共用对象，常驻内存
小整数[-5, 257)共用对象，常驻内存
********************************************************************
"""
char1 = 'a'
print(id(char1))

#删掉char1,地址还是和char1的一样
#del char1
char2 = 'a'
print(id(char2))

print("*" * 100)

int1 = 100
print(id(int1))

#删掉int1,地址还是和int1的一样
#del int1
int2 = 100
print(id(int2))
