from typing import List, Dict
import yfinance as yf
import pandas as pd

def fetch_data(
    tickers: List[str],
    start: str = "2020-01-01",
    end: str = "2025-01-01"
) -> Dict[str, pd.DataFrame]:
    
    data_dict: Dict[str, pd.DataFrame] = {}
    required_cols = ["Open", "High", "Low", "Close", "Volume"]

    for ticker in tickers:
        df = yf.download(ticker, start=start, end=end)

        #Check if all required columns are present
        if not all(col in df.columns for col in required_cols):
            print(f"Skipping {ticker}: Missing OHLCV columns.")
            continue

        #Drop missing rows
        df = df[required_cols].dropna()

        # Skip if too few rows (avoid unstable indicators)
        if len(df) < 50:
            print(f"Skipping {ticker}: Not enough data ({len(df)} rows).")
            continue

        data_dict[ticker] = df

    if not data_dict:
        raise ValueError("No valid data fetched for any ticker.")

    return data_dict

"""
    Fetch OHLCV data for multiple tickers using yfinance.
    
    Args:
        tickers: List of stock symbols (e.g., ["AAPL", "MSFT"])
        start: Start date for historical data (YYYY-MM-DD)
        end: End date for historical data (YYYY-MM-DD)
    
    Returns:
        A dictionary mapping each ticker to its OHLCV DataFrame.
        Each DataFrame includes ['Open', 'High', 'Low', 'Close', 'Volume'].
"""