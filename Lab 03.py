import pandas as pd
#Series one-dimentional array
#Data frame: a type of a relation that has both rows and column

df = pd.read_csv('weather.csv')
print(type(df))
print(df)

#&&%
#First five records
print(df.head())

#&&%
#Last five records
print(df.tail())

#&&%
#description od the dat
print(df.head())



