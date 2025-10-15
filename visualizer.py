import matplotlib.pyplot as plt

def plot_signals(df, ticker=""):
    plt.figure(figsize=(15, 7))

    # Price and indicators
    plt.plot(df['Close'], label='Close Price', color='black', alpha=0.8)
    plt.plot(df['SMA_20'], label='SMA 20', linestyle='--', color='orange')
    plt.plot(df['SMA_50'], label='SMA 50', linestyle='--', color='blue')
    plt.fill_between(df.index, df['Lower_Band'], df['Upper_Band'], color='gray', alpha=0.1)

    # Buy/Sell markers
    if 'Signal' in df.columns:
        df['Signal'] = df['Signal'].astype(str).str.strip()
        buys = df[df['Signal'] == 'BUY']
        sells = df[df['Signal'] == 'SELL']

        plt.scatter(buys.index, buys['Close'], marker='^', color='lime', s=50, label='BUY', zorder=5)
        plt.scatter(sells.index, sells['Close'], marker='v', color='red', s=50, label='SELL', zorder=5)

    plt.title(f"{ticker} Strategy Backtest")
    plt.xlabel("Date")
    plt.ylabel("Price")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()

