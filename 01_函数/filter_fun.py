# filter（）参数为一个函数、一个为迭代对象。
# 遍历可迭代对象依次传入函数，将为ture数据放入的一个可迭代对象中并返回
# 做过滤作用

lis = [1,23,2,3,546,33,5,7]
def func(n):
    return n>10

res =filter(func,lis)
print(list(res))

