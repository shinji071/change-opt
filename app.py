import streamlit as st
import pandas as pd
from sklearn import datasets

@st.cache
def load_data():
    iris = datasets.load_iris()
    df = pd.DataFrame(iris.data, columns=iris.feature_names)
    df['target'] = iris.target_names[iris.target]
    return df

st.title('日常を最適化♪')
st.header('財布の小銭最小化問題')
st.write('文字列') # markdown