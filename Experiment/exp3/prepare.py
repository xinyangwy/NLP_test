# -*- coding: utf-8 -*-
# @Time : 2021/10/26 19:53
# @Author : 信仰
# @File : prepare.py
# @Software: PyCharm
import re
from tkinter import *
from tkinter.tix import Tk, Control, ComboBox
from tkinter.messagebox import showinfo, showwarning, showerror
import pickle

yuliaos = []
danci_set = []
shuangci_set = []
sanci_set = []
sici_set = []
wuci_set = []
danci_dict = {}
shuangci_dict = {}
sanci_dict = {}
sici_dict = {}
wuci_dict = {}
weichuli = []


def is_chinese(uchar):
    if uchar >= u'\u00a4' and uchar <= u'\uffe5':
        return True
    else:
        return False


def analyse_yuliaoku(lines):
    for i in range(0, len(lines)):
        lines[i] = lines[i].rstrip('\n')  # 右边换行符

    for line in lines:
        sts = re.split(' ', line)  # 以“ ”为分割处；sts（每行删去“ ”的部分）
        for i in range(0, len(sts)):  # 删除sts中的/t  /n  /m /q 英文单词  等等（）保留的有中文的标点符号等等
            for ch in sts[i]:
                if is_chinese(ch) == False:
                    sts[i] = sts[i].replace(ch, '')
        while '' in sts:  # 删除此sts列表中的“空元素”
            sts.remove('')
        if sts != '':
            weichuli.append(sts)

    for line in weichuli:
        for word in line:
            if len(word) == 1:
                danci_set.append(word)
            elif len(word) == 2:
                shuangci_set.append(word)
            elif len(word) == 3:
                sanci_set.append(word)
            elif len(word) == 4:
                sici_set.append(word)
            elif len(word) == 5:
                wuci_set.append(word)

    # 对列表中的元素统计词频存入字典
    for danci in danci_set:
        if danci in danci_dict:
            danci_dict[danci] += 1
        else:
            danci_dict[danci] = 1
    for shuangci in shuangci_set:
        if shuangci in shuangci_dict:
            shuangci_dict[shuangci] += 1
        else:
            shuangci_dict[shuangci] = 1
    for sanci in sanci_set:
        if sanci in sanci_dict:
            sanci_dict[sanci] += 1
        else:
            sanci_dict[sanci] = 1
    for sici in sici_set:
        if sici in sici_dict:
            sici_dict[sici] += 1
        else:
            sici_dict[sici] = 1
    for wuci in wuci_set:
        if wuci in wuci_dict:
            wuci_dict[wuci] += 1
        else:
            wuci_dict[wuci] = 1


with open('1998-01-2003版-带音.txt', errors='ignore') as yuliaoku:
    lines = yuliaoku.readlines()
    analyse_yuliaoku(lines)

with open("exp3Data.pickle", "wb")as f:  # 通过with open()的时候可以自动关闭
    pickle.dump(danci_dict, f)
    pickle.dump(shuangci_dict, f)
    pickle.dump(sanci_dict, f)
    pickle.dump(sici_dict, f)
    pickle.dump(wuci_dict, f)
