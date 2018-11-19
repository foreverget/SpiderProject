from multiprocessing import Process
import time

# 创建子进程
class MyProcess(Process):
    def __init__(self,name,*args,**kwargs):
        # 调用父类的init()方法
        super().__init__(*args,**kwargs)
        self.id = id

    # 重写run方法
    def run(self):
        print('子进程%d开始执行--%s'%(self.id,self.pid))
        time.sleep(2)
        print('子进程%d执行结束--%s'%(self.id,self.pid))

if __name__ == '__main__':
    #　主进程
    print('主进程开始执行')
    p = MyProcess(name='子进程',id = 1)
    p.start()
    time.sleep(3)

    print('主进程结束')