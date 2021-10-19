import shutil
import pandas as pd
import datetime
import time
import yfinance as yf
def move_download(TICKER):
    source = f'C:/Users/joaom/Downloads/{TICKER}.csv'
    destination = 'C:/Users/joaom/OneDrive/Documentos/GitHub/Snp1000/Performance Tables'
    dest = shutil.move(source, destination) 


companies = pd.read_csv('SnP1000_TICKR.csv')
companies_list = companies['Companie'].to_list()
print(companies_list)
stock_final = pd.DataFrame()

start = datetime.datetime(2020,10,19)
end = datetime.datetime(2021,10,19)

for i in companies_list[:3]:
    print(str(companies_list.index(i)) + str(' : ') + i, sep=',', end=',', flush=True)
    try:
        stock = []
        stock = yf.download(i, start=start, end=end, progress=False)
        if len(stock) == 0:
            None
        else:
            stock['Name'] = i
            stock_final = stock_final.append(stock, sort=False)
    except Exception:
        None


