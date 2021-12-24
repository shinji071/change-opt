import streamlit as st
import pandas as pd
from sklearn import datasets

@st.cache
def load_data():
    iris = datasets.load_iris()
    df = pd.DataFrame(iris.data, columns=iris.feature_names)
    df['target'] = iris.target_names[iris.target]
    return df

def opt():


st.title('人生アルゴリズム')
st.header('財布の小銭最小化問題')
st.subheader('財布が軽くなるほど、心が満たされる。　　--ヴィクトル・ユーゴー')
st.write('今回は支払い後の財布の中身の紙幣・硬貨枚数が最小になるアルゴリズムを考えてみました') # markdown

st.sidebar.write('財布の中身(自由に設定してみてください）')

yen10000 = st.sidebar.slider('10000円札', 0, 10, 5, 1)
yen5000 = st.sidebar.slider('5000円札', 0, 10, 5, 1)
yen1000 = st.sidebar.slider('1000円札', 0, 10, 5, 1)
yen500 = st.sidebar.slider('500円玉', 0, 10, 5, 1)
yen100 = st.sidebar.slider('100円玉', 0, 10, 5, 1)
yen50 = st.sidebar.slider('50円玉', 0, 10, 5, 1)
yen10 = st.sidebar.slider('10円玉', 0, 10, 5, 1)
yen5 = st.sidebar.slider('5円玉', 0, 10, 5, 1)
yen1 = st.sidebar.slider('1円玉', 0, 10, 5, 1)

st.write('財布の中身合計：', yen10000*10000+yen5000*5000+yen1000*1000+yen500*500+yen100*100+yen50*50+yen10*10+yen5*5+yen1*1)
st.number_input('請求金額 : ', 1, 100000, 1200)

button_state = st.button('Say hello')
if button_state:
    st.write('Why hello there')
else:
    st.write('Goodbye')

