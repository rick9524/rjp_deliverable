import streamlit as st
import pandas as pd
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt
plt.rcParams['font.family'] = 'meiryo'

if st.button('Say hello'):
    st.write('Why hello there')
else:
    st.write('Goodbye')