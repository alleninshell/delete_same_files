__author__ = 'LiWenyu'
# -*- coding: cp936 -*-
import hashlib
import os
from time import clock as now


def getmd5(filename):
    file_txt = open(filename, 'rb').read()
    m = hashlib.md5()
    m.update(file_txt)
    return m.hexdigest()


def main():
    path = u'D:\\test2'
    all_md5 = {}
    all_size = {}
    total_file = 0
    total_delete = 0
    start = now()
    print("start")
    for file in os.listdir(path):
        total_file += 1
        real_path = os.path.join(path, file)
        if os.path.isfile(real_path):
            size = os.stat(real_path).st_size
            name_and_md5 = [real_path, '']
            if size in all_size.keys():
                print('finded')
                new_md5 = getmd5(real_path)
                if all_size[size][1] == '':
                    all_size[size][1] = getmd5(all_size[size][0])
                if new_md5 in all_size[size]:
                    print("DELETE:" + file)
                    os.remove(path+'\\'+file)
                    total_delete += 1
                else:
                    all_size[size].append(new_md5)
            else:
                all_size[size] = name_and_md5
    end = now()
    time_last = end - start
    print('TOTAL NUMBER:', total_file)
    print('DELETED NUMBER:', total_delete)
    print('TIME COST:', time_last, 'SEC')


if __name__ == '__main__':
    main()
