# __new__魔法函数，作用new一个对象，通过重写__new__可实现单例模式

class MyClass(object):
    def __new__(cls, *args, **kwargs):
        print("这是一个new函数")
        # return object.__new__(cls) #返回实例对象方法一
        return super().__new__(cls) #返回实例对象方法二

t = MyClass()
print(t)


# 单例模式：每次实例化，都是使用第一次实例化的属性。实例的属性可以通用，有点类似定义了一个全局变量。
# 这样可以节省内存

# 代码实现单例模式

class Mytest(object):
    _instance = None    #定义一个类属性，用于判断是否已经实例化
    def __new__(cls, *args, **kwargs):
        if not cls._instance:   #如果cls._instance 为false,那么没有实例化，则使用__new__实例化一个对象，并返回赋值给cls._instance
            cls._instance = object.__new__(cls)
            return cls._instance
        else:
            return cls._instance


t1 = Mytest()
t1.name = 'zhangsan'
t2 =Mytest()
print(t2.name)
print(id(t1))
print(id(t2))