import numpy as np
import pickle
dic_1g = {}
dic_2g = {}
dic_granm = {}
dic_sum = {}


def loading():
    filename = 'fenci.txt'
    fn = open(filename, 'r', encoding='UTF-8')
    for line in fn.readlines():
        data = ''
        data1 = ''
        data2 = ''
        flag = 1
        sum_part = 0
        if line[0] == '1':
            for word in line[2:]:  # 下标为2的  -> 一直到最后一个
                if word == ' ':
                    flag = 0
                elif flag == 1:
                    data += word
                elif flag == 0 and word != '\n':
                    sum_part *= 10
                    sum_part += int(word)
            dic_1g[data] = sum_part

        elif line[0] == '2':
            for word in line[2:]:
                if word == ' ' and flag == 1:
                    flag = 0
                elif word == ' ' and flag == 0:
                    flag = -1
                elif flag == 1:
                    data1 += word
                elif flag == 0:
                    data2 += word
                elif flag == -1 and word != '\n':
                    sum_part *= 10
                    sum_part += int(word)
            if data1 not in dic_2g:
                dic_2g[data1] = {data2: sum_part}
                dic_sum[data1] = sum_part
            else:
                dic_2g[data1][data2] = sum_part
                dic_sum[data1] += sum_part

    for key in dic_2g:
        for little in dic_2g[key]:
            dic_2g[key][little] /= dic_sum[key]


#    print(dic_2g)
def makesen(first, num):
    sentence = ''
    if first == '':  # <BOS> 标识符，使first == ''的时候可以进去下一个if判断
        first = '<BOS>'
    if first != '':
        sentence = first
        if first == '<BOS>':
            sentence = ''  # 置空
        for i in range(num):
            prolist = []
            gramlist = []
            if first not in dic_2g:  # 注： <BOS>在dic_2g中
                sentence += '，'
                first = '<BOS>'
                continue
            for key in dic_2g[first]:  # 循环了21987次
                prolist.append(dic_2g[first][key])
            #            print(prolist)
            for key in dic_2g[first].keys():  # 字典 keys() 方法返回一个视图对象  dict_keys(['', '', '', ''])
                gramlist.append(key)
            #            print(gramlist)
            # 在gramlist列表中，以概率prolist取值
            next = np.random.choice(gramlist, 1, True, np.array(prolist))  # 返回列表
            #            if first == '江':
            #                print(np.random.choice(gramlist,10,True,np.array(prolist)))
            #            print(next[0])
            sentence += next[0]  #
            #            print(1)
            first = next[0]  # 不断更新first
    return sentence + '。'


#  # 生成SentenceData.pickle
# loading()
# with open("SentenceData.pickle", "wb")as f:  # 通过with open()的时候可以自动关闭
#     pickle.dump(dic_2g, f)
#

# print(makesen('', 20))
# # print(np.random.choice(['a','n','c','s'],10,True,np.array([0.7,0.2,0.02,0.08])))
