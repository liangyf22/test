
class MyTest(object):
    @classmethod    # 被classmethod装饰后就是类方法，类方法可以被类调用，也可以被实例调用
    def foo(cls): #cls 代表类本身
        print("被装饰的类方法")

    def boo(self):  #self 代表实例本身，只能被实例调用
        print("没被装饰的实例方法")


MyTest.foo()  #类调用类方法
t = MyTest()
t.foo() #实例调用类方法
t.boo() #实例调用实例方法
