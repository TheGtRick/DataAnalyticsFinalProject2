import pandas as pd
df = pd.read_csv("C:\\Users\\Rakon\\Desktop\\DataVis\\StockData.csv")
df['Date'] = pd.to_datetime(df['Date'])
df['Vol.'] = df['Vol.'].replace({'M': '*1e6', 'K': '*1e3'}, regex=True).map(pd.eval)
df['Change %'] = df['Change %'].str.replace('%', '')
numeric_cols = ['Price', 'Open', 'High', 'Low', 'Change %']
df[numeric_cols] = df[numeric_cols].apply(pd.to_numeric)
df = df.sort_values(by='Date')
df.to_csv("C:\\Users\\Rakon\\Desktop\\DataVis\\StockData.csv", index=False)