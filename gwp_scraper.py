#!/usr/bin/env python
# coding: utf-8

# In[10]:


get_ipython().system('pip install pandas requests BeautifulSoup4 selenium')


# In[11]:


import pandas as pd
import requests
from bs4 import BeautifulSoup as bs


# In[12]:


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


# In[13]:


url = "https://www.gpw.pl/akcje"


# In[100]:


company_name = input('Wpisz nazwę indeksu WIG20 używając dużych liter (np. ALLEGRO, CCC, LPP, LOTOS, PEKAO, JSW): ')


# In[124]:


# ten kod używa Chrome webdriver'a, zmień ścieżkę do niego na swoją
# jeśli nie masz tego drivera, ściągnij tutaj: https://sites.google.com/a/chromium.org/chromedriver/downloads

path = "/usr/bin/chromedriver"  


# In[17]:


driver = webdriver.Chrome(path)
driver.get(url) 
time.sleep(5) 
html = driver.page_source


# In[18]:


# dodaję to żeby obejść 'requests.exceptions.SSLError - dh key too small'

requests.packages.urllib3.util.ssl_.DEFAULT_CIPHERS += 'HIGH:!DH:!aNULL'
try:
    requests.packages.urllib3.contrib.pyopenssl.DEFAULT_SSL_CIPHER_LIST += 'HIGH:!DH:!aNULL'
except AttributeError:
    
    pass

response = requests.get(url, verify=False)


# In[19]:


soup = bs(html, "html.parser")


# In[20]:


table = soup.findAll("tr",attrs={"class","trclass"})


# In[ ]:


#podaj nazwe spolki
#zwroc cala liste i index w table


# In[101]:


def iteracja(spolka):
    wynik = "nie znaleziono"
    for index in range(len(table)):
        if table[index].get_text(separator=" ").strip().split(" ")[0] == spolka:
            wynik = index
    return wynik

            


# In[102]:


i = iteracja(company_name)


# In[119]:


kursOdn = int(table[i].get_text(separator=" ").strip().split(" ")[4].replace(",", ''))


# In[120]:


kursOdn


# In[118]:


wolObr = int(table[i].get_text(separator=" ").split(" ")[-2].encode('unicode_escape').decode().replace("\\xa0", ''))


# In[121]:


wolObr

