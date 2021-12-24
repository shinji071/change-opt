import streamlit as st
import pandas as pd
import pulp
import numpy as np
from sklearn import datasets
import random

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

st.sidebar.write('財布の中身(自由に設定してみてください）')

yen10000 = st.sidebar.slider('10000円札', 0, 10, 1, 1)
yen5000 = st.sidebar.slider('5000円札', 0, 10, 1, 1)
yen2000 = st.sidebar.slider('2000円札', 0, 10, 1, 1)
yen1000 = st.sidebar.slider('1000円札', 0, 10, 1, 1)
yen500 = st.sidebar.slider('500円玉', 0, 10, 0, 1)
yen100 = st.sidebar.slider('100円玉', 0, 10, 4, 1)
yen50 = st.sidebar.slider('50円玉', 0, 10, 0, 1)
yen10 = st.sidebar.slider('10円玉', 0, 10, 4, 1)
yen5 = st.sidebar.slider('5円玉', 0, 10, 1, 1)
yen1 = st.sidebar.slider('1円玉', 0, 10, 3, 1)

st.write('財布の中身合計：', yen10000*10000+yen5000*5000+yen2000*2000+yen1000*1000+yen500*500+yen100*100+yen50*50+yen10*10+yen5*5+yen1*1)
input_price = st.number_input('請求金額 : ', 1, 100000, 1200)

opt_payment = -1
st.write("最適な支払い金額 = ", opt_payment)
#st.button('最適計算')

if st.button("最適計算"):
    money_type = (10000, 5000, 2000, 1000, 500, 100, 50, 10, 5, 1)
    price = input_price
    purse = [yen10000, yen5000, yen2000, yen1000, yen500, yen100, yen50, yen10, yen5, yen1]

    problem = pulp.LpProblem('Change Minimization', pulp.LpMinimize)
    pay_var = np.array(
        [pulp.LpVariable('pay_var_' + str(i), 0, purse[k] + 1, 'Integer') for k, i in enumerate(money_type)])
    change_var = np.array(
        [pulp.LpVariable('change_var_' + str(i), 0, purse[k] + 1, 'Integer') for k, i in enumerate(money_type)])
    problem += pulp.lpSum(purse - pay_var + change_var) + pulp.lpSum(pay_var) * 0.01

    problem += pulp.lpDot(money_type, pay_var) - price >= 0
    problem += pulp.lpDot(money_type, change_var) == pulp.lpDot(money_type, pay_var) - price
    for i, v in enumerate(purse):
        problem += pay_var[i] - purse[i] <= 0
    status = problem.solve()

    if status == 1:
        pay_var2 = [a.value() for a in pay_var]
        st.write("最適な支払金額 = ", pulp.lpDot(money_type, pay_var2))
        for i, v in enumerate(pay_var):
            if pay_var[i].value() >= 1:
                st.write("{}円　{}枚".format(money_type[i], pay_var[i].value()))
        st.write("お釣り詳細：")
        for i, v in enumerate(change_var):
            if change_var[i].value() >= 1:
                st.write("{}円　{}枚".format(money_type[i], change_var[i].value()))
    else:
        st.write("最適解なし（そもそも財布の中身が足りないなど）")