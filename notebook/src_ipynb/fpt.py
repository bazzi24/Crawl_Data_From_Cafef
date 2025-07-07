#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests
import os
import csv
import openpyxl
from datetime import datetime
from bs4 import BeautifulSoup


# In[2]:


url = 'https://cafef.vn/du-lieu/hose/fpt-cong-ty-co-phan-fpt.chn'


# In[4]:


response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')


# In[5]:


# Name
artical = soup.find('div', id='symbolbox')
print(artical.text.strip() if artical else "Not found")
# Time
artical2 = soup.find('div', id='time__update')
print(artical2.text.strip() if artical2 else "Not found")
# Price
artical3 = soup.find('div', id='price__0')
print(artical3.text.strip() if artical3 else "Not found")
# (+/-)
artical4 = soup.find('div', id='price__ch')
print(artical4.text.strip() if artical4 else "Not found")
# Volume
artical5 = soup.find('div', id='price__vol')
print(artical5.text.strip() if artical5 else "Not found")
# Reference price
artical6 = soup.find('div', id='price__ref')
print(artical6.text.strip() if artical6 else "Not found")
# Price ceiling
artical7 = soup.find('div', id='price__ceiling')
print(artical7.text.strip() if artical7 else "Not found")
# Floor price
artical8 = soup.find('div', id='price__floor')
print(artical8.text.strip() if artical8 else "Not found")
# Opening price
artical9 = soup.find('div', id='price__open')
print(artical9.text.strip() if artical9 else "Not found")
# Highest price
artical10 = soup.find('div', id='price__high')
print(artical10.text.strip() if artical10 else "Not found")
# Lowest price
artical11 = soup.find('div', id='price__low')
print(artical11.text.strip() if artical11 else "Not found")
# Net trading volume
artical12 = soup.find('div', id='foregin__buyvol')
print(artical12.text.strip() if artical12 else "Not found")
# Purchase value
artical13 = soup.find('div', id='foregin__buyval')
print(artical13.text.strip() if artical13 else "Not found")
# Sale value
artical14 = soup.find('div', id='foregin__sellval')
print(artical14.text.strip() if artical14 else "Not found")
# Room remaining
artical15 = soup.find('div', id='foregin__room')
print(artical15.text.strip() if artical15 else "Not found")


# In[7]:


if response.status_code == 200:
    def get_text(selector):
        el = soup.select_one(selector)
        return el.text.strip() if el else ''

    crawl_time = datetime.now()

    data = [
        crawl_time,
        get_text('div#symbolbox'),
        get_text('div#time__update'),
        get_text('div#price__0'),
        get_text('div#price__ch'),
        get_text('div#price__vol'),
        get_text('div#price__ref'),
        get_text('div#price__ceiling'),
        get_text('div#price__floor'),
        get_text('div#price__open'),
        get_text('div#price__high'),
        get_text('div#price__low'),
        get_text('div#foregin__buyvol'),
        get_text('div#foregin__buyval'),
        get_text('div#foregin__sellval'),
        get_text('div#foregin__room')
    ]

    headers = ["Thời gian crawl dữ liệu", "Tên mã chứng khoán", "Cập nhật", "Giá kết thúc phiên", "Giá so với tham chiếu", 
               "Khối lượng", "Giá tham chiếu", "Giá trần", "Giá sàn", "Giá mở cửa", "Giá cao nhất", 
               "Giá thấp nhất", "KLGD ròng", "GT mua", "GT bán", "Room còn lại"]

    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(BASE_DIR, '..', 'file_csv', 'fpt_data.csv')
    file_exists = os.path.exists(file_path)

    with open(file_path, 'a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        if not file_exists:
            writer.writerow(headers)
        writer.writerow(data)
    print("Scraping data completed!")
else:
    print("Scraping data failed!")

