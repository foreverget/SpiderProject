from threading import Thread, current_thread
# 子线程
import time


def run(id):
    print('%s#%d开始执行' % (current_thread().name,id,))
    time.sleep(2)
    # ...
    print('子线程执行结束')


if __name__ == '__main__':
    print('主线程开始执行')
    # 创建子线程
    t = Thread(target=run, args=(1,), name='子线程')
    # 启动线程
    t.setDaemon(True)
    t.start()
    print(t.isAlive())
    # t.join()

    print('主线程结束执行')
    # print(t.isAlive())