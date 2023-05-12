import re
from tkinter import *
from tkinter.tix import Tk, Control, ComboBox
from tkinter.messagebox import showinfo, showwarning, showerror
import pickle

f = open("exp3Data.pickle", "rb")
danci_dict = pickle.load(f)
shuangci_dict = pickle.load(f)
sanci_dict = pickle.load(f)
sici_dict = pickle.load(f)
wuci_dict = pickle.load(f)
f.close()


def is_chinese(uchar):
    if uchar >= u'\u00a4' and uchar <= u'\uffe5':
        return True
    else:
        return False


def FMM(ststring):
    result = []
    i = 0
    while i < len(ststring):
        n = len(ststring) - i
        if n >= 5:
            temp5 = ststring[i:i + 5]
            temp4 = ststring[i:i + 4]
            temp3 = ststring[i:i + 3]
            temp2 = ststring[i:i + 2]
            temp1 = ststring[i]

            if temp5 in wuci_dict:
                result.append(temp5)
                i += 5
            elif temp4 in sici_dict:
                result.append(temp4)
                i += 4
            elif temp3 in sanci_dict:
                result.append(temp3)
                i += 3
            elif temp2 in shuangci_dict:
                result.append(temp2)
                i += 2
            else:
                result.append(temp1)
                i += 1

        elif n == 4:
            temp4 = ststring[i:i + 4]
            temp3 = ststring[i:i + 3]
            temp2 = ststring[i:i + 2]
            temp1 = ststring[i]

            if temp4 in sici_dict:
                result.append(temp4)
                i += 4
            elif temp3 in sanci_dict:
                result.append(temp3)
                i += 3
            elif temp2 in shuangci_dict:
                result.append(temp2)
                i += 2
            else:
                result.append(temp1)
                i += 1

        elif n == 3:
            temp3 = ststring[i:i + 3]
            temp2 = ststring[i:i + 2]
            temp1 = ststring[i]

            if temp3 in sanci_dict:
                result.append(temp3)
                i += 3
            elif temp2 in shuangci_dict:
                result.append(temp2)
                i += 2
            else:
                result.append(temp1)
                i += 1

        elif n == 2:
            temp2 = ststring[i:i + 2]
            temp1 = ststring[i]

            if temp2 in shuangci_dict:
                result.append(temp2)
                i += 2
            else:
                result.append(temp1)
                i += 1

        elif n == 1:
            temp1 = ststring[i]

            result.append(temp1)
            i += 1
    return result


def BMM(ststring):
    result = []
    i = len(ststring)
    while i > 0:
        n = i
        if n >= 5:
            temp5 = ststring[i - 5:i]
            temp4 = ststring[i - 4:i]
            temp3 = ststring[i - 3:i]
            temp2 = ststring[i - 2:i]
            temp1 = ststring[i - 1]

            if temp5 in wuci_dict:
                result.append(temp5)
                i -= 5
            elif temp4 in sici_dict:
                result.append(temp4)
                i -= 4
            elif temp3 in sanci_dict:
                result.append(temp3)
                i -= 3
            elif temp2 in shuangci_dict:
                result.append(temp2)
                i -= 2
            else:
                result.append(temp1)
                i -= 1

        elif n == 4:
            temp4 = ststring[i - 4:i]
            temp3 = ststring[i - 3:i]
            temp2 = ststring[i - 2:i]
            temp1 = ststring[i - 1]

            if temp4 in sici_dict:
                result.append(temp4)
                i -= 4
            elif temp3 in sanci_dict:
                result.append(temp3)
                i -= 3
            elif temp2 in shuangci_dict:
                result.append(temp2)
                i -= 2
            else:
                result.append(temp1)
                i -= 1

        elif n == 3:
            temp3 = ststring[i - 3:i]
            temp2 = ststring[i - 2:i]
            temp1 = ststring[i - 1]

            if temp3 in sanci_dict:
                result.append(temp3)
                i -= 3
            elif temp2 in shuangci_dict:
                result.append(temp2)
                i -= 2
            else:
                result.append(temp1)
                i -= 1

        elif n == 2:
            temp2 = ststring[i - 2:i]
            temp1 = ststring[i - 1]

            if temp2 in shuangci_dict:
                result.append(temp2)
                i -= 2
            else:
                result.append(temp1)
                i -= 1

        elif n == 1:
            temp1 = ststring[i - 1]

            result.append(temp1)
            i -= 1
    return list(reversed(result))


if __name__ == '__main__':
    root = Tk()
root.title("自然语言实验")  # 设置窗口标题
root.geometry("300x400")  # 设置窗口大小
root.resizable(width=True, height=True)  # 设置窗口是否可以变化长宽，False不可变，Ture可变
root.tk.eval('package require Tix')  # 引入升级包，使用升级的组合控件

# 初始化 生成 一字 二字 三字 四字...  的字典（带有词频）

label = Label(root, text="实验三", bg="pink", bd=5, font=("Arial", 20), width=10, height=1)
label.pack(side=TOP)

# 输入内容
label_cipai = Label(root, text="输入内容", bg='yellow')
label_cipai.pack()

entey = Entry(root, text='0', width=200, bd=5)
entey.pack()


# 输出
def PRINT():
    FMM_results = []
    BMM_results = []
    a = entey.get()
    FMM_results.append(FMM(a))
    BMM_results.append(BMM(a))
    for result in FMM_results:
        text_insert_cipaiming.insert(END, "FMM结果：")
        for word in result:
            text_insert_cipaiming.insert(END, word + ' \ ')
        text_insert_cipaiming.insert(END, '\n')

    for result in BMM_results:
        text_insert_cipaiming.insert(END, "BMM结果：")
        for word in result:
            text_insert_cipaiming.insert(END, word + ' \ ')
        text_insert_cipaiming.insert(END, '\n')


button = Button(root, text='运行', command=PRINT, activeforeground='black', activebackground='blue', bg='orange',
                fg='white', width=12)
button.pack()

frame_thanks = Frame(root)
frame_thanks.pack()
group = LabelFrame(frame_thanks, text='————————', padx=10, pady=10)
group.grid()
frame_teacher = Label(group, text='  ')
frame_thanks.pack(side=BOTTOM)
frame_teacher.pack()

text_insert_cipaiming = Text(root)
text_insert_cipaiming.pack()

root.mainloop()
