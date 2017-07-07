# __author__ = 'zs'
# -*- coding: utf-8 -*-
# @Time : 2017/7/6 16:39

s = 'hello'
s_list = list(s)
print('s_list:', s_list)

a = (1, 2, 3)
t_list = list(a)
print('t_list:', t_list)

# 1、index方法,如果没找到相应的元素，则会抛出异常
# ValueError: 55 is not in list
numbers = [1, 2, 3, 4, 5, 5, 6, 7, 8]
i = numbers.index(5)
print('5出现第一次的位置:', i)

words = ['hello', 'world', 'you', 'me', 'he']
_i = words.index('me')
print('_i:', _i)

# 2、count方法,返回元素出现的次数
print('元素5在numbers中出现的次数:', numbers.count(5))

# 3、append用于追加元素,append 方法用于在列表末尾增加新的元素
numbers.append(9)
print('numbers:', numbers)
numbers.append([10, 11])
print('numbers:', numbers)





