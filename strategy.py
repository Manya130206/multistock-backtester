import pandas as pd
import numpy as np 

def generate_signals(df: pd.DataFrame,
                     rsi_buy: float = 40,
                     rsi_sell: float = 60) -> pd.DataFrame:
    df = df.copy()

    required_cols = ['Close', 'RSI', 'Upper_Band', 'Lower_Band']
    for col in required_cols:
        if col not in df.columns:
            raise ValueError(f"Missing {col} column")

    # 1. Create a clean DataFrame and establish the single, final index
    df_clean = df[required_cols].dropna() 
    final_index = df_clean.index
    
    # 2. Extract and EXPLICITLY REINDEX all Series to the final_index.
    #    We use 'fill_value=np.inf' for the indicator bounds to prevent 
    #    NaNs from appearing in the comparison (Close should never be compared 
    #    to an 'inf' bound if the data is clean, but it guarantees the Series 
    #    is not empty/mismatched).
    
    # Reindex the price and indicator Series
    close = df_clean['Close'].reindex(final_index)
    lower_band = df_clean['Lower_Band'].reindex(final_index)
    upper_band = df_clean['Upper_Band'].reindex(final_index)
    rsi = df_clean['RSI'].reindex(final_index)
    
    # 3. Generate Conditions
    # All Series now share the identical 'final_index'.
    buy_cond = (close < lower_band) & (rsi < rsi_buy)
    sell_cond = (close > upper_band) | (rsi > rsi_sell)

    # 4. Create signals Series
    # The index must match the index of the boolean conditions.
    signals = pd.Series(index=final_index, dtype='object')
    signals.loc[buy_cond] = 'BUY'
    signals.loc[sell_cond] = 'SELL'

    # 5. Assign signals back to the original df
    df['Signal'] = None
    
    # Reindex the signals to the FULL original df index for clean assignment
    df['Signal'] = signals.reindex(df.index)

    return df
