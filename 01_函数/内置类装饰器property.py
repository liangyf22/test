class MyTest(object):
    @classmethod    # 被classmethod装饰后就是类方法，类方法可以被类调用，也可以被实例调用
    def foo(cls): #cls 代表类本身
        print("被装饰的类方法")

    def boo(self):  #self 代表实例本身，只能被实例调用
        print("没被装饰的实例方法")
    @staticmethod
    def too():  #静态方法没有默认参数，可以被类调用，也可以被实例调用.  方法体中不能使用类或实例的任何属性和方法
        print("这是被staticmethod装饰的静态方法")

    @property #设置只读属性，可以跟调用类属性一样调用
    def read_attr(self):
        print("被property装饰，可以像属性一样被调用，且不允许修改")
        return 'dd'

t = MyTest()

print(t.read_attr)