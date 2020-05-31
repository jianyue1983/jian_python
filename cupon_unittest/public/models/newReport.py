#!/usr/bin/env python
# _*_ coding:utf-8 _*_
__author__ = 'jianjiajing'


import os

def new_report(testreport):
    """
    生成最新的测试报告文件
    :param testreport:
    :return:返回文件
    """
    lists = os.listdir(testreport)
    # 获取最新文件的绝对路径，列表中最后一个值,文件夹+文件名
    lists.sort(key=lambda fn: os.path.getmtime(testreport + "\\" + fn))
    file_new = os.path.join(testreport,lists[-1])
    return file_new