# -*- coding: utf-8 -*-
# @Time : 2021/10/26 14:45
# @Author : 信仰
# @File : predictShowByStreamlit.py
# @Software: PyCharm
import joblib
import re
import jieba
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

token = "[0-9\s+\.\!\/_,$%^*()?;；：【】+\"\'\[\]\\]+|[+——！，;:。？《》、~@#￥%……&*（）“”.=-]+"


def preprocess(text):
    text1 = re.sub('&nbsp', ' ', text)
    str_no_punctuation = re.sub(token, ' ', text1)  # 去掉标点
    text_list = list(jieba.cut(str_no_punctuation))  # 分词列表
    text_list = [item for item in text_list if item != ' ']  # 去掉空格
    return ' '.join(text_list)


model = joblib.load("model.pkl")
# 进行模型的预测
# news_lastest = [
#     "360金融旗下产品有360借条、360小微贷、360分期。360借条是360金融的核心产品，是一款无抵押、纯线上消费信贷产品，为用户提供即时到账贷款服务（通俗可以理解为“现金贷”）用户借款主要用于消费支出。从收入构成来看，360金融主要有贷款便利服务费、贷后管理服务费、融资收入、其他服务收入等构成。财报披露，营收增长主要是由于贷款便利化服务费、贷款发放后服务费和其他与贷款发放量增加相关的服务费增加。",
#     "检方并未起诉全部涉嫌贿赂的家长，但起诉名单已有超过50人，耶鲁大学、斯坦福大学等录取率极低的名校涉案也让该事件受到了几乎全球的关注，该案甚至被称作美国“史上最大招生舞弊案”。",
#     "俄媒称，目前尚不清楚特朗普这一言论的指向性，因为近几日，伊朗官员们都在表达力图避免与美国发生军事冲突的意愿。5月19日早些时候，伊朗革命卫队司令侯赛因·萨拉米称，伊朗只想追求和平，但并不害怕与美国发生战争。萨拉米称，“我们（伊朗）和他们（美国）之间的区别在于，美国害怕发生战争，缺乏开战的意志。”"]
# X_new_data = [preprocess(doc) for doc in news_lastest]
# y_pred = model.predict(X_new_data)  # 加载出来的模型跟我们训练出来的模型一样，有相同的参数
# print(y_pred)

############################
st.title('新闻文本分类')
st.write("作者：武梓龙 2019212300")
st.write("（说明： 输出的英文分别所对应的类别为： _08_Finance 经济/_10_IT 信息技术/_13_Health 健康/_14_Sports 体育/_16_Travel 旅游/_20_Education 教育/_22_Recruit 招聘信息/_23_Culture 文化/_24_Military 军事）")
content = st.text_area('请输入一段新闻文本', '例如：10月17日至23日，中俄两国海军的10艘舰艇、6架舰载直升机组成联合编队，在日本海、西太平洋、东海海域成功组织实施了首次海上联合巡航。联合巡航期间，有外国舰艇和飞机对编队进行跟踪侦察和情报搜集。')
content_list = []
content_list.append(content)

X_new_data = [preprocess(doc) for doc in content_list]
y_pred = model.predict(X_new_data)
# st.write('生成的古诗是：', result)
if st.button('分类'):
    st.write('该新闻所属类别是：', y_pred)
# else:
#     st.error('您输入的有误！')

