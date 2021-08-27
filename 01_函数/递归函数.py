'''
1、函数里调用函数本身
2、有递归边界

通过递归函数实现任意数的阶乘
'''
import json


def js(num):
    if num == 1:
        return 1
    else:
        return num * js(num - 1)


print(js(3))


# 斐波那契数列
# 斐波那契数列指的是这样一个数列 0, 1, 1, 2, 3, 5, 8, 13,特别指出：第0项是0，第1项是第一个1。从第三项开始，每一项都等于前两项之和。

def fbnq(n):
    if n == 1:
        return 0
    elif (n == 2 or n == 3):
        return 1
    else:
        return fbnq(n - 1) + fbnq(n - 2)


res = fbnq(7)
print(res)


def fib_loop_for(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a
print(fib_loop_for(6))