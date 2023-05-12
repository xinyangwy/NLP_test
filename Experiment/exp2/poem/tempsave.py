from exp1 import *
# from tkinter import *
# from tkinter.tix import Tk, Control, ComboBox
# from tkinter.messagebox import showinfo, showwarning, showerror
import random
# import streamlit as st
import pickle

del_lines = []  # 删除的行（诗人）
ci_set = []
same_cipai_ci = []
twoword_list_final = []
cipai_set = []


class ci_class(object):
    def __init__(self, cipai, ciwen):
        self.cipai = cipai
        self.ciwen = ciwen


class cipai_class(object):  # dj就是ci_set中的 duanju_ci
    def __init__(self, cipai, dj):
        self.cipai = cipai
        self.duanju_list = []
        self.duanju_list.append(dj)


# 给ci.set中添加元素：duanju_ci 标签
def duanju(ststring):
    result = ""
    i = 0
    while i < len(ststring) - 1:
        temp = ststring[i] + ststring[i + 1]
        if twoword_dict[temp] > 10:  # 该“二字词”出现大于10次
            result = result + str(2)
            i += 2  # 有“二字词”被标记为2之后，向后推进两格
        else:
            result = result + str(1)
            i += 1  # “一字词”
    if i <= len(ststring) - 1:  # 当倒数第二第三个字（二字词）被标记为2
        result = result + str(1)
    return result


def get_new_ci(new_cipai):
    new_ci = []
    for scc in same_cipai_ci:
        if scc.cipai[0] == new_cipai:  # scc.cipai中只有一个词牌名
            for dj_line in scc.duanju_final:
                new_ci_line = ""
                for djl in dj_line:
                    if djl == '1':
                        new_ci_line += oneword_list[random.randint(0, len(oneword_list))]  # oneword_list中的任意一个词
                    else:
                        new_ci_line += twoword_list_final[random.randint(0, len(twoword_list_final))]
                new_ci.append(new_ci_line)
    return new_ci


def get_duanju():
    i = 0
    while i < len(sentences):
        if sentences[i] != []:
            ci_set.append(ci_class(sentences[i], sentences[i + 2]))  # 词牌 与 词文之间隔着一个空字符
            i += 2  # 词文与下面的词牌隔 两个空字符
        i += 1
    # print(ci_set[1].ciwen)
    # ['长忆钱塘', '临水傍山三百寺', '僧房携杖遍曾游', '闲话觉忘忧', '栴檀楼阁云霞畔', '钟梵清宵彻天汉', '别来遥礼只焚香', '便恐是西方']

    # 给ci.set中添加元素：duanju_ci 标签
    for i in range(0, len(ci_set)):
        duanju_ci = []
        for sts in ci_set[i].ciwen:
            duanju_ci.append(duanju(sts))
        ci_set[i].duanju_ci = duanju_ci

    for songci in ci_set:
        if_insert = False
        for i in range(0, len(same_cipai_ci)):
            if same_cipai_ci[i].cipai == songci.cipai:
                same_cipai_ci[i].duanju_list.append(songci.duanju_ci)
                if_insert = True
                break
        if if_insert == False:
            same_cipai_ci.append(cipai_class(songci.cipai, songci.duanju_ci))

    for i in range(0, len(same_cipai_ci)):
        duanju_final = []
        j = 0
        while j < 50:
            temp_list = []
            shaixuan = True  # 筛选
            for k in range(0, len(same_cipai_ci[i].duanju_list)):
                if j < len(same_cipai_ci[i].duanju_list[k]):  # 前提是第k首词含有第j个字段
                    temp_list.append(same_cipai_ci[i].duanju_list[k][j])  # 相同词牌下每首（由k循环每首词）词的第j个位置的标签（字段）

            # temp_list不一定有同一词牌下所有词的第j个字段
            if ((len(temp_list) * 2 < len(same_cipai_ci[i].duanju_list))) | (len(temp_list) == 0):
                j = 999
                shaixuan = False  # 不筛选
            if shaixuan:
                j += 1
                # 统计temp_list中的元素个数；存到temp_dict |  举例：temp_dict={'22': 13, '211': 3, '121': 1, '112': 2, '1111': 1}
                temp_dict = {}
                for temp_li in temp_list:
                    if temp_li in temp_dict:
                        temp_dict[temp_li] += 1
                    else:
                        temp_dict[temp_li] = 1
                # 以value对temp_dict排序；
                # 相同词牌下的词中出现第j个位置：出现最多的字段排在 sorted_temp_dict_list 的最前面
                sorted_temp_dict_list = sorted(temp_dict.items(), key=lambda d: d[1], reverse=True)
                duanju_final.append(sorted_temp_dict_list[0][0])  # 将 （某个词牌下的） 词中所有（j位置循环）位置 出现次数最多的字段存入 duanju_final
        same_cipai_ci[i].duanju_final = duanju_final  # 将 （所有词牌下的） 词中所有（j位置循环）位置 出现次数最多的字段存入 duanju_final


