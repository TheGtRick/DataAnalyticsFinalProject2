from bs4 import BeautifulSoup as bs
import numpy as np
from selenium import webdriver
import pandas as pd
from selenium.webdriver.chrome.service import Service
import time
from io import StringIO
from selenium.webdriver.common.by import By

service = Service()
options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument('--ignore-ssl-errors')
options.add_argument('--disable-extensions')
options.add_argument('--disable-quic')
driver = webdriver.Chrome(service=service, options=options)
URL = "https://ycharts.com/companies/EA/financials/income_statement/18"
driver.get(URL)
time.sleep(3)
driver.find_element(By.XPATH, '/html/body/ycn-top-bar-nav/header/div/div[4]/div[3]/a').click()
time.sleep(3)
driver.find_element(By.XPATH, '//*[@id="id_username"]').send_keys('220107020@stu.sdu.edu.kz')
driver.find_element(By.XPATH, '//*[@id="id_password"]').send_keys('R@iym12345')
driver.find_element(By.XPATH, '/html/body/main/div/div[2]/div/form/div/div[4]/button').click()
time.sleep(3)
content = driver.page_source
soup = bs(content, 'html.parser')
def set_level_of_df(df, level_index, labels):
    new_df = df.copy()
    unique, inverse = np.unique(labels, return_inverse=True)
    new_df.columns = new_df.columns.set_codes(inverse, level=level_index)
    new_df.columns = new_df.columns.set_levels(unique, level=level_index)
    return new_df
tables = soup.find_all("table", class_="table table-dense table-striped")
df = pd.read_html(StringIO(str(tables)))[0]
i = df.columns.get_level_values(0)
new_vals = i.where(~i.str.startswith('Unnamed: '), 'test_col')
df = set_level_of_df(df, 0, new_vals)
df = df.drop(columns=['test_col'], errors='ignore')
df = df.T
df = df.reset_index()
df.columns = df.iloc[0]
df = df.drop(0)
df = df.reset_index(drop=True)
df = df.drop(columns=['Actual Release Date'], errors='ignore')
df = df.rename(columns={'Future Periods': 'Date'})
df['Date'] = pd.to_datetime(df['Date'])
df = df.replace('--', '0')
for col in df.columns:
    if col != 'Date':
        df[col] = df[col].apply(lambda x: float(x[:-1]) * 1000000 if x.endswith('M') else float(x[:-1]) * 1000000000 if x.endswith('B') else float(x[:-1]) if x.endswith('%') else float(x))
for col in df.columns:
    if col != 'Date':
        df[col] = pd.to_numeric(df[col])
for j in range(len(tables) - 2):
    dfn = pd.read_html(StringIO(str(tables)))[j + 1]
    i = dfn.columns.get_level_values(0)
    new_vals = i.where(~i.str.startswith('Unnamed: '), 'test_col')
    dfn = set_level_of_df(dfn, 0, new_vals)
    dfn = dfn.drop(columns=['test_col'], errors='ignore')
    dfn = dfn.T
    dfn = dfn.reset_index()
    dfn.columns = dfn.iloc[0]
    dfn = dfn.drop(0)
    dfn = dfn.reset_index(drop=True)
    dfn = dfn.drop(columns=['Actual Release Date'], errors='ignore')
    dfn = dfn.rename(columns={'Future Periods': 'Date'})
    dfn['Date'] = pd.to_datetime(dfn['Date'])
    dfn = dfn.replace('--', '0')
    for col in dfn.columns:
        if col != 'Date':
            dfn[col] = dfn[col].apply(lambda x: float(x[:-1]) * 1000000 if x.endswith('M') else float(x[:-1]) * 1000000000 if x.endswith('B') else float(x[:-1]) if x.endswith('%') else float(x))
    for col in dfn.columns:
        if col != 'Date':
            dfn[col] = pd.to_numeric(dfn[col])
    df = pd.merge(df, dfn, on='Date')
for i in range(1, 18):
    driver.find_element(By.XPATH, '//*[@id="finTabs"]/div/div[2]/div[1]/div/div/div[5]/span[1]/a').click()
    time.sleep(3)
    content = driver.page_source
    soup = bs(content, 'html.parser')
    tables = soup.find_all("table", class_="table table-dense table-striped")
    dfc = pd.read_html(StringIO(str(tables)))[0]
    i = dfc.columns.get_level_values(0)
    new_vals = i.where(~i.str.startswith('Unnamed: '), 'test_col')
    dfc = set_level_of_df(dfc, 0, new_vals)
    dfc = dfc.drop(columns=['test_col'], errors='ignore')
    dfc = dfc.T
    dfc = dfc.reset_index()
    dfc.columns = dfc.iloc[0]
    dfc = dfc.drop(0)
    dfc = dfc.reset_index(drop=True)
    dfc = dfc.drop(columns=['Actual Release Date'], errors='ignore')
    dfc = dfc.rename(columns={'Future Periods': 'Date'})
    dfc['Date'] = pd.to_datetime(dfc['Date'])
    dfc = dfc.replace('--', '0')
    for col in dfc.columns:
        if col != 'Date':
            dfc[col] = dfc[col].apply(lambda x: float(x[:-1]) * 1000000 if x.endswith('M') else float(x[:-1]) * 1000000000 if x.endswith('B') else float(x[:-1]) if x.endswith('%') else float(x))
    for col in dfc.columns:
        if col != 'Date':
            dfc[col] = pd.to_numeric(dfc[col])
    for j in range(len(tables) - 2):
        dfn = pd.read_html(StringIO(str(tables)))[j + 1]
        i = dfn.columns.get_level_values(0)
        new_vals = i.where(~i.str.startswith('Unnamed: '), 'test_col')
        dfn = set_level_of_df(dfn, 0, new_vals)
        dfn = dfn.drop(columns=['test_col'], errors='ignore')
        dfn = dfn.T
        dfn = dfn.reset_index()
        dfn.columns = dfn.iloc[0]
        dfn = dfn.drop(0)
        dfn = dfn.reset_index(drop=True)
        dfn = dfn.drop(columns=['Actual Release Date'], errors='ignore')
        dfn = dfn.rename(columns={'Future Periods': 'Date'})
        dfn['Date'] = pd.to_datetime(dfn['Date'])
        dfn = dfn.replace('--', '0')
        for col in dfn.columns:
            if col != 'Date':
                dfn[col] = dfn[col].apply(lambda x: float(x[:-1]) * 1000000 if x.endswith('M') else float(x[:-1]) * 1000000000 if x.endswith('B') else float(x[:-1]) if x.endswith('%') else float(x))
        for col in dfn.columns:
            if col != 'Date':
                dfn[col] = pd.to_numeric(dfn[col])
        dfc = pd.merge(dfc, dfn, on='Date')
    df = pd.concat([df, dfc])
df = df.sort_values(by='Date')
df.to_csv("C:\\Users\\Rakon\\Desktop\\DataVis\\FinancialData.csv", index=False)