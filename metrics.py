import pandas as pd
import numpy as np

def compute_sharpe_ratio(df: pd.DataFrame, risk_free_rate: float = 0.01)-> float:
    returns = df['Log Return'].dropna()
    excess_return = returns - risk_free_rate/252
    sharpe = (excess_return.mean()/ returns.std())*np.sqrt(252)
    return sharpe

def compute_max_drawdown(df : pd.DataFrame) -> float:
    return df['Drawdown'].min()

def compute_cagr(df : pd.DataFrame) ->float:
    n = len(df)
    total_return = df['Cumulative_Return'].iloc[-1]
    years = n/252 #approx no of trading days
    cagr = total_return ** (1/years) -1
    return cagr
