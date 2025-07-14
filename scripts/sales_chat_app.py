import streamlit as st
import pandas as pd
from sales_queries import get_total_sales, get_monthly_sales

st.title("Sales Data Assistant")

user_input = st.text_input("Ask a question about your sales data:")
df = pd.read_csv("https://raw.githubusercontent.com/AllThingsDataWithAngelina/DataSource/main/sales_data_sample.csv", encoding='latin1')
product = st.selectbox("Choose a product line:", df["PRODUCTLINE"].unique())
if st.button("Get Sales"):
    st.write(get_total_sales(df, product_line=product))

if "total sales" in user_input.lower():
    result = get_total_sales(df)
    st.write(f"Total sales: ${result}")

elif "monthly sales" in user_input.lower():
    st.write(get_monthly_sales(df))
