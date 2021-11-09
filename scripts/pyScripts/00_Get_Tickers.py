import csv
from selenium import webdriver
from bs4 import BeautifulSoup
import requests
import pandas as pd
import re
driver = webdriver.Chrome()
url1 = 'https://en.wikipedia.org/wiki/List_of_S%26P_600_companies'
url2 = 'https://en.wikipedia.org/wiki/List_of_S%26P_400_companies'
def clean(string):
    string = string.replace('<td>','')
    string = string.replace('</td>','')
    string = string.replace('<', '')
    string = string.replace('>', '')

    #string = string.replace('/', '')
    #string = string.strip()
    return string

def get_SNP1000(url1,url2):
    html_content = requests.get(url1).text
    soup = BeautifulSoup(html_content, "html.parser")
    table00 = soup.find(id = 'constituents')
    table01 = table00.findAll('td')
    table02 = []

    html_content2 = requests.get(url2).text
    soup2 = BeautifulSoup(html_content2, "html.parser")
    table10 = soup2.find(id = 'constituents')
    table11 = table10.findAll('td')
    print(len(table01))
    print(len(table11))
    for i in range(0,600):
        a = clean(str(table01[   (1)+5*i +i ]))
        a = a[a.rfind('"'):-1].replace('/', '').replace('"', '')
        a = a[:-1]
        table02.append([  clean(str(table01[   (0)+5*i +i ])),
                          a,
                          clean(str(table01[   (2)+5*i +i ])),
                          clean(str(table01[   (3) + 5 * i + i])),
                          clean(str(table01[   (4)+5*i +i ])),
                          clean(str(table01[   (5)+5*i +i ])),
                          'S&P600'
                          ])
    print('0-----' + str(table11[0]))
    print('1-----' + str(table11[1]))
    print('2-----' + str(table11[2]))
    print('3-----' + str(table11[3]))
    print('4 ----' + str(table11[4]))
    print('5 -----' + str(table11[5]))
    print('6 -----' + str(table11[6]))
    print('7 ----' + str(table11[7]))
    print('8 ----' + str(table11[8]))
    print('9 -----'+ str(table11[9]))
    print('10 ----' + str(table11[10]))
    for i in range(0,399):
        a = clean(str(table11[   (1)+5*i]))
        a = a[a.rfind('"'):-1].replace('/', '').replace('"', '')
        table02.append([clean(str(table11[   (0)+5*i ])),
                        a,
                        clean(str(table11[   (2)+5*i ])),
                        clean(str(table11[   (3)+5*i ])),
                        clean(str(table11[   (4)+5*i ])),
                        '',
                        'S&P400'])
    #pd.options.display.max_rows
    data = pd.DataFrame(table02)
    data.to_csv('SnP1000.csv', index=False)

get_SNP1000(url1,url2)
