from multiprocessing import Pool
import time
import random



def run(id):
    print('子进程#%d开始执行' % (id,))
    start = time.time()
    time.sleep(random.choice([1, 2, 3]))
    end = time.time()
    print('子进程#%d执行结束, 耗时%.2f' % (id, (end-start)))


if __name__ == '__main__':
    print('主进程开始执行')
    # 创建进程池
    pp = Pool(5)
    # 往进程池中添加进程
    for i in range(6):
        pp.apply_async(run, args=(i,))

    # 关闭进程池
    pp.close()
    # 等待进程池中的进程结束
    pp.join()

    print('主进程结束执行')

