# -*- coding: utf-8 -*-
"""
Created on Sun Jun 25 18:02:00 2023

@author: himan
"""

import pandas as pd

data= pd.read_csv('transaction.csv')


data =pd.read_csv('transaction.csv',sep=';')

#working with calculations

# Defining Variables

costperitem = 11.27
SellingPricePerItem = 21.11
NumberOfItemsPurchased = 6

ProfitPerItem= costperitem  - SellingPricePerItem

ProfitPerTransaction= NumberOfItemsPurchased* ProfitPerItem
CostPerTransaction=NumberOfItemsPurchased*costperitem
SellingPricePerTransaction= NumberOfItemsPurchased*SellingPricePerItem

 # Adding a new Column to dataframe
data['CostPerTransaction'] = data['CostPerItem']*data['NumberOfItemsPurchased']

 # Sales Per Transaction
 
data['SalesPerTransaction'] = data['SellingPricePerItem']*data['NumberOfItemsPurchased']
 
 #Profit Calculation  = Sales -Cost
 
data['ProfitPerTransaction'] = data['SalesPerTransaction']-data['CostPerTransaction']
 
 #MArkup = (sales -cost)/cost

data['Markup'] =(data['SalesPerTransaction']-data['CostPerTransaction'])/data['CostPerTransaction']


data ['ItemDescription'] = data ['ItemDescription'].str.lower()
 
# Rounding Markup
data['Markup'] = round(data['Markup'] ,3)

#Checking datacolumn datatype
print(data['Day'].dtype)

#change column type 

day =data['Day'].astype(str)

print(day.dtype)

 
# Concatenating columns 

data['Date'] = data['Day'].astype(str)+'-'+ data['Month'].astype(str)+'-'+data['Year'].astype(str)


data.iloc[0] # views the row with index =0
data.iloc[0:3]

data.iloc[-5:]

data.head(5) # bydefault get first 5 rows data.head()

data.iloc[:,3] # bring all rows in 3rd column

data.iloc[4,2] # get 4th row and 2nd column data 

#Using split  to split the client keywords
#new_var = column.str.split('sep', expand=True)

split_col = data['ClientKeywords'].str.split(',',expand=True)

#creating new columns for aplit column in ClientKeyword

data['ClientAge'] =split_col[0]
data['ClientTypes'] =split_col[1] 
data['LengthOfContract']=split_col[2]

#replac function


data['ClientAge'] =  data['ClientAge'].str.replace('[','')
data['LengthOfContract'] =  data['LengthOfContract'].str.replace(']','')


# How to Merge Files 

# bringing in a new dataset
seasons = pd.read_csv('value_inc_seasons.csv', sep=';')

# merging files : merge_df = pd.merge (old_df,new_df, on =key)

data = pd.merge(data,seasons,on ='Month')


# dropping columns

# df = df.drop('columnname', axis=1)

data = data.drop('ClientKeywords', axis=1)
data = data.drop(['Year','Month'], axis=1)
data = data.drop('Day', axis=1)

#export to CSV

data.to_csv('ValueInc_Cleaned.csv',index=False)











