# __str__和__repr__都用于返回字符串
# 重写__str__和__repr__必须有return值且必须是字符串
# object 的__str__和__repr__返回的是对象
#
# 触发条件
# print()/ str()/format() 都是触发__str__(当没有重写__str__，但是重写__repr__时，也可以触发__repr__。都没有重写则查找父类的__str__。
# 可以理解为__repr__是__str__的备胎)
# 交互命令 、 obj   repr 触发__repr__

class TestClass(object):

    def __init__(self,name):
        self.name = name

    def __str__(self):
        print("触发了__str__")
        return self.name

    def __repr__(self):
        print("触发了__repr__")
        return self.name

t = TestClass("zhangsan")
print(t)
format(t)
str(t)

repr(t)