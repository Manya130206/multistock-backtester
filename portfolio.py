import pandas as pd
import numpy as np

def simulate_portfolio(df, initial_cash=10000):
    df = df.copy()
    cash = initial_cash
    position = 0
    trade_log = []

    df['Portfolio Value'] = np.nan

    for i in range(len(df)):
        signal = df['Signal'].iloc[i]
        close_price = float(df['Close'].iloc[i].item())  # Ensure scalar float

        # Buy logic
        if isinstance(signal, str) and signal.upper() == 'BUY' and cash >= close_price:
            qty = int(cash // close_price)  # Use floor division for full shares
            cost = qty * close_price
            if qty > 0:
                cash -= cost
                position += qty
                trade_log.append({
                    'Date': df.index[i],
                    'Action': 'BUY',
                    'Price': close_price,
                    'Qty': qty
                })

        # Sell logic
        elif isinstance(signal, str) and signal.upper() == 'SELL' and position > 0:
            revenue = position * close_price
            cash += revenue
            trade_log.append({
                'Date': df.index[i],
                'Action': 'SELL',
                'Price': close_price,
                'Qty': position
            })
            position = 0

        # Portfolio value = cash + current value of holdings
        df.at[df.index[i], 'Portfolio Value'] = cash + (position * close_price)

    df['Portfolio Value'] = df['Portfolio Value'].ffill()

    return df, trade_log

