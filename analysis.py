def calculate_moving_averages(df, short_window=20, long_window=50):
    df['MA20'] = df['Close'].rolling(window=short_window).mean()
    df['MA50'] = df['Close'].rolling(window=long_window).mean()
    return df
