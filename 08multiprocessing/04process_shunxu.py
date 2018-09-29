from multiprocessing import Process
from time import sleep
import os



# 子进程
def run():
    print('子进程开始执行--%s' % (os.getpid(),))
    sleep(10)
    print('子进程执行结束')


if __name__ == '__main__':
    print('父进程开始执行--%s' % (os.getpid(),))
    # 创建子进程
    p = Process(target=run)
    p.start()

    p.join(timeout=5)

    print('父进程执行结束')