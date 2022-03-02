# -*- coding: utf-8 -*-
"""
Created on Wed Mar  2 14:23:15 2022

@author: syaka
"""

import streamlit as st
import numpy as np
import pandas as pd
import time
from PIL import Image


st.title("streamlit 超入門")

st.write('データフレーム')

df = pd.DataFrame({
    '一列目': [ 1, 2, 3, 4],
    '二列目': [ 10, 2, 3, 4]
    })

st.write(df)

st.dataframe(df.style.highlight_max(axis=0))

st.table(df)


    
"""

# 章
## 節
### 項

```python
import streamlit as st
import numpy as np
import pandas as pd

```


"""

df2 = pd.DataFrame(
    np.random.rand(20,3),
    columns=['a','B','c']
    )

st.line_chart(df2)
st.area_chart(df2)
st.bar_chart(df2)


df3 = pd.DataFrame(
    np.random.rand(100,2)/[50,50]+[35.69,139.70],
    columns=['lat','lon']
    )

st.map(df3)

if st.checkbox('Show Image'):  
    img = Image.open('sample.png')
    st.image(img, caption='sakaeda', use_column_width=True)

option = st.selectbox(
    'あなたが好きな数字を教えてください',
    list(range(1, 11))
)

'あなたの好きな数字は',option,'です！'

option2 = st.text_input('あなたの趣味を教えてください。')
'あなたの好きな趣味は',option2,'です！'

option3 = st.slider('あなたの今の調子は',0,100,50)

'コンディション：',option3

left_column, right_column = st.columns(2)
button = left_column.button('右カラムに文字を表示')
if button:
    right_column.write('ここは右カラム')

expander = st.expander('問い合わせ')
expander.write("問い合わせを描く")

latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_iteration.text(f'Iteration{i+1}')
    bar.progress(i + 1)
    time.sleep(0.3)

'deone!!!'