import re

oneword_dict = {}
twoword_dict = {}
oneword_list = []
twoword_list = []
sentences = []
sorted_oneword_dict = {}
sorted_twoword_dict = {}


def get_words(word_num, short_sentence):
    result = []
    if word_num == 1:
        for oneword in short_sentence:
            result.append(oneword)
    elif word_num == 2:
        for i in range(0, len(short_sentence) - 1):
            twoword = short_sentence[i] + short_sentence[i + 1]
            result.append(twoword)
    return result


def is_chinese(uchar):
    if uchar >= u'\u4e00' and uchar <= u'\u9fa5':
        return True
    else:
        return False


def fenci(lines):
    for i in range(0, len(lines)):
        lines[i] = lines[i].rstrip('\n')

    for line in lines:
        sts = re.split("，|。|？|！|、| ", line)
        while '' in sts:
            sts.remove('')
        sentences.append(sts)

    for i in range(0, len(sentences)):
        for j in range(0, len(sentences[i])):
            for ch in sentences[i][j]:
                if is_chinese(ch) == False:
                    sentences[i][j] = sentences[i][j].replace(ch, '')

    global oneword_list, twoword_list

    for sentence in sentences:
        for sts in sentence:
            oneword_list += get_words(1, sts)
            twoword_list += get_words(2, sts)

    for oneword in oneword_list:
        if oneword in oneword_dict:
            oneword_dict[oneword] += 1
        else:
            oneword_dict[oneword] = 1

    for twoword in twoword_list:
        if twoword in twoword_dict:
            twoword_dict[twoword] += 1
        else:
            twoword_dict[twoword] = 1

    sorted_oneword_list = sorted(oneword_dict.items(), key=lambda d: d[1], reverse=True)
    sorted_twoword_list = sorted(twoword_dict.items(), key=lambda d: d[1], reverse=True)

    for e in sorted_oneword_list:
        sorted_oneword_dict[e[0]] = e[1]
    for e in sorted_twoword_list:
        sorted_twoword_dict[e[0]] = e[1]


if __name__ == "__main__":
    with open('../Ci.txt', errors='ignore') as ci:
        lines = ci.readlines()
    fenci(lines)
    with open('C:\\Users\\Lenovo\\Desktop\\自然语言实验\\exp1\\danci.txt', 'w') as cp:
        for oneword in sorted_oneword_dict:
            cp.write(oneword + " " + str(sorted_oneword_dict[oneword]) + '\n')
    with open('C:\\Users\\Lenovo\\Desktop\\自然语言实验\\exp1\\shuangci.txt', 'w') as cp:
        for twoword in sorted_twoword_dict:
            cp.write(twoword + " " + str(sorted_twoword_dict[twoword]) + '\n')
