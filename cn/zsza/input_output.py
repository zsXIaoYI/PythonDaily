# __author__ = 'zs'
# -*- coding: utf-8 -*-
# @Time : 2017/2/3 16:22
import sys
from Tools.scripts.treesync import raw_input

py_encode = sys.getdefaultencoding()
print('py_encode:', py_encode)

hello = '你好'
print('hello:', hello)

print('hello, world')
print('my name is', '小k')
print(100 + 200 + 300)
print('100 + 200 =', 100 + 200)


# Python2中的raw_input
# 不管我们输入一个字符串、数值还是表达式，raw_input 都直接返回一个字符串
name = raw_input('please enter your name: ')
print('type 函数:', type(name))
print('name:', name)

# eval函数用以执行一个字符串表达式
n1 = eval('1+2')
print('n1:', n1)

n = 9
n2 = eval('n+1')
print('n2:', n2)

# 格式化输出
s1 = 'hello'
l = len(s1)
print('the length of %s is %d' % (s1, l))

for i in range(0, 3):
    print(i, end=' ')              # 加end则不会换行输出


