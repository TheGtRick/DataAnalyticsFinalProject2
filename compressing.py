import pandas as pd

df = pd.read_csv("C:\\Users\\Rakon\\Desktop\\DataVis\\StockData.csv")

df['Date'] = pd.to_datetime(df['Date'])
new_row = pd.DataFrame({'Date': ['1989-06-01'], 'Price': [0], 'Open': [0], 'High': [0], 'Low': [0], 'Vol.': [0], 'Change %': [0]})
new_row['Date'] = pd.to_datetime(new_row['Date'])
df = pd.concat([new_row, df]).reset_index(drop=True)
df.set_index('Date', inplace=True)
compressed_df = df.resample('Q').agg({'Price': 'mean', 'Open': 'mean', 'High': 'mean', 'Low': 'mean', 'Vol.': 'sum'})
compressed_df['Change %'] = ((compressed_df['Price'] - compressed_df['Price'].shift()) / compressed_df['Price'].shift()) * 100
compressed_df['Change %'].iloc[0:2] = 0.0
compressed_df['Vol.'] = compressed_df['Vol.'].apply(lambda x: f"{x:.0f}")

compressed_df.index = compressed_df.index - pd.offsets.QuarterBegin()
print(compressed_df)
compressed_df.reset_index(inplace=True)
compressed_df['Date'] = pd.to_datetime(compressed_df['Date'])
compressed_df.set_index('Date', inplace=True)
compressed_df = compressed_df.iloc[:-2]

compressed_df.to_csv("C:\\Users\\Rakon\\Desktop\\DataVis\\CompressedStockData.csv")