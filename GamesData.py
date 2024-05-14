from bs4 import BeautifulSoup as bs
from selenium import webdriver
import pandas as pd
from selenium.webdriver.chrome.service import Service
from io import StringIO
from selenium.webdriver.common.by import By
import time

service = Service()
options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument('--ignore-ssl-errors')
options.add_argument('--disable-extensions')
options.add_argument('--disable-quic')
driver = webdriver.Chrome(service=service, options=options)
URL = "https://en.wikipedia.org/wiki/List_of_Electronic_Arts_games:_1983%E2%80%931999"
driver.get(URL)
time.sleep(3)
content = driver.page_source
soup = bs(content, "html.parser")
tables = soup.find_all("table")
df = pd.read_html(StringIO(str(tables)))[1]

URL = "https://en.wikipedia.org/wiki/List_of_Electronic_Arts_games:_2000%E2%80%932009"
driver.get(URL)
time.sleep(3)
content = driver.page_source
soup = bs(content, "html.parser")
tables = soup.find_all("table")
dfn = pd.read_html(StringIO(str(tables)))[1]
df = pd.concat([df, dfn])

URL = "https://en.wikipedia.org/wiki/List_of_Electronic_Arts_games:_2010%E2%80%932019"
driver.get(URL)
time.sleep(3)
content = driver.page_source
soup = bs(content, "html.parser")
tables = soup.find_all("table")
dfn = pd.read_html(StringIO(str(tables)))[1]
df = pd.concat([df, dfn])

URL = "https://en.wikipedia.org/wiki/List_of_Electronic_Arts_games:_2020%E2%80%93present"
driver.get(URL)
time.sleep(3)
content = driver.page_source
soup = bs(content, "html.parser")
tables = soup.find_all("table")
dfn = pd.read_html(StringIO(str(tables)))[1]
df = pd.concat([df, dfn])
df["Release date"] = df["Release date"].str[-4:]
df = df.drop(columns={"Ref(s)"})
df.to_csv('C:\\Users\\Rakon\\Desktop\\DataVis\\Games.csv', index=False)