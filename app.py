

# STREAMLIT套件
import streamlit as st
# 可以互動的PLOT套件
import plotly.graph_objects as go
# 設置日期格式的套件
import datetime
from datetime import datetime as dt
from datetime import timedelta 
import tejapi

# 登入TEJ API
tejapi.ApiConfig.api_key = "BZiY7cmWfPf5hyMJ8gSlvKUEzXIZ0n"
#把時間取消保留日期 (無視)
tejapi.ApiConfig.ignoretz = True

st.set_page_config(page_title='量化投資', page_icon=':bar_chart:', layout='wide')

with st.sidebar:
    
    st.title('TEJAPI股票學習')
    col1, col2 = st.columns(2)
    with col1:
        # 將股票起使日期設置為變數d1
        d1 = st.date_input(
        "股票起始日期",
        # 並將預設資料設定為2022年的1/1
        datetime.date(2022, 1, 1))
        
    with col2:
        # 將股票起使日期設置為變數d2
        d2= st.date_input(
        "股票結束日期",
        datetime.date(2023, 2, 3))
        
      
