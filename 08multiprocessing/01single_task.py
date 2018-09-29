from time import sleep



# 任务二
def run():
    while True:
        print('today is hot')
        sleep(2)


if __name__ == '__main__':

    # 主进程
    # 任务一
    # 阻塞
    while True:
        print('today is a good day.')
        sleep(1)

    # 执行任务二
    run()