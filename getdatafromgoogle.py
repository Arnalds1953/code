import streamlit as st
import gspread
from google.oauth2 import service_account
import pandas as pd
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

# 测试加载谷歌表格
scope = [
    'https://www.googleapis.com/auth/spreadsheets',
    'https://www.googleapis.com/auth/drive'
]

credentials = service_account.Credentials.from_service_account_info(
                st.secrets["database"], scopes = scope)

gc = gspread.authorize(credentials)
sh = gc.open_by_url(st.secrets["gsheets"])
worksheet = sh.sheet1
df = pd.DataFrame(worksheet.get_all_records())

st.write(df)