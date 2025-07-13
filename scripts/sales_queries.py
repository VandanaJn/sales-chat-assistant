import pandas as pd
from pandas import DataFrame
def get_total_sales(df:DataFrame, product_line:str=None ):
    if product_line:
        return df[df["PRODUCTLINE"]==product_line]["SALES"].sum()
    return df["SALES"].sum()

def get_sales_by_country(df:DataFrame, country:str):
    return df[df["COUNTRY"]==country]["SALES"].sum()

def get_monthly_sales(df:DataFrame):
    df["ORDERDATE"]=pd.to_datetime(df["ORDERDATE"])
    data= df.groupby(df["ORDERDATE"].dt.to_period("M"))["SALES"].sum()
    return data

def get_sales_for_customer(df, customer_name):
    return df[df["CUSTOMERNAME"].str.contains(customer_name, case=False)]["SALES"].sum()

def get_large_deals(df, threshold=10000):
    return df[df["SALES"] > threshold]