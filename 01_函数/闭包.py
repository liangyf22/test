# 闭包条件
# 1、函数里嵌套了函数
# 2、外层函数返回的是嵌套函数名
# 3、嵌套函数引用外层函数非全局的变量

def func1(n):
    def func2():
        return 2*n
    return func2

res = func1(10)
print(res.__closure__)  #被引用的的外部变量会被保存到__closure__属性中
print(res())
