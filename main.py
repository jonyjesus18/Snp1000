import csv
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import time
import requests
from csv import reader
import pandas as pd

'''
https://selenium-python.readthedocs.io/getting-started.html
'''

driver = webdriver.Chrome()
url = 'https://stockanalysis.com/ipos/2020/'
yahoo = 'https://uk.finance.yahoo.com/'
finVizz = 'https://finviz.com/'


def get_tickr(url):
    html_content = requests.get(url).text
    soup = BeautifulSoup(html_content, "html.parser")
    list = soup.find_all('a')
    stock_list = []
    for link in list:
        string = link.get('href')
        stock = string[1:7]
        if stock == 'stocks':
            val = string[8:].replace('/', '')
            # print(val)
            stock_list.append(val)
    with open('IPO.csv', 'a') as f:
        stock_list.remove('')
        for val in stock_list:
            print(val)
            f.write(val + '\n')


def openYahoo():
    init_button = driver.find_element_by_name('agree')
    init_button.click()


def openFinViz():
    driver.get(finVizz)
    driver.implicitly_wait(10)
    read_more_button = driver.find_element_by_xpath('/html/body/div[11]/div[1]/div[3]/button')
    read_more_button.click()
    accept_all_button = driver.find_element_by_xpath('/html/body/div[11]/div[1]/div[1]/div/button')
    accept_all_button.click()


