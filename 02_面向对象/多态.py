# @Author  : liangyf
# @Time    : 2021/8/9 22:21

# 面向对象三大特性  继承、多态、封装

#多态  子类重写了父类的方法，实现不同的功能

class perple(object):

    def work(self):
        print("都要996")
    def eat(self):
        print("吃饭")


class xiaoming(perple):

    def eat(self):
        print("吃水果")

class laowang(perple):

    def eat(self):
        print("吃烧烤")



a_obj = perple()
a_obj.eat()
a_obj.work()

b_obj =xiaoming()
b_obj.eat()
a_obj.work()


c_obj = laowang()
c_obj.eat()
a_obj.work()
