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



# options = webdriver.ChromeOptions()
# options.add_experimental_option('excludeSwitches', ['enable-logging'])
# driver = webdriver.Chrome(options=options)

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
    driver = webdriver.Chrome()
    init_button = driver.find_element_by_name('agree')
    init_button.click()


def openFinViz():
    driver = webdriver.Chrome(executable_path = r"C:\Users\joaom\OneDrive\Documentos\GitHub\Snp1000\Scripts\chromedriver.exe")
    driver.get(finVizz)
    driver.implicitly_wait(10)
    read_more_button = driver.find_element_by_xpath('/html/body/div[11]/div[1]/div[3]/button')
    read_more_button.click()
    accept_all_button = driver.find_element_by_xpath('/html/body/div[11]/div[1]/div[1]/div/button')
    accept_all_button.click()


def finVizEngine(input,output):
    import chromedriver_autoinstaller
    chromedriver_autoinstaller.install()  # Check if the current version of chromedriver exists
                                      # and if it doesn't exist, download it automatically,
                                      # then add chromedriver to path

    #driver = webdriver.Chrome(r'C:\Users\joaom\OneDrive\Documentos\GitHub\Snp1000\Scripts\chromedriver.exe')
    driver = webdriver.Chrome()
    ipo_df = pd.DataFrame({})
    #----------------
    #driver = webdriver.Chrome(executable_path = r"C:\Users\joaom\OneDrive\Documentos\GitHub\Snp1000\Scripts\chromedriver.exe")
    driver.get(finVizz)
    driver.implicitly_wait(10)
    read_more_button = driver.find_element_by_xpath('/html/body/div[11]/div[1]/div[3]/button')
    read_more_button.click()
    accept_all_button = driver.find_element_by_xpath('/html/body/div[11]/div[1]/div[1]/div/button')
    accept_all_button.click()
    #----------------
    with open(input, 'r') as IPO_List:
        csv_reader = reader(IPO_List)
        with open(output, 'a') as dataframe:
            writer = csv.writer(dataframe)
            HEADER = ['Ticker','Index', 'MarketCap', 'Income', 'Sales', 'Booksh','Cashsh', 'Dividend',
                      'Dividend_Percentage', 'Employees','Recom', 'PriceToEarnings', 'ForwardPTE','PEG',
                      'PriceToSales', 'PriceToBook', 'PutCallRatio','PFCF', 'QuickRatio', 'CurrentRatio', 'DebtEquity','LdDebtEquity',
                      'SMA20','SMA50','SMA200','ROA', 'ROE', 'ROI', 'GrossMargin', 'OperationalMargin', 'ProfitMargin', 'Payout',
                      'SHSOutstanding', 'ShsFloat', 'ShoartFloat', 'ShortRatio', 'TargetPrice','52WH','52WL','AVGVol','Vol', 'PerformaceHalfYear',
                      'PerformanceYear', 'PerformanceYTD']
            writer.writerow(HEADER)
            for Ticker in csv_reader:
                try:
                    searchbox = driver.find_element_by_xpath('//*[@id="search"]/div/form/input')
                    searchbutton = driver.find_element_by_xpath('//*[@id="search"]/div/form/span')
                    searchbox.click()
                    searchbox.send_keys(Ticker)
                    searchbutton.click()
                    #driver.implicitly_wait(5)
                    #--- New Additions---
                    Index = driver.find_element_by_xpath('/html/body/div[4]/div/table[2]/tbody/tr[1]/td[2]/b').text
                    Cashsh = driver.find_element_by_xpath('/html/body/div[4]/div/table[2]/tbody/tr[6]/td[2]/b').text
                    Recom = driver.find_element_by_xpath('/html/body/div[4]/div/table[2]/tbody/tr[12]/td[2]/b').text
                    PEG = driver.find_element_by_xpath('/html/body/div[4]/div/table[2]/tbody/tr[3]/td[4]/b').text
                    PFCF = driver.find_element_by_xpath('/html/body/div[4]/div/table[2]/tbody/tr[7]/td[4]/b').text
                    LdDebtEquity = driver.find_element_by_xpath('/html/body/div[4]/div/table[2]/tbody/tr[11]/td[4]/b').text
                    SMA20 = driver.find_element_by_xpath('/html/body/div[4]/div/table[2]/tbody/tr[12]/td[4]/b').text
                    SMA50 = driver.find_element_by_xpath('/html/body/div[4]/div/table[2]/tbody/tr[12]/td[6]/b').text
                    SMA200 = driver.find_element_by_xpath('/html/body/div[4]/div/table[2]/tbody/tr[12]/td[8]/b').text
                    Wl52 = driver.find_element_by_xpath('/html/body/div[4]/div/table[2]/tbody/tr[8]/td[10]/b').text
                    Wh52 = driver.find_element_by_xpath('/html/body/div[4]/div/table[2]/tbody/tr[7]/td[10]/b').text
                    AvgVol = driver.find_element_by_xpath('/html/body/div[4]/div/table[2]/tbody/tr[11]/td[10]/b').text
                    Vol = driver.find_element_by_xpath('/html/body/div[4]/div/table[2]/tbody/tr[12]/td[10]/b').text
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
                    HEADER = ['Ticker','Index', 'MarketCap', 'Income', 'Sales', 'Booksh','Cashsh', 'Dividend',
                      'Dividend_Percentage', 'Employees','Recom', 'PriceToEarnings', 'ForwardPTE','PEG',
                      'PriceToSales', 'PriceToBook', 'PutCallRatio','PFCF', 'QuickRatio', 'CurrentRatio', 'DebtEquity','LdDebtEquity',
                      'SMA20','SMA50','SMA200','ROA', 'ROE', 'ROI', 'GrossMargin', 'OperationalMargin', 'ProfitMargin', 'Payout',
                      'SHSOutstanding', 'ShsFloat', 'ShoartFloat', 'ShortRatio', 'TargetPrice','52WH','52WL','AVGVol','Vol', 'PerformaceHalfYear',
                      'PerformanceYear', 'PerformanceYTD']
                    INSERT = [Ticker,Index, MarketCap, Income, Sales, Booksh,Cashsh, Dividend,
                      Dividend_Percentage, Employees,Recom, PriceToEarnings, ForwardPTE,PEG,
                      PriceToSales, PriceToBook, PutCallRatio,PFCF, QuickRatio, CurrentRatio, DebtEquity,LdDebtEquity,
                      SMA20,SMA50,SMA200,ROA, ROE, ROI, GrossMargin, OperationalMargin, ProfitMargin, Payout,
                      SHSOutstanding, ShsFloat, ShoartFloat, ShortRatio, TargetPrice,Wh52,Wl52,AvgVol,Vol, PerformaceHalfYear,
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
finVizEngine('Scripts\SnP1000_TICKR.csv','SnP1000_DATA.csv')


