import numpy as np
import pandas as pd

df= pd.read_csv('laptops.csv')
# print(df.head()) #.head start k 5 columns show krwata or () k andr number pass krdo tw wo utnoi colmns show krwata

# print(df)
# print(df.Brand)

# #built in properties of data frames
# print(df.shape)  #total rows and columns 
# print(df.dtypes) #types btata h 
# print(df.columns) #total columns
# print(df.values) #

#methods
# print(df.info())
# print(df.describe())
# print(df.head(6))
# print(df.tail())  #last k 5 show krwata 

# print(df.sample(5))
# print(df.isnull().sum())
# print(df.duplicated().sum())

# print(df.head(1))
# df.loc[0,'Brand']='HP'  #loc means location
# df.loc[0, 'GPU'] = 3
# print(df.head(1))

# #single col
# print(df[['Brand']].head(1))
# #multiple cols
# print(df[['Brand','GPU','Laptop']].head(1))

# #column renaming
# df.rename(columns={'Brand' : 'Brands'},inplace=True)
# print(df)

hp_laptops = df['Brands'] == 'HP'
print(hp_laptops)

print(df.iloc[1]) #iloc means index location
print(df[0:5])

#start , end, steps
print(df[0:5:3])
print(df[2:15:2])