# 初始准备工作
# @st.cache
def main_proc():
    with open('Ci.txt', errors='ignore') as ci:
        lines = ci.readlines()
    del_writer_num = 0  # 统计诗人数目
    for i in range(2, len(lines) - 3):
        temp_num = i - del_writer_num  # lines的行数实时变化（因为同时删除了诗人名字所在的行）
        if (lines[temp_num] != '\n') & (lines[temp_num + 1] == '\n') & (lines[temp_num + 2] == '\n') & (
                lines[temp_num - 1] == '\n') & (lines[temp_num - 2] == '\n'):
            del_lines.append(lines[temp_num])
            lines.remove(lines[temp_num])  # 删除诗人名字所在的行
            del_writer_num += 1  # 统计诗人数目

    fenci(lines)

    get_duanju()

    # 统计“二字词”出现最多的（按照出现次数排序）；
    # 实质上类似于：将twoword_list中出现次数大于10的挑选出来，按出现次数排序，存入twoword_list_final（列表）中
    for k in sorted_twoword_dict:
        if twoword_dict[k] > 10:
            twoword_list_final.append(k)
        else:
            break

    for scc in same_cipai_ci:
        cipai_set.append(scc.cipai[0])  # cipai_set含有所有词牌的列表


if __name__ == "__main__":
    main_proc()
    # print(list(same_cipai_ci))
    # print(oneword_list)
    ## same_cipai_ci不是列表

    # [<__main__.cipai_class object at 0x0000020AA179CD30>,

    with open("data.pickle", "wb")as f: # 通过with open()的时候可以自动关闭
        pickle.dump(same_cipai_ci, f)
        pickle.dump(oneword_list, f)
        pickle.dump(twoword_list_final, f)
    # st.title('自然语言实验：自动生成古诗词')
    # # st.text_input(label="输入词牌名")
    # ci_title = st.text_input('请输入词牌名', '浣溪沙')
    # result = get_new_ci(ci_title)
    # # st.write('生成的古诗是：', title)
    # # if st.button('生成'):
    # st.write('生成的古诗是：', result)

# -----------------------------------------------------------------------------------------
# root = Tk()
# root.title("自然语言实验")  # 设置窗口标题
# root.geometry("300x400")  # 设置窗口大小
# root.resizable(width=True, height=True)  # 设置窗口是否可以变化长宽，False不可变，True可变
# root.tk.eval('package require Tix')  # 引入升级包，使用升级的组合控件
#
# label = Label(root, text="实验二", bg="pink", bd=5, font=("Arial", 20), width=10, height=1)
# label.pack(side=TOP)
#
# label_cipai = Label(root, text="词牌名", bg='green')
# label_cipai.pack()
#
# entey = Entry(root, text='0', width=20, bd=5)
# entey.pack()
#
#
# # 输入词牌名之后的输出
# def PRINT():
#     a = get_new_ci(entey.get())  # 手动输入的词牌
#     text_insert_cipaiming.insert(END, entey.get() + '\n')
#     for i in a:
#         text_insert_cipaiming.insert(END, i + '\n')
#     text_insert_cipaiming.insert(END, '\n')
#
#
# button = Button(root, text='运行', command=PRINT, activeforeground='black', activebackground='blue', bg='orange',
#                 fg='white', width=12)
# button.pack()
#
# frame_thanks = Frame(root)
# frame_thanks.pack()
# group = LabelFrame(frame_thanks, text=' ', padx=10, pady=10)
# group.grid()
# frame_teacher = Label(group, text=' ')
# frame_thanks.pack(side=BOTTOM)
# frame_teacher.pack()
#
# text_insert_cipaiming = Text(root)
# text_insert_cipaiming.pack()
#
# root.mainloop()
