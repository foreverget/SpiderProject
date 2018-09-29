from multiprocessing import Pool
from shutil import copyfile

# 定义拷贝文件的函数
import os

import time

source = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'files')
dest = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'tofiles')


def copy_file(source, dest):
    old_file = open(source, 'rb')
    new_file = open(dest, 'wb')
    # 读取内容
    content = old_file.read()
    # 写入新文件。
    new_file.write(content)
    # 关闭文件。
    old_file.close()
    new_file.close()


if __name__ == '__main__':
    # 读出files目录下的所有文件。
    file_list = os.listdir(source)
    # 循环拷贝文件。
    start = time.time()
    pp = Pool(8)
    for file_name in file_list:
        pp.apply_async(copyfile(os.path.join(source, file_name), os.path.join(dest, file_name)))
    end = time.time()

    print('耗费时间%.2f' % (end-start))