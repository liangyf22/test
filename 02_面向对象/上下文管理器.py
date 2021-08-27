# with open("name.txt") as f:
#     f.read()
# 这就是一个上下管理的例子
# 打开文件后，退出后自动关闭
#
# with 后面跟的是一个上下管理对象

# 上下文管理器其实就是实现了__enter__和__exit__的类

class Myopen(object):
    def __init__(self, file_name, open_method, encoding):
        self.file_name = file_name
        self.open_method = open_method
        self.encoding = encoding

    def __enter__(self):
        self.f = open(self.file_name, self.open_method, encoding=self.encoding)
        return self.f

    def __exit__(self, exc_type, exc_val, exc_tb):
        print(exc_tb)
        print(exc_val)
        print(exc_tb)


with Myopen("test.txt", "r", "utf-8") as f:
    content = f.read()
    print(content)
