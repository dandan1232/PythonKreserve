# -*- coding: utf-8 -*-
# @Time    : 2024-03-20 22:14
# @Author  : Lindand
# @File    : Arrays.py
# @Description :数组的常用操作

# 创建数组
a = [];

# 添加元素
a.append(1)
a.append(2)
a.append(3)
# [1,2,3]
print(a)

# 使用索引添加
a.insert(2, 10)
print(a)

# 访问元素  用索引（下标）访问元素
temp = a[2]
print(temp)

# 更新元素
a[2] = 89
print(a)

# 删除元素
# 时间复杂度O(n)
a.append(10)
a.remove(89)
print(a)
a.pop(2)
print(a)
# 时间复杂度O(1)
a.pop()  # 删除最后一个元素
print(a)

# 获取数组长度
b = [1, 5, 8, 9]
size = len(b)
print(size)

# 遍历数组
for i in a:
    print(i)

for index, value in enumerate(a):
    print(index, value)

for i in range(0, len(a)):
    print("i:", i, "element:", a[i])

# 查找某个元素
index=a.index(2)
print(index)

# 数组排序
# 时间复杂度O(NlogN)
a=[1,3,2]
# 从小到大排序
a.sort()
print(a)

# 倒序
a.sort(reverse=True)
print(a)

