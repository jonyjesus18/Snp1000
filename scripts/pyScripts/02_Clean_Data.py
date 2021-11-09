import pandas as pd
import numpy as np

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
data = pd.read_csv('SnP1000_DATA.csv')
data.shape
#data = data.dropna()
data = data.replace("'",'', regex=True)
data = data.replace(" ",'', regex=True)


list1 = ['Ticker','MarketCap', 'Income', 'Sales', 'Booksh', 'Dividend',
        'Dividend_Percentage', 'Employees', 'PriceToEarnings', 'ForwardPTE',
        'PriceToSales','PEG', 'PriceToBook', 'PutCallRatio', 'QuickRatio', 'CurrentRatio', 'DebtEquity',
        'SHSOutstanding', 'ShsFloat', 'ShortRatio', 'TargetPrice',
        'ROI','ROE','ROA','GrossMargin','OperationalMargin','ProfitMargin',
        'ShoartFloat','PerformaceHalfYear','PerformanceYear','PerformanceYTD','Payout',
        'Index','Cashsh','Recom','PFCF','LdDebtEquity',
         'SMA20','SMA50','SMA200','52WL','52WH','AVGVol','Vol','Unnamed: 44','Unnamed: 45']

list2 = ['MarketCap','Income','Sales',
'SHSOutstanding','ShsFloat','AVGVol']
data.shape

for column in list1:
    data[f'{column}'] = data[f'{column}'].apply(lambda x: str(x).replace('[','').replace(']','')) 
for column in list2:
    data[f'{column}'] = data[f'{column}'].apply(lambda x: str(x).replace('.','').replace('M','00000') if str(x[-1]) == 'M' else x )
    data[f'{column}'] = data[f'{column}'].apply(lambda x: str(x).replace('.','').replace('B','00000000') if str(x[-1]) == 'B' else x )
    data[f'{column}'] = data[f'{column}'].apply(lambda x: str(x).replace('.','').replace('K','000') if str(x[-1]) == 'K' else x )

    data[f'{column}'] = data[f'{column}'].apply(lambda x: x.replace('-','0') if x == '-' else x)
    data[f'{column}'] = data[f'{column}'].apply(lambda x: int(float(x)))/100

for column in list1:
    data[f'{column}'] = data[f'{column}'].apply(lambda x: float((str(x).replace('%','00'))) if '%' in str(x) else x) 
    
list4 = ['MarketCap', 'Income', 'Sales', 'Booksh','Cashsh','Recom','Dividend',
                      'Dividend_Percentage', 'Employees', 'PriceToEarnings', 'ForwardPTE','LdDebtEquity','PEG','PFCF',
                      'PriceToSales', 'PriceToBook', 'PutCallRatio', 'QuickRatio', 'CurrentRatio', 'DebtEquity',
                      'SHSOutstanding', 'ShsFloat', 'ShoartFloat', 'ShortRatio', 'TargetPrice', 'PerformaceHalfYear',
                      'PerformanceYear','Payout', 'PerformanceYTD','ROI','ROE','ROA','GrossMargin','OperationalMargin','ProfitMargin','Unnamed: 44','Unnamed: 45']
for column in list4:
    data[f'{column}'] = data[f'{column}'].apply(lambda x: x.replace('-','0') if x == '-' else x)
    data[f'{column}'] = data[f'{column}'].apply(lambda x: float(str(x)))


data['Ticker'] = data['Ticker'].str.upper()  
data = data.rename(columns={'ROA': 'ROA(%)', 'ROE': 'ROE(%)','ROI':'ROI(%)','GrossMargin': 'GrossMargin(%)'
                          ,'ProfitMargin':'ProfitMargin(%)','Payout':'Payout(%)','ShoartFloat':'ShortFloat(%)',
                         'PerformaceHalfYear':'PerformanceHalfYear(%)','PerformanceYear':'PerformanceYear(%)','PerformanceYTD':'PerformanceYTD(%)'})


data['PerformanceHalfYear(%)'] = data['PerformanceYTD(%)']
data['PerformanceYear(%)'] = data['Unnamed: 44']
data['PerformanceYTD(%)'] = data['Unnamed: 45']
data = data.drop(columns = ['Vol','Unnamed: 44','Unnamed: 45'],axis=1)
data['PerformanceYTD(%)'] = data['PerformanceYTD(%)'].apply(lambda x: float((str(x).replace('%','00'))) if '%' in str(x) else x)

index_data = pd.read_csv('SnP1000.csv')
index_data['2'] = index_data['2'].apply(lambda x: x.replace('\n',''))
index_data['3'] = index_data['3'].apply(lambda x: x.replace('\n',''))
index_data = index_data.drop(columns = ['0','4','5'],index = 1)
data = data.drop(columns = ['Index'], axis = 1)
index_data = index_data.rename(columns={'1': 'Ticker', '2': 'Industry','3':'Sub Industry','6': 'Index'})
data = pd.merge(data, index_data,how="left", on="Ticker") #add all index_data columns to main dataframe on correct ticker

data.sort_values(by=['PerformanceHalfYear(%)','Industry','Sub Industry'], ascending = False)