from multiprocessing import Process
from time import sleep
import os

num=100

def run():
    print('子进程开始执行--%s'%(os.getppid(),))
    # 对全局变量操作
    global num
    num+=1
    print(num)
    sleep(2)
    print('子进程执行结束')

if __name__ == '__main__':
    print('主进程开始执行')
    #　创建子进程
    p = Process(target=run)
    p2 = Process(target=run)
    p.start()
    p2.start()
    #　显示全局变量
    sleep(3)
    print(num)
    print('主进程执行结束')