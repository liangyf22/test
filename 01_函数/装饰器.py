# 装饰器的本质就是闭包
# 装饰器的作用，在不修改原函数的前提下，实现函数功能的拓展。

def login(index): #传入被装饰的函数
    def foo():
        usernamae ='python'
        password = '123'
        u = input('请输入用户名')
        p = input('请输入密码')
        if usernamae== u and password == p:
            index() #执行传入进来的被装饰函数
        else:
            print("用户名或密码错误")
    return foo


#@login -->语法糖
# 等同于 index = login(index)  ,将被装饰的函数传入login函数，然后返回了foo 函数，并赋值给名字相同的index。
# 同时index函数被存在login.__closure__属性中。
# 当执行index()时，便执行了foo()
@login
def index():
    print('欢迎来到首页')
# index()

# index=login(index)
# print(index.__closure__)
# index()


#带参数的装饰器

def login2(buy): #传入被装饰的函数
    def foo2(*avgs,**kwargs):
        usernamae ='python'
        password = '123'
        u = input('请输入用户名')
        p = input('请输入密码')
        if usernamae== u and password == p:
            buy(*avgs,**kwargs) #使用了foo2传入的参数
        else:
            print("用户名或密码错误")
    return foo2


@login2
def buy(name):
    print('购买了{}商品'.format(name))

# buy('张三')



#装饰类


def login3(Myclass): #传入被装饰的函数
    def foo2(*avgs,**kwargs):
        usernamae ='python'
        password = '123'
        u = input('请输入用户名')
        p = input('请输入密码')
        if usernamae== u and password == p:
            return Myclass(*avgs,**kwargs) #z装饰类没有返回值，所以这里要加个return
        else:
            print("用户名或密码错误")
    return foo2


@login3
class Myclass:
    def __init__(self,n,m):
        self.n = n
        self.m = m
    def add(self):
        return (self.n+self.m)

my = Myclass(3,4)
print(my.add())
