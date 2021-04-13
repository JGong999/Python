import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import numpy.polynomial.polynomial as pl
from sklearn.metrics import r2_score

nb_2016 = pd.read_csv('neighbourhood-profiles-2016-csv.csv')
nb_2016.head(3)

# Create new tables for each Category with name of 'nb2016_Category'
tableName = []
for i in nb_2016['Category'].unique():
    j = i.title().replace(', ', '').replace(' ', '')
    tableName.append('nb2016_' + j)
    globals()['nb2016_' + j] = nb_2016[nb_2016['Category'] == i]

# Create new column names
ColName = {}
n=2
for i in nb2016_Population['Characteristic'][0:7]:
    j = i.title().replace(', ', '').replace(' ', '').replace('-', '')
    ColName[n] = j
    n = n + 1

# Rename column name
nb2016Pop = nb2016_Population[0:7].iloc[:, 5:].transpose().rename(columns=ColName)

print(nb2016Pop.columns.values)

print(nb2016Pop.dtypes)

# Converting string to int and float
for i in nb2016Pop.columns:
    if i == 'PopulationChange20112016':
        nb2016Pop[i] = nb2016Pop[i].str.replace('%', '').astype(float) / 100
    elif i == 'LandAreaInSquareKilometres':
        nb2016Pop[i] = nb2016Pop[i].str.replace(',', '').astype(float)
    else: 
        nb2016Pop[i] = nb2016Pop[i].str.replace(',', '').astype(int)

# Checking data types
nb2016Pop.dtypes

for i in nb2016Pop.columns:
    j = nb2016Pop[nb2016Pop[i].isna()==True].index
    print(i, j)

print(nb2016Pop.corr())

nb2016Pop['dw_pop'] = nb2016Pop['TotalPrivateDwellings'] / nb2016Pop['Population2016']
plt.scatter(nb2016Pop['dw_pop'], nb2016Pop['PopulationChange20112016'])
plt.show()

# Set train and test

# train = nb2016Pop.sample(frac=0.8)
train = nb2016Pop[:113]
# test = pd.concat([nb2016Pop, train]).drop_duplicates(keep=False)
test = nb2016Pop[113:]
# print(train.info())
# print(test.info())

# Build polinomial model
model = pl.Polynomial(pl.polyfit(train['dw_pop'], train['PopulationChange20112016'], 2))
print(model)


myline = np.linspace(min(nb2016Pop['dw_pop']), max(nb2016Pop['dw_pop']), 141)
plt.scatter(train['dw_pop'], train['PopulationChange20112016'])
plt.plot(myline, model(myline))
plt.show()

r2 = r2_score(test['PopulationChange20112016'], model(test['dw_pop']) )
print('r-square = ', r2)

