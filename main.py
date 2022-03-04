# -*- coding: utf-8 -*-
"""
Created on Wed Mar  2 14:23:15 2022

@author: syaka
"""

import streamlit as st
import time
from PIL import Image
import random as rd
no = list(range(1,343,1))
正解 = 1
old = rd.choice(no)
no.remove(old)





new = rd.choice(no)
no.remove(new)
st.title("いいじまくんのきゅう＆ニュー")
"新しいと思う画像を選んでください"

oimg = Image.open(f"./img/jima ({old}).jpg")
nimg = Image.open(f"./img/jima ({new}).jpg")
col1, col2 = st.columns(2)
with col1:    
    st.header("左")
    st.image(nimg,use_column_width=True)
with col2:
    st.header("右")
    st.image(oimg,use_column_width=True)



st.button("リロード")

判定 = new >= old




latest_iteration = st.empty()
bar = st.progress(0) 

for i in range(100):
    latest_iteration.text(round(i/20))
    bar.progress(i + 1)
    time.sleep(0.05)

'タイムアップ!!!'
if new >= old:
    st.title("左が新しい！")
    st.write(f"※左は{new}作目、右は{old}作目") 
else :
    st.title("右が新しい！")   
    st.write(f"※左は{new}作目、右は{old}作目") 
    
 