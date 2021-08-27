#map传入两个参数，一个函数，一个可迭代对象
# 遍历可迭代对象传入函数，函数处理后全部放入可迭代对象中返回

lis = [1,34,2,4,5,6,7,8]
def func(n):
    return n*2

res = map(func,lis)
print(list(res))
