import numpy as np
import pandas as pd
from ta.momentum import RSIIndicator

def compute_indicators(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()

    # Log Return
    close, close_shift = df['Close'].align(df['Close'].shift(1), join='inner')
    df['Log Return'] = np.log(close / close_shift)

    # Percent Return
    df['Return'] = df['Close'].pct_change()

    # Cumulative Return
    df['Cumulative_Return'] = (1 + df['Return']).cumprod()

    # Cumulative Max
    df['Cumulative_Max'] = df['Cumulative_Return'].cummax()

    # Drawdown
    cum_return, cum_max = df['Cumulative_Return'].align(df['Cumulative_Max'], join='inner')
    df['Drawdown'] = cum_return / cum_max - 1

    # Moving Averages
    df['SMA_20'] = df['Close'].rolling(window=20).mean()
    df['SMA_50'] = df['Close'].rolling(window=50).mean()

    # RSI
    rsi = RSIIndicator(df['Close'].squeeze(), window=14)
    df['RSI'] = rsi.rsi()

    # Bollinger Bands
    window = 20
    df['Middle_Band'] = df['Close'].rolling(window).mean()
    df['STD'] = df['Close'].rolling(window).std()
    df['Upper_Band'] = df['Middle_Band'] + 2 * df['STD']
    df['Lower_Band'] = df['Middle_Band'] - 2 * df['STD']

    # Final cleanup
    df.dropna(inplace=True)
    return df
