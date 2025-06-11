import yfinance as yf

def fetch_stock_data(ticker):
    df = yf.download(ticker, start="2020-01-01")
    df.reset_index(inplace=True)
    return df
