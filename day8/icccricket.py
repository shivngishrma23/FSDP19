
from bs4 import BeautifulSoup as bs
import requests


icc= "https://www.icc-cricket.com/rankings/mens/team-rankings/odi"
source = requests.get(icc).text
soup= bs(source,"lxml")
print(soup.prettify())
all_tables=soup.find_all('table')

print (all_tables)

right_table=soup.find('table', class_='table')

print (right_table)

a=[]
b=[]
c=[]
d=[]


for row in right_table.findAll('tr'):
    cells = row.findAll('td')
    
     
    if len(cells) == 5:
         a.append(cells[1].text.strip())
         b.append(cells[2].text.strip())
         c.append(cells[3].text.strip())
         d.append(cells[4].text.strip())
         
import pandas as pd
from collections import OrderedDict

col_name = ["country","matches","points","ratings"]
col_data = OrderedDict(zip(col_name,[a,b,c,d]))
df = pd.DataFrame(col_data) 
df.to_csv("my.csv")
