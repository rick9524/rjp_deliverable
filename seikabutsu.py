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
mani = pd.read_csv('data_csv/思い出のマーニー.csv',parse_dates=["時間"])
lovesong = pd.read_csv('data_csv/天使にラブ・ソングを.csv',parse_dates=["時間"])
pirates_1 = pd.read_csv('data_csv/パイレーツオブカリビアン_呪われた海賊たち.csv',parse_dates=["時間"])
pirates_2 = pd.read_csv('data_csv/パイレーツオブカリビアン_デッドマンズチェスト.csv',parse_dates=["時間"])

st.title('映画を観た感情の起伏')

img = Image.open('スプラトゥーン3.jpg')
if st.checkbox('check'):
    st.image(img,caption='スプラトゥーン',use_column_width=True)

left_column,right_column = st.columns(2)
left_column.image(img,caption='スプラトゥーン',use_column_width=True)
right_column.image(img,caption='スプラトゥーン',use_column_width=True)

expander = st.expander('連投')
expander.image(img,caption='スプラトゥーン',use_column_width=True)
expander.image(img,caption='スプラトゥーン',use_column_width=True)
expander.image(img,caption='スプラトゥーン',use_column_width=True)
expander.image(img,caption='スプラトゥーン',use_column_width=True)
