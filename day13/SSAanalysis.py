import pandas as pd
df = pd.DataFrame()
import matplotlib.pyplot as plt
import numpy as np

for i in range (1880,2010):
    with open('yob'+str(i)+'.txt','rt') as files:
        df1= pd.read_csv(files,header=None)
        df1.columns = ['Name','gender','noOFnames']
        df1['year']= i
        df = pd.concat([df,df1])
   
## top 5 male and female baby_names in 2010
        
male = df['Name'][(df['gender']=="M") & (df['year'] == 2009)]        
male.head().values

female = df['Name'][(df['gender']=="F") & (df['year'] == 2009)]
female.head().values

##sum of births
pv = pd.pivot_table(df,index=['gender','year'],aggfunc=np.sum)

pv = pv.iloc[:10,:]
pv.plot.bar()