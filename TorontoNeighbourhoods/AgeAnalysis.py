import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

nb_2016 = pd.read_csv('neighbourhood-profiles-2016-csv.csv')
print(nb_2016.head(3))

print(nb_2016.columns.values)

print(nb_2016['Category'].unique())

# Create new tables for each Category with name of 'nb2016_Category'
tableName = []
for i in nb_2016['Category'].unique():
    j = i.title().replace(', ', '').replace(' ', '')
    tableName.append('nb2016_' + j)
    globals()['nb2016_' + j] = nb_2016[nb_2016['Category'] == i]
print(tableName)


# Create subset of Population
print(nb2016_Population['Topic'].unique())

nb2016Age = nb2016_Population[nb2016_Population['Topic'] == 'Age characteristics'].iloc[:, 4:]

# Convert string to int
for i in nb2016Age.iloc[:, 1:].columns:
    nb2016Age[i] = nb2016Age[i].str.replace(',', '').astype('int')


# Analyze with age segments
nb2016AgeSeg = nb2016Age[:6]

# Plot horizontal bar by age segments
plt.barh(nb2016AgeSeg['Characteristic'], nb2016AgeSeg['City of Toronto'])
plt.xlabel('Population')
plt.show()

# Analyze with age and gender segments
nb2016AgeGender = nb2016Age[6:]
print(nb2016AgeGender.info())

nb2016Female = nb2016AgeGender[nb2016AgeGender['Characteristic'].str.find('Female') == 0]

nb2016Male = nb2016AgeGender[nb2016AgeGender['Characteristic'].str.find('Female') == -1]

nb2016Female['Age'] = nb2016Female['Characteristic'].str[8:]
nb2016Male['Age'] = nb2016Male['Characteristic'].str[6:]

nb2016FM = pd.merge(nb2016Female, nb2016Male, how='inner', on='Age', suffixes=('_f', '_m'))
nb2016FM['Ages'] = nb2016FM['Age'].str.split().str.get(0).astype('int')

nb2016FM = nb2016FM.sort_values(['Ages'])

X = nb2016FM['Age']
plt.barh(X, nb2016FM['City of Toronto_f'])
plt.barh(X, -nb2016FM['City of Toronto_m'])
plt.title('City of Toronto')
plt.xlabel('Male                  Female')
plt.show()

X = nb2016FM['Age']
plt.barh(X, nb2016FM['Agincourt North_f'])
plt.barh(X, -nb2016FM['Agincourt North_m'])
plt.title('Agincourt North')
plt.xlabel('Male                  Female')
plt.show()




