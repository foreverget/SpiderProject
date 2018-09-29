from threading import Thread
import time


# 定义全局变量
num = 100

def run(id):
    print('子线程#%d开始执行' % (id,))
    global num
    num += 1
    time.sleep(3)
    print(num)
    print('子线程#%d结束执行' % (id,))


if __name__ == '__main__':
    print('主线程开始执行')
    t = Thread(target=run, args=(1,))
    t.start()
    t.join()
    print('num=', num)

    print('主线程结束执行')