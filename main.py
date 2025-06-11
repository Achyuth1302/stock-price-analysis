from fetch_data import fetch_stock_data
from analysis import calculate_moving_averages
from visualization import plot_stock_trends



def main():
    symbol = 'AAPL'  # Apple
    df = fetch_stock_data(symbol)
    df = calculate_moving_averages(df)
    plot_stock_trends(df, symbol)

if __name__ == "__main__":
    main()
