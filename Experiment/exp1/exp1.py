# -*- coding: utf-8 -*-
# @Time : 2021/9/29 22:21
# @Author : 武梓龙
# @File : exp1.py
# @Software: PyCharm
import re
from collections import Counter

g_max_word_length = 2  # 最大的切分片段的长度

# 获得ngram切分
OneWord = []  # 一个字
TwoWord = []  # 两个字


def Count_ListToDict(list):
    temp = Counter(list)
    sorted_list = sorted(temp.items(), key=lambda x: x[1], reverse=True)
    Dict = dict(sorted_list)
    return Dict


def build_ngram_word(content, word_length):
    for i in range(0, len(content) - word_length + 1):
        word = "".join(content[i:i + word_length])
        if re.findall('[^\u4e00-\u9fa5]', word):
            # 如果单个的分词含有“非中文”，则跳过（re.findall返回的是一个列表，“列表为空”在if语句中即代表false；正则表达式匹配的是"非中文"）
            continue
        if word_length == 1:
            OneWord.append(word)
        if word_length == 2:
            TwoWord.append(word)


# 构建所有长度的切分片段
def build_all_ngram_word(content):
    for word_length in range(1, g_max_word_length + 1):
        build_ngram_word(content, word_length)


with open('Ci.txt', 'r', errors='ignore') as f:
    content = f.read()

build_all_ngram_word(content)

# 统计词频 + 输出
sorted_OneWord_dict = Count_ListToDict(OneWord)
sorted_TwoWord_dict = Count_ListToDict(TwoWord)
with open('OneWord.txt', 'w', encoding="utf-8") as cp:
    for oneword in sorted_OneWord_dict:
        cp.write(oneword + " " + str(sorted_OneWord_dict[oneword]) + '\n')
with open('TwoWord.txt', 'w', encoding="utf-8") as cp:
    for twoword in sorted_TwoWord_dict:
        cp.write(twoword + " " + str(sorted_TwoWord_dict[twoword]) + '\n')
