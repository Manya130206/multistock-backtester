#  Multi-Stock Trading Strategy Backtester  

### **Author:** [Manya Shah](https://www.linkedin.com/in/manya-shah-486543358/)  
 **Email:** [manyashah1320@gmail.com](mailto:manyashah1320@gmail.com)  
 **GitHub:** [Manya130206](https://github.com/Manya130206)  

---

##  Project Overview  
This project implements an **automated multi-stock backtesting system** using **technical indicators** such as **RSI (Relative Strength Index)** and **Bollinger Bands**.  
It fetches stock data using **`yfinance`**, computes key indicators, generates **BUY/SELL** signals, simulates a trading portfolio, and evaluates performance through **Sharpe Ratio**, **CAGR**, and **Max Drawdown**.  

It helps traders and analysts assess the effectiveness of rule-based strategies across different stocks and timeframes.

---

##  Objectives  
 Fetch historical OHLCV data using **yfinance**  
 Compute **RSI**, **Bollinger Bands**, and **SMA (20 & 50)**  
 Generate **BUY/SELL** trading signals  
 Simulate portfolio performance  
 Visualize trades and strategy performance  
 Calculate key financial metrics  
 <img width="1918" height="1130" alt="image" src="https://github.com/user-attachments/assets/dd2985f4-d0c3-42a3-b8fc-bf29da964816" />
<img width="1850" height="938" alt="Screenshot 2025-10-15 150407" src="https://github.com/user-attachments/assets/3c881d33-a67f-485b-bf70-47bce4eafc72" />
<img width="1866" height="935" alt="Screenshot 2025-10-15 150344" src="https://github.com/user-attachments/assets/6a8bc2a9-b479-42b0-bb9b-12101aaaa1ec" />


---

##  Tools & Libraries  
| Library | Purpose |
|----------|----------|
| `pandas` | Data handling and manipulation |
| `numpy` | Numerical computation |
| `matplotlib` | Plotting and visualization |
| `yfinance` | Fetching financial market data |

---

##  Project Structure  
```plaintext
 project_2_backtester/
│
├── data_loader.py        # Fetches OHLCV data from yfinance
├── indicators.py         # Calculates RSI, SMA, Bollinger Bands
├── strategy.py           # Generates BUY/SELL signals
├── portfolio.py          # Simulates portfolio & trade logging
├── metrics.py            # Computes Sharpe Ratio, CAGR, Max Drawdown
├── visualizer.py         # Plots signals, prices, and indicators
├── main.py               # Orchestrates full pipeline
└── README.md             # Project documentation
