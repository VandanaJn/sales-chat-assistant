import streamlit as st
import pandas as pd
import re
from sales_queries import get_total_sales, get_monthly_sales, get_large_deals

# 🎨 Title and input
st.title("Sales Data Assistant")
user_input = st.text_input("Ask a question about your sales data:")

# 📦 Load dataset
df = pd.read_csv(
    "https://raw.githubusercontent.com/AllThingsDataWithAngelina/DataSource/main/sales_data_sample.csv",
    encoding="latin1"
)

# 🧠 Query map
query_map = {
    "total sales": get_total_sales,
    "monthly sales": get_monthly_sales,
    "large deals": lambda df: get_large_deals(df, threshold=5000)
}

# 🔍 Entity extractor
def extract_product_line(query):
    query = query.lower()
    best_match = None
    for line in df["PRODUCTLINE"].unique():
        if line.lower() in query or query in line.lower():
            best_match = line
            break
    return best_match

# from difflib import get_close_matches

# def extract_product_line_fuzzy(query):
#     matches = get_close_matches(query.lower(), [line.lower() for line in df["PRODUCTLINE"].unique()], n=1, cutoff=0.6)
#     if matches:
#         return next((line for line in df["PRODUCTLINE"].unique() if line.lower() == matches[0]), None)
#     return None



# 🤖 Query handler
def handle_query(user_input, df):
    for key, func in query_map.items():
        if key in user_input.lower():
            pline = extract_product_line(user_input)
            # pline = extract_product_line_fuzzy(user_input)
            if key == "total sales" and pline:
                return func(df, product_line=pline)
            return func(df)
    return "Sorry, I couldn't interpret that. Try asking about total sales, monthly sales, or large deals."

# 🚀 Process query
if user_input:
    st.write("Detected product line:", extract_product_line(user_input))
    # st.write("Detected product line fuzzy:", extract_product_line_fuzzy(user_input))
    result = handle_query(user_input, df)
    st.write(result)