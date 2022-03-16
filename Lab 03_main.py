#%%
import pandas as pd
#Series one-dimentional array
#Data frame: a type of a relation that has both rows and column

df = pd.read_csv('weather.csv')
print(type(df))
print(df)

#%%
#First five records
print(df.head())

#%%
#Last five records
print(df.tail())

#%%
#description od the dataset
print(df.describe())

#%%
df.columns = ['outlook','temperature','humidity','windy','play']

#Series can not use multiple column

t = df['temperature']
print(type(t))
print(t)

#%%
sum = 0
for value in t:
    sum = sum+value
print(sum)

#%% can use multiple column

df1 = df[['temperature','humidity']]
print(df1)

#%%&

df2 = df.loc[0:9,['temperature','humidity']]
print(df2)

#%%
df3 = df.iloc[0:10,[1,2]]
print((df3))

#%% 1::2 1 theke 2 kore barbe like 1 3 5. jump parameter
df4 = df.iloc[1::2,[0,1,3]]
print((df4))

#%% data frame

print('Mean: ', df[['temperature']].mean())

#%% series 

print('Mean: ', df['temperature'].mean())

#%% all statistical measures over temperature column

temperature = df[['temperature']]
print("Mean: ", temperature.mean())
print("Standard Deviation: ", temperature.std())

#%%

df.hist(column='tempareture', bins = 5 )
#%%
df.hist(column = 'humidity', bins = 7)

#%%

humidity = df[['humidity']]
print("Mean: " , humidity.mean())

#%%

list1 = [[1,1], [1,2],[2,3],[2,3], [2,4],
         [2,4],[3,4],[3,4],[4,5],[5,5]]
print(list1)
#%%

df_list1 = pd.DataFrame(list1, columns = ['x','y'])
print(df_list1)

#%%

df_list1.hist(column = ['x'], bins =5)
#%%

print('Skew: ', df_list1[['x']].skew())
#%%

df_list1.hist(column = ['y'], bins = 5)
#%%

print('Skew: ', df_list1[['y']].skew())

#%%
print('Kurt - X: ', df_list1[['x']].kurt())
print('Kurt - Y: ', df_list1[['y']].kurt())
