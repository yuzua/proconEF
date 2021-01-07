!pip install beautifulsoup4
!pip install lxml
!pip install requests

from bs4 import BeautifulSoup
import requests
import pandas as pd
from pandas import  Series, DataFrame
#car_name取得
url = 'http://www.carsensorlab.net/car/LGS0095024205VU312943791700.html'
result = requests.get(url)
c = result.content
soup = BeautifulSoup(c,'lxml')
summry = soup.find('div',{'id':'box4'})
summary = summry.find('div',{'id':'clmain'})
data1 = summary.find_all('span')
data2 = summary.find_all('a')
datax1 = []

for span in data1:
  dataxxx = span.find(text=True)
  print(dataxxx)
  datax1.append(dataxxx.replace('：',' '))
datax2 = []

for span in data2:
  dataxxx = span.find(text=True)
  print(dataxxx)
  datax2.append(dataxxx)

datax1 = pd.Series(datax1)
datax2 = pd.Series(datax2)
name_df = pd.concat([datax1,datax2],axis=1)

#table1
tables1 = summry.find_all('table',{'class':'tbl1'})

data1 = []
data2 = []

rows = tables1[0].find_all('tr')

for tr in rows:
  colos = tr.find_all('th')
  for th in colos:
    text = th.find(text=True)
    print(text)
    data1.append(text)

for tr in rows:
  colos = tr.find_all('td')
  for td in colos:
    text = td.find(text=True)
    print(text)
    data2.append(text)

datax1 = pd.Series(data1)
datax2 = pd.Series(data2)
table1_df = pd.concat([datax1,datax2],axis=1)

#table3(◯×なしvar)
tables3 = summry.find_all('table',{'class':'tbl3'})
rows = tables3[0].find_all('tr')
for tr in rows:
  colos = tr.find_all('th')
  for th in colos:
    jadge = th.find('a')
    if not jadge:
      text = th.find(text=True)
    else:
      text = th.find(text=True)
      text2 = jadge.find(text=True)
      if text == text2:
        pass
      else:
        text = text + text2
    print(text)
    table3.append(text)
    text = ""
    sample = ""
    jadge = ""

#table4(◯×なしvar)
tables3 = summry.find_all('table',{'class':'tbl3'})
rows = tables3[1].find_all('tr')
for tr in rows:
  colos = tr.find_all('th')
  for th in colos:
    jadge = th.find('a')
    if not jadge:
      text = th.find(text=True)
    else:
      text = th.find(text=True)
      text2 = jadge.find(text=True)
      if text == text2:
        pass
      else:
        text = text + text2
    print(text)
    table4.append(text)
    text = ""
    sample = ""
    jadge = ""

#photo_data
summry = soup.find('div',{'id':'box4'})
photo_html = summry.find_all('div',{'id':'climg'})
rows = photo_html[0].find_all('img')

photo = []
for i in rows:
  a = i.get('src')
  photo.append(a)