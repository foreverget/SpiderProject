import threading
import time
"""
threading模块是python中专门提供用来做多线程编程的模块。threading模块中最常用的类是Thread。
"""

def coding():
    for x in range(3):
        print('%s正在写代码' % x)
        time.sleep(1)

def drawing():
    for x in range(3):
        print('%s正在画图' % x)
        time.sleep(1)


def single_thread():
    coding()
    drawing()

def multi_thread():
    t1 = threading.Thread(target=coding)
    t2 = threading.Thread(target=drawing)

    t1.start()
    t2.start()

if __name__ == '__main__':
    multi_thread()