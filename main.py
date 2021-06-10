#$pip install pandas 
#$pip install numpy
#$pip install streamlit
#%windir%\System32\cmd.exe "/K" C:\Users\yoshi\.julia\conda\3\Scripts\activate.bat C:\Users\yoshi\.julia\conda\3
#%windir%\System32\cmd.exe "/K" C:\Users\yoshi\anaconda3\Scripts\activate.bat C:\Users\yoshi\anaconda3

from altair.vegalite.v4.api import condition
import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
import time

st.title('Stremalit 超入門')

st.write('プログレスバーの表示')
'Start!!'

latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_iteration.text(f'Iteration {i+1}')#テキストを表示している。
    bar.progress(i + 1)#バーが増える
    time.sleep(0.1)

'Done!!!!!'

#st.write('DataFrame')

#df = pd.DataFrame({
#    '1列目': [1, 2, 3, 4],
#    '2列目': [10, 20, 30, 40]
#})

#st.write(df)

#st.dataframe(df)
#こちらは指定できる引数がある。

#st.dataframe(df, width=100, height=100)#これで100*100の表になる,writeはそのような機能はない

#st.dataframe(df.style.highlight_max(axis=0))#これで最大値に色が付けてくれる。

#st.table(df.style.highlight_max(axis=0))#静的なテーブルを作成する時はtableを使う。

#マジックコマンド
#"""
## 章
### 節
#### 項

#```python
#import streamlit as st
#import numpy as np
#import pandas as pd
#```

#"""

#df = pd.DataFrame(
#    np.random.rand(20,3),
#    columns=['a','b','c']
#)
#st.line_chart(df)
#st.bar_chart(df)
#st.earia_chart(df)

#df = pd.DataFrame(
#    np.random.rand(100, 2)/[50, 50] + [35.69, 139.70], 
#    columns=['lat','lon']#これは緯度と経度を表している。
#)
#st.map(df)

#st.write('Display Image')

# if st.checkbox('Show Image'):#チェックボックス
#   img = Image.open('\\Users\\yoshi\\Desktop\\Streamlit\\sample.jpg')#絶対参照じゃないとまずいっぽい
#   st.image(img, caption='スクリーンショット', use_column_width=True) '''

# option =  st.selectbox(#動的に変えることができるセレクトボックス
#     'あなたが好きな数字を教えてください、',
#     list(range(1,11))
# )
# 'あなたが好きな数字は、', option ,'です。'
# st.write('Interactive Widgets')

# left_column, right_column = st.beta_columns(2)
# button = left_column.button('右カラムに文字を表示')
# if button:
#     right_column.write('ここに右カラム')

# expander1 = st.beta_expander('問い合わせ1')
# expander1.write('問い合わせ1内容を書く')
# expander2 = st.beta_expander('問い合わせ2')
# expander2.write('問い合わせ2内容を書く')
# expander3 = st.beta_expander('問い合わせ2')
# expander3.write('問い合わせ2内容を書く')

# text = st.text_input('あなたの趣味を教えてください。')
# 'あなたの趣味：', text ,'です。'

# condition =  st.slider('あなたの今の調子は？', 0, 100, 50)
# 'コンディション：', condition

# sidebar