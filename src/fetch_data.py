import requests
import pandas as pd

API_KEY = "acHoNoczANkNzrIXD2tIQmWWjfFguKjy"

def get_stock_data(symbol="AAPL"):
    
    url = f"https://financialmodelingprep.com/stable/historical-price-eod/full?symbol={symbol}&apikey={API_KEY}"
    
    response = requests.get(url)
    data = response.json()
    
    df = pd.DataFrame(data)
    
    df["date"] = pd.to_datetime(df["date"])
    
    return df


def get_earnings_data(symbol="AAPL"):
    
    url = f"https://financialmodelingprep.com/stable/earnings-calendar?symbol={symbol}&apikey={API_KEY}"
    
    response = requests.get(url)
    data = response.json()
    
    df = pd.DataFrame(data)
    
    df["date"] = pd.to_datetime(df["date"])
    
    return df
