# -*- coding: utf-8 -*-

arr1 = ["a", "b", "c"]
print(arr1)
print(len(arr1))
print(arr1[0])
print(arr1[1])

#pop
print(arr1.pop())
print(arr1)

for i in arr1:
    print("%d - %s"%(arr1.index(i), i))
