# -*- coding: GBK -*-
# filename: multiprocessreadfile.py

import datetime
import os
import multiprocessing

"""
多进程分块读取文件
"""

DATA_FILE = "/Users/leizhang/Downloads/ukpostcodes.txt"
WORKERS = 4
BLOCKSIZE = 100000000  # 字节，接近100MB
FILE_SIZE = 0
Summary = {}


def getFilesize(file):
    """
        获取要读取文件的大小
    """
    global FILE_SIZE
    fstream = open(file, 'r')
    fstream.seek(0, os.SEEK_END)
    FILE_SIZE = fstream.tell()
    fstream.close()


def analyseLine(line):
    global Summary

    post_code = line.split(',')[1]
    outward_code = post_code.split(' ')[0]
    lati = line.split(',')[2]
    longi = line.split(',')[3]

    if Summary.get(outward_code):
        Summary[outward_code]['count'] += 1
        Summary[outward_code]['total_lati'] += float(lati)
        Summary[outward_code]['avg_lati'] = float(
            float(Summary[outward_code]['total_lati']) / Summary[outward_code]['count'])
        Summary[outward_code]['total_longi'] += float(longi)
        Summary[outward_code]['avg_longi'] = float(
            float(Summary[outward_code]['total_longi']) / Summary[outward_code]['count'])
    else:
        Summary[outward_code] = {}
        Summary[outward_code]['count'] = 1
        Summary[outward_code]['total_lati'] = float(lati)
        Summary[outward_code]['avg_lati'] = float(lati)
        Summary[outward_code]['total_longi'] = float(longi)
        Summary[outward_code]['avg_longi'] = float(longi)


def printAnalyseRes():
    global Summary
    for key in Summary:
        print(key + ',' + str(Summary[key]['count']) + ',' + str(Summary[key]['avg_lati']) + ',' + str(Summary[key]['avg_longi']))


def process_found(pid, array, file, rlock, rlock1):
    global FILE_SIZE
    global JOB
    global PREFIX
    """
        进程处理
        Args:
            pid:进程编号
            array:进程间共享队列，用于标记各进程所读的文件块结束位置
            file:所读文件名称
        各个进程先从array中获取当前最大的值为起始位置startpossition
        结束的位置endpossition (startpossition+BLOCKSIZE) if (startpossition+BLOCKSIZE)<FILE_SIZE else FILE_SIZE
        if startpossition==FILE_SIZE则进程结束
        if startpossition==0则从0开始读取
        if startpossition!=0为防止行被block截断的情况，先读一行不处理，从下一行开始正式处理
        if 当前位置 <=endpossition 就readline
        否则越过边界，就从新查找array中的最大值
    """
    getFilesize(file)
    fstream = open(file, 'r')
    while True:
        rlock.acquire()
        startpossition = max(array)
        endpossition = array[pid] = (startpossition + BLOCKSIZE) if (
                                                                        startpossition + BLOCKSIZE) < FILE_SIZE else FILE_SIZE
        print('pid%s' % pid, ','.join([str(v) for v in array]))
        rlock.release()

        if startpossition == FILE_SIZE:  # end of the file
            print('===============pid%s end===============' % (pid))
            printAnalyseRes()
            break
        elif startpossition != 0:
            fstream.seek(startpossition)
            fstream.readline()
        pos = ss = fstream.tell()

        while pos < endpossition:
            # 处理line
            line = fstream.readline()
            rlock1.acquire()
            analyseLine(line)
            rlock1.release()
            pos = fstream.tell()
        ee = fstream.tell()
    fstream.close()


def main():
    global FILE_SIZE

    print(datetime.datetime.now().strftime("%Y/%d/%m %H:%M:%S"))
    file = DATA_FILE
    getFilesize(file)
    print(FILE_SIZE)

    rlock = multiprocessing.RLock()
    rlock1 = multiprocessing.RLock()
    array = multiprocessing.Array('l', WORKERS, lock=rlock)

    threads = []
    for i in range(WORKERS):
        p = multiprocessing.Process(target=process_found, args=[i, array, file, rlock, rlock1])
        threads.append(p)

    for i in range(WORKERS):
        threads[i].start()

    for i in range(WORKERS):
        threads[i].join()

    print(datetime.datetime.now().strftime("%Y/%d/%m %H:%M:%S"))


if __name__ == '__main__':
    main()
