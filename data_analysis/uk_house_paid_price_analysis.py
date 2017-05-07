# -*- coding: GBK -*-
# filename: multiprocessreadfile.py

import datetime
import os
import multiprocessing

"""
多进程分块读取文件
"""

DATA_FILE = "/Users/leizhang/Downloads/UK_House_Price_paid_data/pp-complete.csv"
OUT_FILE = "/Users/leizhang/Downloads/ret.log"
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
    price = line.split(',')[1].replace('"', '')
    transaction_date = line.split(',')[2].replace('"', '')
    date_year_month = transaction_date.split('-')[0]+transaction_date.split('-')[1]

    post_code = line.split(',')[3].replace('"', '')
    if not post_code: return
    outward_code = post_code.split(' ')[0]

    # D = Detached, S = Semi-Detached, T = Terraced, F = Flats/Maisonettes, O = Other
    property_type = line.split(',')[4].replace('"', '')

    # Y = a newly built property, N = an established residential building
    old_or_new = line.split(',')[5].replace('"', '')

    if Summary.get(outward_code):
        if Summary[outward_code].get(date_year_month):
            Summary[outward_code][date_year_month]['count'] += 1
            Summary[outward_code][date_year_month]['total_price'] += int(price)
            Summary[outward_code][date_year_month]['avg_price'] = float(
                float(Summary[outward_code][date_year_month]['total_price']) / Summary[outward_code][date_year_month]['count'])

            if property_type == 'D':
                Summary[outward_code][date_year_month]['D_count'] += 1
            elif property_type == 'S':
                Summary[outward_code][date_year_month]['S_count'] += 1
            elif property_type == 'T':
                Summary[outward_code][date_year_month]['T_count'] += 1
            elif property_type == 'F':
                Summary[outward_code][date_year_month]['F_count'] += 1
            elif property_type == 'O':
                Summary[outward_code][date_year_month]['O_count'] += 1
            else:
                Summary[outward_code][date_year_month]['E1_count'] += 1

            if old_or_new == 'Y':
                Summary[outward_code][date_year_month]['Y_count'] += 1
            elif old_or_new == 'N':
                Summary[outward_code][date_year_month]['N_count'] += 1
            else:
                Summary[outward_code][date_year_month]['E2_count'] += 1

        else:
            Summary[outward_code][date_year_month] = {}
            Summary[outward_code][date_year_month]['count'] = 1
            Summary[outward_code][date_year_month]['total_price'] = int(price)
            Summary[outward_code][date_year_month]['avg_price'] = int(price)

            Summary[outward_code][date_year_month]['D_count'] = 0
            Summary[outward_code][date_year_month]['S_count'] = 0
            Summary[outward_code][date_year_month]['T_count'] = 0
            Summary[outward_code][date_year_month]['F_count'] = 0
            Summary[outward_code][date_year_month]['O_count'] = 0
            Summary[outward_code][date_year_month]['E1_count'] = 0
            Summary[outward_code][date_year_month]['Y_count'] = 0
            Summary[outward_code][date_year_month]['N_count'] = 0
            Summary[outward_code][date_year_month]['E2_count'] = 0

            if property_type == 'D':
                Summary[outward_code][date_year_month]['D_count'] = 1
            elif property_type == 'S':
                Summary[outward_code][date_year_month]['S_count'] = 1
            elif property_type == 'T':
                Summary[outward_code][date_year_month]['T_count'] = 1
            elif property_type == 'F':
                Summary[outward_code][date_year_month]['F_count'] = 1
            elif property_type == 'O':
                Summary[outward_code][date_year_month]['O_count'] = 1
            else:
                Summary[outward_code][date_year_month]['E1_count'] = 1

            if old_or_new == 'Y':
                Summary[outward_code][date_year_month]['Y_count'] = 1
            elif old_or_new == 'N':
                Summary[outward_code][date_year_month]['N_count'] = 1
            else:
                Summary[outward_code][date_year_month]['E2_count'] = 1

    else:
        Summary[outward_code] = {}
        Summary[outward_code][date_year_month] = {}

        Summary[outward_code][date_year_month]['count'] = 1
        Summary[outward_code][date_year_month]['total_price'] = int(price)
        Summary[outward_code][date_year_month]['avg_price'] = int(price)

        Summary[outward_code][date_year_month]['D_count'] = 0
        Summary[outward_code][date_year_month]['S_count'] = 0
        Summary[outward_code][date_year_month]['T_count'] = 0
        Summary[outward_code][date_year_month]['F_count'] = 0
        Summary[outward_code][date_year_month]['O_count'] = 0
        Summary[outward_code][date_year_month]['E1_count'] = 0
        Summary[outward_code][date_year_month]['Y_count'] = 0
        Summary[outward_code][date_year_month]['N_count'] = 0
        Summary[outward_code][date_year_month]['E2_count'] = 0

        if property_type == 'D':
            Summary[outward_code][date_year_month]['D_count'] = 1
        elif property_type == 'S':
            Summary[outward_code][date_year_month]['S_count'] = 1
        elif property_type == 'T':
            Summary[outward_code][date_year_month]['T_count'] = 1
        elif property_type == 'F':
            Summary[outward_code][date_year_month]['F_count'] = 1
        elif property_type == 'O':
            Summary[outward_code][date_year_month]['O_count'] = 1
        else:
            Summary[outward_code][date_year_month]['E1_count'] = 1

        if old_or_new == 'Y':
            Summary[outward_code][date_year_month]['Y_count'] = 1
        elif old_or_new == 'N':
            Summary[outward_code][date_year_month]['N_count'] = 1
        else:
            Summary[outward_code][date_year_month]['E2_count'] = 1


def printAnalyseRes():
    global Summary
    fp = open(OUT_FILE, 'w')
    for key in Summary:
        for key1 in Summary[key]:
            retstr = key + ',' + key1 + ',' + str(Summary[key][key1]['count']) + ',' \
                     + str(Summary[key][key1]['avg_price']) + ',' + str(Summary[key][key1]['D_count']) \
                     + ',' + str(Summary[key][key1]['S_count']) + ',' + str(Summary[key][key1]['T_count']) \
                     + ',' + str(Summary[key][key1]['F_count']) + ',' + str(Summary[key][key1]['O_count']) \
                     + ',' + str(Summary[key][key1]['Y_count']) + ',' + str(Summary[key][key1]['N_count']) \
                     + ',' + str(Summary[key][key1]['E1_count']) + ',' + str(Summary[key][key1]['E2_count']) \
                     + '\n'
            fp.write(retstr)
    fp.close()


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
