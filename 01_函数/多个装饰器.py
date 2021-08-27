
import time
def timer(func):
    """
    :param func: 被装饰函数
    :return: None
    """
    def wrapper(*args,**kwargs):
        start_time = time.time()
        print('开始时间{}:'.format(start_time))
        res =func()
        end_time = time.time()
        print('结束时间:{}'.format(end_time))
        print('运行时间:{}'.format(end_time-start_time))
        return res
    return wrapper

with open('userinfo.txt') as f:
    userinfo = eval(f.read())
    print(userinfo)

def login_check(func):
    """
    验证功能的装饰器
    :param func:
    :return:
    """
    def ado(*args):
        if not userinfo['Token']:
            print("登录页面")
            username = input('请输入用户名：')
            password = input('请输入密码：')
            if userinfo["user"] == username and  userinfo["psw"] == password:
                userinfo['Token'] = True
                print('登录验证成功')
                func()
        else:
            print('已经验证过')
            func()
    return ado



@login_check
@timer
def goods():
    time.sleep(3)
    print('查询商品页面')
"""
装饰从下往上装饰，执行从上往下执行
"""

goods()
goods()