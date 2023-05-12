# -*- coding: utf-8 -*-
# @Time : 2021/10/26 16:55
# @Author : 信仰
# @File : show_tkinter.py
# @Software: PyCharm

from tkinter import *
from tkinter.tix import Tk, Control, ComboBox
from tkinter.messagebox import showinfo, showwarning, showerror
import pickle
import random


class cipai_class(object):  # dj就是ci_set中的 duanju_ci
    def __init__(self, cipai, dj):
        self.cipai = cipai
        self.duanju_list = []
        self.duanju_list.append(dj)


# # with open("data.pickle", "rb")as f:
f = open("data.pickle", "rb")
same_cipai_ci = pickle.load(f)
oneword_list = pickle.load(f)
twoword_list_final = pickle.load(f)
f.close()


# same_cipai_ci_file = open('same_cipai_ci.pickle', 'rb')
# oneword_list_file = open('oneword_list.pickle', 'rb')
# twoword_list_final_file = open('twoword_list_final.pickle', 'rb')
#
# same_cipai_ci = pickle.load(same_cipai_ci_file)
# oneword_list = pickle.load(oneword_list_file)
# twoword_list_final = pickle.load(twoword_list_final_file)

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


root = Tk()
root.title("自然语言实验")  # 设置窗口标题
root.geometry("300x400")  # 设置窗口大小
root.resizable(width=True, height=True)  # 设置窗口是否可以变化长宽，False不可变，True可变
root.tk.eval('package require Tix')  # 引入升级包，使用升级的组合控件

label = Label(root, text="实验二", bg="white", bd=5, font=("Arial", 20), width=10, height=1)
label.pack(side=TOP)

label_cipai = Label(root, text="词牌名", bg='yellow')
label_cipai.pack()

entey = Entry(root, text='0', width=20, bd=5)
entey.pack()


# 输入词牌名之后的输出
def PRINT():
    a = get_new_ci(entey.get())  # 手动输入的词牌
    text_insert_cipaiming.insert(END, entey.get() + '\n')
    for i in a:
        text_insert_cipaiming.insert(END, i + '\n')
    text_insert_cipaiming.insert(END, '\n')


button = Button(root, text='运行', command=PRINT, activeforeground='black', activebackground='blue', bg='orange',
                fg='white', width=12)
button.pack()

frame_thanks = Frame(root)
frame_thanks.pack()
group = LabelFrame(frame_thanks, text='武梓龙 2019212300', padx=10, pady=10)
group.grid()
# frame_teacher = Label(group, text=' ')
frame_thanks.pack(side=BOTTOM)
# frame_teacher.pack()

text_insert_cipaiming = Text(root)
text_insert_cipaiming.pack()

root.mainloop()
