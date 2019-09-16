"""
更改文件编码,文件统一改为utf-8无BOM
"""
# -*- coding: UTF-8 -*-
import os
import pandas as pd

coding = 'utf-8'
file_dir = 'path'  # 文件夹目录


def run_coding():
    for root, dirs, files in os.walk(file_dir, topdown=False):
        for i in files:
            files_name = os.path.join(root, i)
            try:
                df1 = pd.read_csv(files_name, encoding='utf-8')
            except:
                df1 = pd.read_csv(files_name, encoding='gbk')
            df1.to_csv(files_name, encoding=coding, index=None)


if __name__ == '__main__':
    run_coding()
    print("It's done")