#!/usr/bin/env python
# coding: utf-8

# ### Data from
# https://open.toronto.ca/dataset/neighbourhood-profiles/

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


nb_2016 = pd.read_csv(r'https://raw.githubusercontent.com/JGong999/Python/main/TorontoNeighbourhoods/neighbourhood-profiles-2016-csv.csv')
print(nb_2016)


# Viewing/Inspecting Data
print(nb_2016.info())

# pd.set_option("max_rows", None)
# # pd.set_option("max_rows", 6)
# print(nb_2016['Characteristic'])

print(nb_2016.columns)

print(nb_2016['Category'].unique())

# Creating Subset

# To get population in 2016, 2011
pop_2016_2011 = nb_2016[nb_2016['Characteristic'].isin(['Population, 2016', 'Population, 2011', 'Population Change 2011-2016'])]
pop_2016_2011 = pop_2016_2011.transpose()[5:].reset_index()
map = {'index':'areaName', 2:'pop2016', 3: 'pop2011', 4:'delta11_16'}
pop_2016_2011.rename(columns=map, inplace=True)
pop_2016_2011['pop2016'] = pop_2016_2011['pop2016'].str.replace(',', '').astype(int)
pop_2016_2011['pop2011'] = pop_2016_2011['pop2011'].str.replace(',', '').astype(int)
pop_2016_2011['delta11_16'] = pop_2016_2011['delta11_16'].str.replace('%', '').astype(float) / 100
print(pop_2016_2011)


# Top 5 population decreasing neibourhoods
pop1611D = pop_2016_2011.sort_values('delta11_16').head(5)
print(pop1611D)

# Top 5 population increasing neibourhoods
pop1611I = pop_2016_2011.sort_values('delta11_16', ascending=False).head(5)
print(pop1611I)


# Graphs

# Bar chart for top 5 population increasing/decreasing neibourhoods
plt.bar(pop1611I['areaName'], pop1611I['pop2016'], label='Increasing')

plt.xticks(rotation='vertical')
plt.xlabel('Community Name')
plt.ylabel('Population')
plt.title('Top 5 Population Increasing Communities \n Toronto, Ontario, Canada 2016')

plt.bar(pop1611D['areaName'], pop1611D['pop2016'], label='Decreasing')

plt.title('Top 5 Population Increasing/Decreasing Neibourhoods \n in Toronto between 2011 and 2016')

plt.legend(loc='upper right')

plt.show()


# Top 5 population increasing neibourhoods

# Stacked bar graph
width = 0.35

plt.bar(pop1611I['areaName'], pop1611I['pop2016'], width, label='2016')
plt.bar(pop1611I['areaName'], pop1611I['pop2011'], width, label='2011')

plt.xticks(rotation='vertical')
plt.xlabel('Community Name')
plt.ylabel('Population')
plt.title('Top 5 Population Increasing Neibourhoods \n in Toronto between 2011 and 2016')

plt.legend(loc='upper right')

plt.show()

# Grouped bar chart
pop1611I[['pop2011','pop2016']].plot.bar()
plt.xticks(np.arange(len(pop1611I)), pop1611I['areaName'], rotation='vertical')
plt.xlabel('Community Name')
plt.ylabel('Population')
plt.title('Top 5 Population Increasing Neibourhoods \n in Toronto between 2011 and 2016')

plt.legend(loc='upper right')

plt.show()

# Top 5 population decreasing neibourhoods

# Stacked bar graph
width = 0.35

plt.bar(pop1611D['areaName'], pop1611D['pop2011'], width, label='2011')
plt.bar(pop1611D['areaName'], pop1611D['pop2016'], width, label='2016')

plt.xticks(rotation='vertical')
plt.xlabel('Community Name')
plt.ylabel('Population')
plt.title('Top 5 Population Decreasing Neibourhoods \n in Toronto between 2011 and 2016')

plt.legend(loc='upper right')

plt.show()

# Grouped bar chart
pop1611D[['pop2011','pop2016']].plot.bar()
plt.xticks(np.arange(len(pop1611D)), pop1611D['areaName'], rotation='vertical')
plt.xlabel('Community Name')
plt.ylabel('Population')
plt.title('Top 5 Population Decreasing Neibourhoods \n in Toronto between 2011 and 2016')

plt.legend(loc='upper left')

plt.show()





