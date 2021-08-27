# 实现了__call__方法的类，允许一个类的实例像函数一样被调用：x(a, b) 调用 x.__call__(a, b)


class Myclass(object):
     def __init__(self,func):
         self.func =func

     def __call__(self, *args, **kwargs):
         print("洗手")
         self.func()
         print("擦嘴")

@Myclass # func = Myclass()
def func():
    print("吃饭了")

func()