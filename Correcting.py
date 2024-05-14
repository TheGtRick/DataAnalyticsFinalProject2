import pandas as pd
df = pd.read_csv("C:\\Users\\Rakon\\Desktop\\DataVis\\Games.csv")
df = df.drop(columns={'Platforms'})
df['Developer(s)'] = df['Developer(s)'].replace({'TBA': 'Unknown'})
df['Release date'] = df['Release date'].replace({'TBA': '2024'})
df = df.groupby(['Title', 'Release date', 'Developer(s)']).sum().reset_index()
df['Release date'] = pd.to_datetime(df['Release date'], format='%Y')
df = df.sort_values(by='Release date')
df["Genre"] = "Action"
df.to_csv("C:\\Users\\Rakon\\Desktop\\DataVis\\Games.csv", index=False)