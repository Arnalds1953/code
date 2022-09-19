import code
import encodings
import streamlit as st
import pandas as pd
import openpyxl

uploaded_file = st.file_uploader("Choose a file")
if uploaded_file is not None:
    # Can be used wherever a "file-like" object is accepted:
    df0 = pd.read_csv(uploaded_file)
    st.write(df0)


# Path0 = 'D:/测试文件夹/01.原始数据/03.销售/WAYFAIR+Kadehome Inc+2022.7-8月原始数据+Tom.csv'
Path1 = 'D:/测试文件夹/03.模板/WAYFAIR销售数据汇总模板.xlsx' 
Path2 = 'D:/测试文件夹/01.原始数据/04.商品总表/Kadehome商品总表.xlsx'
# Path3 = 'D:/测试文件夹/02.输出结果/20220919.xlsx'


# df0 = pd.read_csv(Path0)
df1 = pd.read_excel(Path1, encoding='utf-8')
df2 = pd.read_excel(Path2, encoding='utf-8')

df4 = df0.merge(df2, on='Item Number', how='left')

df1[['P.O. Number:','PO Date','订单状态','Quantity','Wholesale Price','目的地所属州','Item Name','平台货号']] = df4[['PO Number','PO Date','Order Status','Quantity','Wholesale Price','Ship To State','Item Name','Item Number']]
df1[['供应商名称','供应商货号','唯非货号','DDP美金单价','下单给供应商所用SKU']] = df4[['供应商编码','供应商SKU','唯非SKU','8月DDP美金','下单SKU']]




st.download_button(
    label="Download data",
    data = df1.to_csv().encode('utf-8'),
    file_name='large_df.csv',
)

