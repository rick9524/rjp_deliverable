import streamlit as st
import pandas as pd
import numpy as np
from scipy import stats
from scipy import integrate
import matplotlib.pyplot as plt
plt.rcParams['font.family'] = 'Meiryo'
import streamlit as st
from PIL import Image

anaban = pd.read_csv('data_csv/あなたの番です.csv',parse_dates=["時間"])
violet = pd.read_csv('data_csv/ヴァイオレットエヴァーガーデン.csv',parse_dates=["時間"])
baton = pd.read_csv('data_csv/そしてバトンは渡された.csv',parse_dates=["時間"])
hauru = pd.read_csv('data_csv/ハウルの動く城.csv',parse_dates=["時間"])
pirates = pd.read_csv('data_csv/パイレーツオブカリビアン_呪われた海賊たち.csv',parse_dates=["時間"])
mani = pd.read_csv('data_csv/思い出のマーニー.csv',parse_dates=["時間"])
lovesong = pd.read_csv('data_csv/天使にラブ・ソングを.csv',parse_dates=["時間"])

st.title('タイトル')
st.subheader('あらすじ')
st.write('いいいいいい')

img = Image.open('あなたの番です2.png',)
imgg = Image.open('あなたの番です.png',)

col1, col2 = st.columns(2)
with col1:
    st.header("図1:感情を-1~1で表したヒストグラム")
    st.image("あなたの番です2.png", use_column_width=True,width=10)

with col2:
    st.header("図2:感情を6段階に分割した積み上げ面プロット")
    st.image("あなたの番です.png", use_column_width=True,width=30)
    
st.subheader('グラフの解釈')
st.write('うううううう')

st.subheader('こんな方におすすめ')
st.write('うううううう')



st.write('・あああ　　・いいい　　・ううう')

