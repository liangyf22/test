# zip() 函数用于将可迭代的对象作为参数，将对象中对应的元素打包成一个个元组，然后返回由这些元组组成的列表。
#
# 如果各个迭代器的元素个数不一致，则返回列表长度与最短的对象相同，利用 * 号操作符，可以将元组解压为列表。
#
# zip 方法在 Python 2 和 Python 3 中的不同：在 Python 3.x 中为了减少内存，zip() 返回的是一个对象
lis1= [1,2,3,4]
lis2 = ['a','b','c']

res = list(zip(lis1,lis2))
print(res)
res2 = zip(*res)
print(list(res2))
