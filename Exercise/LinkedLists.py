# -*- coding: utf-8 -*-
# @Time    : 2024-03-23 15:26
# @Author  : Lindand
# @File    : LinkedLists.py
# @Description :链表的常用操作
from collections import deque

# 1.创建链表
linkedlist = deque()

# 2.添加元素
# 时间复杂度O(1)
linkedlist.append(2)
linkedlist.append(3)
linkedlist.append(8)
linkedlist.append(4)
linkedlist.append(2)

# deque([2, 3, 8, 4])
print(linkedlist)

# 时间复杂度O(N)
linkedlist.insert(3, 10)
print(linkedlist)

# 3.访问元素
# 时间复杂度O(N)
element = linkedlist[2]
print(element)

# 4.搜索元素（使用索引
# 时间复杂度O(N)
index = linkedlist.index(3)
print(index)

# 5.更新元素
# 时间复杂度O(N)
linkedlist[3]=99
print(linkedlist)

# 6.删除元素
# 时间复杂度0(N)
linkedlist.remove(2)
print(linkedlist)

# 7.获取长度
# 时间复杂度O(1)
length=len(linkedlist)
print(length)