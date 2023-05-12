import pickle
import numpy as np
import streamlit as st

st.set_page_config(
    page_title="武梓龙 2019212300",
    page_icon=":shark:",
    menu_items={
        'Get Help': 'https://www.xinyang666.xyz/170-2',
        'Report a bug': "https://www.xinyang666.xyz/170-2",
        'About': "## 作者：武梓龙 2019212300"
    }
)

f = open("SentenceData.pickle", "rb")
dic_2g = pickle.load(f)
f.close()


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


if __name__ == "__main__":

    st.title('实验二：2.自动生成文本内容')
    st.write("作者:武梓龙 2019212300")
    name = st.text_input('请输入首词', '我')
    num = st.text_input('请输入词数', '10')
    sentence = makesen(name, int(num))

    if st.button('生成'):
        st.write('生成的文本内容是：', sentence)
    # else:
    #     st.error('您输入有误！')
