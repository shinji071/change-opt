import streamlit as st
import pandas as pd
from sklearn import datasets

@st.cache
def load_data():
    iris = datasets.load_iris()
    df = pd.DataFrame(iris.data, columns=iris.feature_names)
    df['target'] = iris.target_names[iris.target]
    return df

st.title('人生アルゴリズム')
st.header('財布の小銭最小化問題')
st.subheader('財布が軽くなるほど、心が満たされる。　　--ヴィクトル・ユーゴー')
st.write('今回は支払い後の財布の中身の紙幣・硬貨枚数が最小になるアルゴリズムを考えてみました') # markdown

st.slider('10000円札', 0, 10, 5, 1)
st.slider('ラベル', 0, 10, 5, 1)
st.slider('ラベル', 0, 10, 5, 1)
st.slider('ラベル', 0, 10, 5, 1)
st.slider('ラベル', 0, 10, 5, 1)
st.slider('ラベル', 0, 10, 5, 1)
st.slider('ラベル', 0, 10, 5, 1)