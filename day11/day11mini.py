from bs4 import BeautifulSoup
import requests

import matplotlib.pyplot as plt
import pandas as pd
from collections import OrderedDict
import numpy as np

wiki = "https://en.wikipedia.org/wiki/List_of_states_and_union_territories_of_India_by_area"
source = requests.get(wiki).text


soup = BeautifulSoup(source,"lxml")

print (soup.prettify())

all_tables=soup.find_all('table')

print (all_tables)

right_table=soup.find('table', class_='wikitable')

print (right_table)
a=[]
b=[]

for i in right_table.findAll('tr'):
    cells= i.findAll('td')
    if len(cells)==7:
        a.append(cells[1].text.strip())
        b.append(cells[4].text.strip())
       
col_name = ["state","shares%"]
col_data = OrderedDict(zip(col_name,[a,b]))        
df = pd.DataFrame(col_data)        
print(df)
mod_df = df[0:6]
print(mod_df)

labels = np.array(["state"])
sizes = np.array(["share%"],dtype=float)
explode = (0.1,0,0,0,0,0)

plt.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%', shadow=True, startangle=0)

plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.show()