def finVizEngine(input,output):
    ipo_df = pd.DataFrame({})
    openFinViz()
    with open(input, 'r') as IPO_List:
        csv_reader = reader(IPO_List)
        with open(output, 'a') as dataframe:
            writer = csv.writer(dataframe)
            HEADER = ['Ticker', 'MarketCap', 'Income', 'Sales', 'Booksh', 'Dividend',
                      'Dividend_Percentage', 'Employees', 'PriceToEarnings', 'ForwardPTE',
                      'PriceToSales', 'PriceToBook', 'PutCallRatio', 'QuickRatio', 'CurrentRatio', 'DebtEquity',
                      'ROA', 'ROE', 'ROI', 'GrossMargin', 'OperationalMargin', 'ProfitMargin', 'Payout',
                      'SHSOutstanding', 'ShsFloat', 'ShoartFloat', 'ShortRatio', 'TargetPrice', 'PerformaceHalfYear',
                      'PerformanceYear', 'PerformanceYTD']
            writer.writerow(HEADER)
            for IPO in csv_reader:
                try:
                    searchbox = driver.find_element_by_xpath('//*[@id="search"]/div/form/input')
                    searchbutton = driver.find_element_by_xpath('//*[@id="search"]/div/form/span')
                    searchbox.click()
                    searchbox.send_keys(IPO)
                    searchbutton.click()
                    driver.implicitly_wait(5)
                    # ----------------------------
                    MarketCap = driver.find_element_by_xpath('/html/body/div[4]/div/table[2]/tbody/tr[2]/td[2]/b').text
                    Income = driver.find_element_by_xpath('/html/body/div[4]/div/table[2]/tbody/tr[3]/td[2]/b').text
                    Sales = driver.find_element_by_xpath('/html/body/div[4]/div/table[2]/tbody/tr[4]/td[2]/b').text
                    Booksh = driver.find_element_by_xpath('/html/body/div[4]/div/table[2]/tbody/tr[5]/td[2]/b').text
                    Dividend = driver.find_element_by_xpath('/html/body/div[4]/div/table[2]/tbody/tr[7]/td[2]/b').text
                    Dividend_Percentage = driver.find_element_by_xpath(
                        '/html/body/div[4]/div/table[2]/tbody/tr[8]/td[2]/b').text
                    Employees = driver.find_element_by_xpath('/html/body/div[4]/div/table[2]/tbody/tr[9]/td[2]/b').text
                    PriceToEarnings = driver.find_element_by_xpath(
                        '/html/body/div[4]/div/table[2]/tbody/tr[1]/td[4]/b').text
                    ForwardPTE = driver.find_element_by_xpath('/html/body/div[4]/div/table[2]/tbody/tr[2]/td[4]/b').text
                    PriceToSales = driver.find_element_by_xpath(
                        '/html/body/div[4]/div/table[2]/tbody/tr[4]/td[4]/b').text
                    PriceToBook = driver.find_element_by_xpath(
                        '/html/body/div[4]/div/table[2]/tbody/tr[5]/td[4]/b').text
                    PutCallRatio = driver.find_element_by_xpath(
                        '/html/body/div[4]/div/table[2]/tbody/tr[6]/td[4]/b').text
                    QuickRatio = driver.find_element_by_xpath('/html/body/div[4]/div/table[2]/tbody/tr[8]/td[4]/b').text
                    CurrentRatio = driver.find_element_by_xpath(
                        '/html/body/div[4]/div/table[2]/tbody/tr[9]/td[4]/b').text
                    DebtEquity = driver.find_element_by_xpath(
                        '/html/body/div[4]/div/table[2]/tbody/tr[10]/td[4]/b').text
                    ROA = driver.find_element_by_xpath('/html/body/div[4]/div/table[2]/tbody/tr[5]/td[8]/b').text
                    ROE = driver.find_element_by_xpath('/html/body/div[4]/div/table[2]/tbody/tr[6]/td[8]/b').text
                    ROI = driver.find_element_by_xpath('/html/body/div[4]/div/table[2]/tbody/tr[7]/td[8]/b').text
                    GrossMargin = driver.find_element_by_xpath(
                        '/html/body/div[4]/div/table[2]/tbody/tr[8]/td[8]/b').text
                    OperationalMargin = driver.find_element_by_xpath(
                        '/html/body/div[4]/div/table[2]/tbody/tr[9]/td[8]/b').text
                    ProfitMargin = driver.find_element_by_xpath(
                        '/html/body/div[4]/div/table[2]/tbody/tr[10]/td[8]/b').text
                    Payout = driver.find_element_by_xpath('/html/body/div[4]/div/table[2]/tbody/tr[11]/td[8]/b').text
                    SHSOutstanding = driver.find_element_by_xpath(
                        '/html/body/div[4]/div/table[2]/tbody/tr[1]/td[10]/b').text
                    ShsFloat = driver.find_element_by_xpath('/html/body/div[4]/div/table[2]/tbody/tr[2]/td[10]/b').text
                    ShoartFloat = driver.find_element_by_xpath(
                        '/html/body/div[4]/div/table[2]/tbody/tr[3]/td[10]/b').text
                    ShortRatio = driver.find_element_by_xpath(
                        '/html/body/div[4]/div/table[2]/tbody/tr[4]/td[10]/b').text
                    TargetPrice = driver.find_element_by_xpath(
                        '/html/body/div[4]/div/table[2]/tbody/tr[5]/td[10]/b').text
                    PerformaceHalfYear = driver.find_element_by_xpath(
                        '/html/body/div[4]/div/table[2]/tbody/tr[4]/td[12]/b').text
                    PerformanceYear = driver.find_element_by_xpath(
                        '/html/body/div[4]/div/table[2]/tbody/tr[5]/td[12]/b').text
                    PerformanceYTD = driver.find_element_by_xpath(
                        '/html/body/div[4]/div/table[2]/tbody/tr[6]/td[12]/b').text
                    # ----------------------------
                    INSERT = [IPO, MarketCap, Income, Sales, Booksh, Dividend,
                              Dividend_Percentage, Employees, PriceToEarnings, ForwardPTE,
                              PriceToSales, PriceToBook, PutCallRatio, QuickRatio, CurrentRatio, DebtEquity,
                              ROA, ROE, ROI, GrossMargin, OperationalMargin, ProfitMargin, Payout,
                              SHSOutstanding, ShsFloat, ShoartFloat, ShortRatio, TargetPrice, PerformaceHalfYear,
                              PerformanceYear, PerformanceYTD]
                    print(INSERT)
                    dataframe.write(str(INSERT) + '\n')
                except:
                    try:
                        x = driver.find_element_by_id('modal-elite-ad-close')
                        x.click()
                    except:
                        pass
                    pass


