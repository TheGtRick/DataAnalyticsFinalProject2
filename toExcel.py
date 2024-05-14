import pandas as pd
df = pd.read_csv("C:\\Users\\Rakon\\Desktop\\DataVis\\GamesInSteam.csv")
df.to_excel("GamesInSteam.xlsx", index=False)