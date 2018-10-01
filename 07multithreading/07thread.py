import threading
import time
"""
为了让线程代码更好的封装。可以使用threading模块下的Thread类，继承自这个类，然后实现run方法，线程就会自动运行run方法中的代码。
"""

class CodingThread(threading.Thread):
    def run(self):
        for x in range(3):
            print('%s正在写代码' % threading.current_thread())
            time.sleep(1)

class DrawingThread(threading.Thread):
    def run(self):
        for x in range(3):
            print('%s正在画图' % threading.current_thread())
            time.sleep(1)

def multi_thread():
    t1 = CodingThread()
    t2 = DrawingThread()

    t1.start()
    t2.start()

if __name__ == '__main__':
    multi_thread()