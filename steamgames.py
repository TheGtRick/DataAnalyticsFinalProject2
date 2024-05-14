from bs4 import BeautifulSoup as bs
import numpy as np
from selenium import webdriver
import pandas as pd
from selenium.webdriver.chrome.service import Service
import time
from io import StringIO
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

service = Service()
options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument('--ignore-ssl-errors')
options.add_argument('--disable-extensions')
options.add_argument('--disable-quic')
driver = webdriver.Chrome(service=service, options=options)
URL = "https://steamdb.info/publisher/Electronic+Arts/"
driver.get(URL)
time.sleep(3)
Select(driver.find_element(By.XPATH, '/html/body/div[4]/div[1]/div[2]/div[2]/div[2]/div[3]/div/div[1]/div[1]/select')).select_by_value('-1')
time.sleep(3)
content = driver.page_source
soup = bs(content, "html.parser")
tables = soup.find_all("table")
df = pd.read_html(StringIO(str(tables)))[0]
df = df.loc[:, ~df.columns.str.contains('^Unnamed')]
df = df.loc[:, ~df.columns.str.contains('^%')]
df = df.drop('Release', axis=1)
df = df[df["Name"].str[-4:] == "Game"]
df = df.replace('', '0')
df = df.replace('—', '0')
df["Name"] = df["Name"].apply(lambda x: x[:-5])
df["Price"] = df["Price"].apply(lambda x: int(x[:-1]) if x != '0' else int(x))
df["Rating"] = df["Rating"].apply(lambda x: float(x[:-1]) if x != '0' else float(x))
df.to_csv("C:\\Users\\Rakon\\Desktop\\DataVis\\GamesInSteam.csv", index=False)