def cleanFinVizData(csv):
    pd.set_option('display.max_columns', None)
    data = pd.read_csv('IPO_data.csv')
    data = data.dropna()
    data = data.replace("'", '', regex=True)
    data = data.replace(" ", '', regex=True)
    list1 = ['IPO', 'MarketCap', 'Income', 'Sales', 'Booksh', 'Dividend',
             'Dividend_Percentage', 'Employees', 'PriceToEarnings', 'ForwardPTE',
             'PriceToSales', 'PriceToBook', 'PutCallRatio', 'QuickRatio', 'CurrentRatio', 'DebtEquity',
             'SHSOutstanding', 'ShsFloat', 'ShortRatio', 'TargetPrice',
             'ROI', 'ROE', 'ROA', 'GrossMargin', 'OperationalMargin', 'ProfitMargin',
             'ShoartFloat', 'PerformaceHalfYear', 'PerformanceYear', 'PerformanceYTD', 'Payout']

    list2 = ['MarketCap', 'Income', 'Sales',
             'SHSOutstanding', 'ShsFloat']

    for column in list1:
        data[f'{column}'] = data[f'{column}'].apply(lambda x: x.replace('[', '').replace(']', ''))

    for column in list2:
        data[f'{column}'] = data[f'{column}'].apply(
            lambda x: str(x).replace('.', '').replace('M', '00000') if str(x[-1]) == 'M' else x)
        data[f'{column}'] = data[f'{column}'].apply(
            lambda x: str(x).replace('.', '').replace('B', '00000000') if str(x[-1]) == 'B' else x)
        data[f'{column}'] = data[f'{column}'].apply(lambda x: x.replace('-', '0') if x == '-' else x)
        data[f'{column}'] = data[f'{column}'].apply(lambda x: int(float(x))) / 100

    for column in list1:
        data[f'{column}'] = data[f'{column}'].apply(
            lambda x: float((str(x).replace('%', '00'))) if '%' in str(x) else x)

    list4 = ['MarketCap', 'Income', 'Sales', 'Booksh', 'Dividend',
             'Dividend_Percentage', 'Employees', 'PriceToEarnings', 'ForwardPTE',
             'PriceToSales', 'PriceToBook', 'PutCallRatio', 'QuickRatio', 'CurrentRatio', 'DebtEquity',
             'SHSOutstanding', 'ShsFloat', 'ShoartFloat', 'ShortRatio', 'TargetPrice', 'PerformaceHalfYear',
             'PerformanceYear', 'Payout', 'PerformanceYTD', 'ROI', 'ROE', 'ROA', 'GrossMargin', 'OperationalMargin',
             'ProfitMargin', ]
    for column in list4:
        data[f'{column}'] = data[f'{column}'].apply(lambda x: x.replace('-', '0') if x == '-' else x)
        data[f'{column}'] = data[f'{column}'].apply(lambda x: float(str(x)))

    data['IPO'] = data['IPO'].str.upper()

    data['IPO'] = data['IPO'].str.upper()
    data = data.rename(columns={'ROA': 'ROA(%)', 'ROE': 'ROE(%)', 'ROI': 'ROI(%)', 'GrossMargin': 'GrossMargin(%)'
        , 'ProfitMargin': 'ProfitMargin(%)', 'Payout': 'Payout(%)', 'ShoartFloat': 'ShortFloat(%)',
                                'PerformaceHalfYear': 'PerformanceHalfYear(%)', 'PerformanceYear': 'PerformanceYear(%)',
                                'PerformanceYTD': 'PerformanceYTD(%)'})

    data = data.sort_values(by=['PerformanceYTD(%)'], ascending=False)
    return data

finVizEngine('SnP1000_TICKR.csv','SnP1000_DATA,csv')
data = cleanFinVizData('SnP1000_DATA.csv')
data.to_csv('SnP1000_DATA.csv', index=False)

#NEW CHANGES!!!!!!!!!!
