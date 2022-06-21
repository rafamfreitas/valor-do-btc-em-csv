from selenium import webdriver
import csv


# Mudar endereço do diretório onde geckodriver está localizado em seu computador.
driver = webdriver.Firefox(executable_path='/home/usr/.local/bin/geckodriver')
driver.get('https://finance.yahoo.com/quote/BTC-EUR/history/')


#Criação de uma tabela
tabela1 = driver.find_element_by_xpath('//td[@class="Py(10px) Ta(start) Pend(10px)"]')
fechamento1 = driver.find_element_by_xpath('//*[@id="Col1-1-HistoricalDataTable-Proxy"]/section/div[2]/table/tbody/tr[1]/td[5]')

tabela2 = driver.find_element_by_xpath('//*[@id="Col1-1-HistoricalDataTable-Proxy"]/section/div[2]/table/tbody/tr[2]/td[1]')
fechamento2 = driver.find_element_by_xpath('//*[@id="Col1-1-HistoricalDataTable-Proxy"]/section/div[2]/table/tbody/tr[2]/td[5]')

tabela3 = driver.find_element_by_xpath('//*[@id="Col1-1-HistoricalDataTable-Proxy"]/section/div[2]/table/tbody/tr[3]/td[1]')
fechamento3 = driver.find_element_by_xpath('//*[@id="Col1-1-HistoricalDataTable-Proxy"]/section/div[2]/table/tbody/tr[3]/td[5]')

tabela4 = driver.find_element_by_xpath('//*[@id="Col1-1-HistoricalDataTable-Proxy"]/section/div[2]/table/tbody/tr[4]/td[1]')
fechamento4 = driver.find_element_by_xpath('//*[@id="Col1-1-HistoricalDataTable-Proxy"]/section/div[2]/table/tbody/tr[4]/td[5]')

tabela5 = driver.find_element_by_xpath('//*[@id="Col1-1-HistoricalDataTable-Proxy"]/section/div[2]/table/tbody/tr[5]/td[1]')
fechamento5 = driver.find_element_by_xpath('//*[@id="Col1-1-HistoricalDataTable-Proxy"]/section/div[2]/table/tbody/tr[5]/td[5]')

tabela6 = driver.find_element_by_xpath('//*[@id="Col1-1-HistoricalDataTable-Proxy"]/section/div[2]/table/tbody/tr[6]/td[1]')
fechamento6 = driver.find_element_by_xpath('//*[@id="Col1-1-HistoricalDataTable-Proxy"]/section/div[2]/table/tbody/tr[6]/td[5]')

tabela7 = driver.find_element_by_xpath('//*[@id="Col1-1-HistoricalDataTable-Proxy"]/section/div[2]/table/tbody/tr[7]/td[1]')
fechamento7 = driver.find_element_by_xpath('//*[@id="Col1-1-HistoricalDataTable-Proxy"]/section/div[2]/table/tbody/tr[7]/td[5]')

tabela8 = driver.find_element_by_xpath('//*[@id="Col1-1-HistoricalDataTable-Proxy"]/section/div[2]/table/tbody/tr[8]/td[1]')
fechamento8 = driver.find_element_by_xpath('//*[@id="Col1-1-HistoricalDataTable-Proxy"]/section/div[2]/table/tbody/tr[8]/td[5]')

tabela9 = driver.find_element_by_xpath('//*[@id="Col1-1-HistoricalDataTable-Proxy"]/section/div[2]/table/tbody/tr[9]/td[1]')
fechamento9 = driver.find_element_by_xpath('//*[@id="Col1-1-HistoricalDataTable-Proxy"]/section/div[2]/table/tbody/tr[9]/td[5]')

tabela10 = driver.find_element_by_xpath('//*[@id="Col1-1-HistoricalDataTable-Proxy"]/section/div[2]/table/tbody/tr[10]/td[1]')
fechamento10 = driver.find_element_by_xpath('//*[@id="Col1-1-HistoricalDataTable-Proxy"]/section/div[2]/table/tbody/tr[10]/td[5]')


f = open('eur_btc_rates.csv', 'a', newline="")
tabelaMain = ('Date', 'BTC Closing Value')
t1 = (tabela1.text, fechamento1.text)
t2 = (tabela2.text, fechamento2.text)
t3 = (tabela3.text, fechamento3.text)
t4 = (tabela4.text, fechamento4.text)
t5 = (tabela5.text, fechamento5.text)
t6 = (tabela6.text, fechamento6.text)
t7 = (tabela7.text, fechamento7.text)
t8 = (tabela8.text, fechamento8.text)
t9 = (tabela9.text, fechamento9.text)
t10 = (tabela10.text, fechamento10.text)


writer = csv.writer(f)
writer.writerow(tabelaMain)
writer.writerow(t1)
writer.writerow(t2)
writer.writerow(t3)
writer.writerow(t4)
writer.writerow(t5)
writer.writerow(t6)
writer.writerow(t7)
writer.writerow(t8)
writer.writerow(t9)
writer.writerow(t10)

f.close()