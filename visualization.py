import matplotlib.pyplot as plt

def plot_stock_trends(df, symbol):
    plt.figure(figsize=(14, 7))
    plt.plot(df['Date'], df['Close'], label='Close Price', color='blue')
    plt.plot(df['Date'], df['MA20'], label='20-Day MA', color='green')
    plt.plot(df['Date'], df['MA50'], label='50-Day MA', color='red')
    plt.title(f"{symbol} Stock Price with Moving Averages")
    plt.xlabel('Date')
    plt.ylabel('Price (USD)')
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()
