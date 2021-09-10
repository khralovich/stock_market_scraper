#!/usr/bin/env python
# coding: utf-8

get_ipython().system('pip install pandas requests BeautifulSoup4 selenium')
import pandas as pd
import requests
from bs4 import BeautifulSoup as bs
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

url = "https://www.gpw.pl/akcje"

company_name = input('Wpisz nazwę indeksu WIG20 używając dużych liter (np. ALLEGRO, CCC, LPP, LOTOS, PEKAO, JSW): ')

# ten kod używa Chrome webdriver'a, zmień ścieżkę do niego na swoją
# jeśli nie masz tego drivera, ściągnij tutaj: https://sites.google.com/a/chromium.org/chromedriver/downloads

path = "/usr/bin/chromedriver"  

driver = webdriver.Chrome(path)
driver.get(url) 
time.sleep(5) 
html = driver.page_source

# dodaję to żeby obejść 'requests.exceptions.SSLError - dh key too small'

requests.packages.urllib3.util.ssl_.DEFAULT_CIPHERS += 'HIGH:!DH:!aNULL'
try:
    requests.packages.urllib3.contrib.pyopenssl.DEFAULT_SSL_CIPHER_LIST += 'HIGH:!DH:!aNULL'
except AttributeError:
    
    pass

response = requests.get(url, verify=False)

soup = bs(html, "html.parser")
table = soup.findAll("tr",attrs={"class","trclass"})

def iteracja(spolka):
    wynik = "nie znaleziono"
    for index in range(len(table)):
        if table[index].get_text(separator=" ").strip().split(" ")[0] == spolka:
            wynik = index
    return wynik

           
i = iteracja(company_name)

kursOdn = int(table[i].get_text(separator=" ").strip().split(" ")[4].replace(",", ''))

wolObr = int(table[i].get_text(separator=" ").split(" ")[-2].encode('unicode_escape').decode().replace("\\xa0", ''))

