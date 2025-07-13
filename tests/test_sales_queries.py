import pytest
import pandas as pd
from scripts.sales_queries import get_total_sales, get_sales_by_country, get_monthly_sales
@pytest.fixture
def sales_df():
    return pd.read_csv("tests\sales.csv")
    
def test_get_total_Sales(sales_df):
    assert get_total_sales(sales_df)==11711.5

@pytest.mark.parametrize("line, sales",argvalues=[
    ("Classic Cars",5371),
    ("Motorcycles",2440.50),
    ])
def test_get_total_sales_product(line, sales, sales_df):
    assert get_total_sales(sales_df,product_line=line)==sales

@pytest.mark.parametrize("country, sales",argvalues=[
    ("USA",4371),
    ("Canada",2440.50),
    ])
def test_get_sales_by_country(country, sales, sales_df):
    assert get_sales_by_country(sales_df,country=country)==sales

def test_get_monthly_sales(sales_df):
    sales=get_monthly_sales(sales_df)
    assert sales.index[0]==pd.Period("2003-01", freq="M")
    assert sales.iloc[0]==pytest.approx(7711.5)
    assert sales.index[1]==pd.Period("2003-02", freq="M")
    assert sales.iloc[1]==pytest.approx(4000)



    
