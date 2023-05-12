import streamlit as st
# from tempsave import cipai_class
import pickle
import random
st.set_page_config(
    page_title="武梓龙 2019212300",
    page_icon=":shark:",
    menu_items={
        'Get Help': 'https://www.xinyang666.xyz/170-2',
        'Report a bug': "https://www.xinyang666.xyz/170-2",
        'About': "## 作者：武梓龙 2019212300"
    }
)


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


# print(get_new_ci("酒泉子"))
if __name__ == "__main__":
    st.title('实验二：1.自动生成宋词')
    st.write("作者:武梓龙 2019212300")
    ci_title = st.text_input('请输入词牌名', '浣溪沙')
    result = get_new_ci(ci_title)
    if st.button('生成'):
        st.write('生成的古诗是：', result)
    # else:
    #     st.error('您输入的不是词牌名！')

    st.markdown('例如你可以输入：酒泉子 菩萨蛮 望海潮 破阵乐 浪淘沙 卜算子 西江月 定风波 渔家傲 苏幕遮 等等')
