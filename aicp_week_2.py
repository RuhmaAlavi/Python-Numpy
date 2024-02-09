# -*- coding: utf-8 -*-
"""AICP week 2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1SmHC16QH4Q73e0X1yN7LU7wAHM1vTxmZ
"""

import pandas as pd

"""Q1: Create a panda series without using dictionary"""

inde_x= ['a','x','c','2','e']

val=[1,4,9,6,7]

series= pd.Series(val,index=inde_x,dtype='int64')
print(series)

"""Q2) Create a series using dictionary"""

data = {'Bilal': 42,'Ayesha':28,'Hadia':39}
series = pd.Series(data,dtype='int64')
print(series)

"""Q3) Create a two dimentional dataframe of given information"""

day= pd.Series(["1/1/2017","1/2/2017","1/3/2017","1/4/2017","1/5/2017","1/6/2017"])
temp= pd.Series([32,35,28,24,22,21])
winsp = pd.Series([6,7,2,7,4,2])
event = pd.Series(["Rain","Sunny","Snow","Snow","Rain","Sunny"])
data = pd.DataFrame({"day":day,"temperature":temp,"wndspeed":winsp,"event":event})
data

"""
Q4) In extension to above question, you are required to replace index by ['a','b','c','d','e','f']"""

data2 = pd.DataFrame({"day": day, "temperature": temp, "wndspeed": winsp, "event": event}, index=['a', 'b', 'c', 'd', 'e', 'f'])
data2

"""Q5) Calculate mean, miximum and minimum for label “temperature"
"""

# Calculate mean, maximum, and minimum temperature
mean_t = data['temperature'].mean()
max_t = data['temperature'].max()
min_t = data['temperature'].min()

print("Mean temperature:", mean_t)
print("Maximum temperature:", max_t)
print("Minimum temperature:", min_t)

"""Q6) Import CSV ‘people.csv’ in the given folder"""

file = pd.read_csv('people.csv',usecols = ["First Name","Sex","Email","Phone","Job Title"],index_col = ["Sex","Job Title"],skiprows = [1,5])

file.to_csv('NewPeople.csv')

file

"""Q7) Import excel sheet ‘SampleWork.xlsx’ in the given folder"""

data = pd.read_excel('SampleWork.xlsx', sheet_name='Sheet1', usecols=[0, -1], skiprows=[1], header=1)
data.to_excel('NewSheet.xlsx', index=False)
data

"""Q8) : Create the following dataframe as AICP_DF then implement different operations as described below:"""

data = {
    'Name': ['Sonia', 'Bilal', 'Hifza', 'Kabir', 'Jazim'],
    'Age': [27, 24, 22, 32, 23],
    'Address': ['Lahore', 'Karachi', 'Sialkot', 'Peshawar', 'lhr'],
    'Qualification': ['MsC', 'MA', 'MCA', 'Phd', 'bsc'],
}

AICP_DF = pd.DataFrame(data)
AICP_DF

"""select 'Name', 'Qualification' coloumns and save to df1"""

df1 = AICP_DF[['Name', 'Qualification']].copy()
df1

"""add a new column to AICP_DF “Height” with the following values: [5.1, 6.2, 5.1, 5.2,5.1]"""

AICP_DF['Height'] = [5.1, 6.2, 5.1, 5.2, 5.1]
AICP_DF

"""set column “Name” as the index column"""

AICP_DF.set_index('Name', inplace=True)
AICP_DF

"""retrieve row with index “Hifza”"""

row_hifza = AICP_DF.loc['Hifza']
row_hifza

"""retrieve row with index 3"""

row_three = AICP_DF.iloc[2]
row_three

"""drop row with index “Bilal”"""

AICP_DF.drop('Bilal', inplace=True)
AICP_DF