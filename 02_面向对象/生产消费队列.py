# @Author  : liangyf
# @Time    : 2021/9/3 22:36
import queue

# 创建一个队列
import time
from threading import Thread

q = queue.Queue()

# 生产和消费队列
class Producer(Thread):
    """生产者"""
    def run(self):
        # 判断列表中的商品是否少于500，少于后生产1000个
        count = 0
        while True:
            if q.qsize() < 500:
                for i in range(1000):
                    count +=1
                    goods = '--第{}个商品--'.format(count)
                    q.put(goods)
                    print('生产：',goods)
                time.sleep(1)

class Consumer(Thread):
    """消费者"""

    def run(self):
        while True:
            if q.qsize()>10:
                for i in range(500):
                    print('消费{}'.format(q.get()))
            time.sleep(0.01)

# 一个生产者线程
p = Producer()
p.start()

# 五个消费者线程

for i in range(5):
    c = Consumer()
    c.start()

