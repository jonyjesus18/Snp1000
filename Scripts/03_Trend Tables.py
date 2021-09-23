import shutil 
from selenium import webdriver
import chromedriver_autoinstaller


def move_download(TICKER):
    source = f'C:/Users/joaom/Downloads/{TICKER}.csv'
    destination = 'C:/Users/joaom/OneDrive/Documentos/GitHub/Snp1000/Performance Tables'
    dest = shutil.move(source, destination) 

'''
with open(input, 'r') as IPO_List:
        csv_reader = reader(IPO_List)
'''


yahoo = 'https://finance.yahoo.com/quote/AAPL?p=AAPL&.tsrc=fin-srch'
driver = webdriver.Chrome(executable_path = r"C:\Users\joaom\OneDrive\Documentos\GitHub\Snp1000\Scripts\chromedriver.exe")
chromedriver_autoinstaller.install()
driver.get(yahoo)
init_button = driver.find_element_by_id('/html/body/div/div/div/div/form/div[2]/div[2]/button')
print('---------------')
print(init_button)
print('---------------')
init_button.click()
driver.implicitly_wait(5)
finantials_button = driver.find_element_by_xpath('//*[@id="quote-nav"]/ul/li[5]/a')
download_button = driver.find_element_by_xpath('//*[@id="Col1-1-HistoricalDataTable-Proxy"]/section/div[1]/div[2]/span[2]/a')
finantials_button.click()
download_button.click()









