from multiprocessing import Process
from time import sleep
import os


def run(desc):
    while True:
        print('today is %s--%s--%s' % (desc, os.getpid(), os.getppid()))
        sleep(3)
        # break


if __name__ == '__main__':
    # 主进程
    print('主进程开始执行--%s' % (os.getpid(),))
    # 创建进程执行run
    # p = Process(target=run, args=('rainy',))
    p = Process(name='天气',target=run, kwargs={'desc': 'hot'})
    # p.daemon = True
    # 启动进程
    p.start()
    print(p.is_alive())
    print(p.exitcode)
    print(p)
    # p.join(timeout=1)
    sleep(2)
    p.terminate()
    print(p.is_alive())
    print(p.exitcode)
    print(p.pid)


    while True:
        print('today is a good day.')
        sleep(3)
        break
