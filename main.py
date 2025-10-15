from data_loader import fetch_data
from indicators import compute_indicators
from strategy import generate_signals
from portfolio import simulate_portfolio
from metrics import compute_sharpe_ratio, compute_max_drawdown, compute_cagr
from visualizer import plot_signals
import pandas as pd

# Load data for multiple tickers
tickers = ["AAPL", "MSFT", "GOOG"]
raw_data = fetch_data(tickers)

# Dictionaries to store results
all_dfs = {}
all_trade_logs = {}

for ticker in tickers:
    print(f"\nProcessing {ticker}...\n")

    # Extract single stock DataFrame from MultiIndex
    df_raw = raw_data[ticker].copy()
    
    # Flatten MultiIndex if needed
    if isinstance(df_raw.columns, pd.MultiIndex):
        df_raw.columns = ['_'.join(col).strip() for col in df_raw.columns.values]
        # Rename Close column to 'Close' for your indicators
        close_cols = [c for c in df_raw.columns if 'Close' in c]
        df_raw.rename(columns={close_cols[0]: 'Close'}, inplace=True)

    # Compute indicators
    df = compute_indicators(df_raw)

    # Generate signals
    df = generate_signals(df)

    # Simulate portfolio
    df, trade_log = simulate_portfolio(df)

    # Store results
    all_dfs[ticker] = df
    all_trade_logs[ticker] = trade_log

    # Plot
    plot_signals(df, ticker=ticker)

    # Print metrics
    print(f"{ticker} Sharpe Ratio:", compute_sharpe_ratio(df))
    print(f"{ticker} Max Drawdown:", compute_max_drawdown(df))
    print(f"{ticker} CAGR:", compute_cagr(df))
