import shutil
import pandas as pd
import datetime
import time
import yfinance as yf
def move_download(TICKER):
    source = f'C:/Users/joaom/Downloads/{TICKER}.csv'
    destination = 'C:/Users/joaom/OneDrive/Documentos/GitHub/Snp1000/Performance Tables'
    dest = shutil.move(source, destination) 


import yfinance as yf
import seaborn as sns
pd.set_option('display.max_rows',None)
import matplotlib.pyplot as plt
companies = pd.read_csv('SnP1000_TICKR.csv')
companies_list = companies['Companie'].to_list()
print(companies_list)
df = pd.DataFrame()

start = datetime.datetime(2020,10,19)
end = datetime.datetime(2021,10,19)

df = df.iloc[0:0]
companies_list=['TSLA']
for i in companies_list[:1]:
    print(str(companies_list.index(i)) + str(' : ') + i, sep=',', end=',', flush=True)
    try:
        stock = []
        stock = yf.download(i, start=start, end=end, progress=False)
        if len(stock) == 0:
            None
        else:
            stock['Name'] = i
            df = df.append(stock, sort=False)
    except Exception:
        None

df.reset_index(inplace=True)
df['Change'] = (df['Close'].shift(-1)-df['Close']).shift(1)
df['ChangeAverage'] = df['Change'].rolling(window=2).mean()
df['ChangeAverage+'] = df.apply(lambda x: x['ChangeAverage'] if x['ChangeAverage'] > 0 else 0,axis=1).rolling(window=14).mean()
df['ChangeAverage-'] = df.apply(lambda x: x['ChangeAverage'] if x['ChangeAverage'] < 0 else 0,axis=1).rolling(window=14).mean()*-1
df['RSI'] = 100-(100/(1+(df['ChangeAverage+']/df['ChangeAverage-'])))
from matplotlib.pyplot import figure
figure1 = df.plot.line(x='Date',y=['RSI'])
figure1.axhline(y = 30, color = 'r', linestyle = '-')
figure1.axhline(y = 70, color = 'r', linestyle = '-')
figure2 = df.plot.line(x='Date',y='Close')



VolumeList = df['Volume'].tolist()
OBV = [VolumeList[0]]
i=1



for i in range(len(VolumeList)-1):
    if VolumeList[i] > VolumeList[i-1]:
        OBV.append(VolumeList[i-1]+OVB[i])
                   
    if VolumeList[i]==VolumeList[i-1]:
        OBV.append(OBV[i-1]+0)
                   
    if VolumeList[i]<VolumeList[i-1]:
        OBV.append(VolumeList[i-1]-OBV[i])


        df['OBV_Rolling_M14'] = df.apply(lambda x: x['OBV'].rolling(window=10).diff()/10)
