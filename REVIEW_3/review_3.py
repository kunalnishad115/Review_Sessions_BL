import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df=pd.read_csv('REVIEW_3/country_wise_latest.csv')
print(df)

# Create NumPy arrays using COVID confirmed cases data.
# ● Perform:
# ○ Mean
# ○ Sum
# ○ Max
# ○ Min
# ○ Reshaping
# ○ Slicing
# ○ Broadcasting

array=df['Confirmed'].values
print("Confirmed array:", array)

print("Mean of Array:",np.mean(array))

print("Sum of array:",np.sum(array))

print("Max of Array:",np.max(array))

print("Min of Array:",np.min(array))

print(np.size(array))

# print(df['Confirmed'].count())

print("Reshape the array:",array.reshape(1,-1))

print("Slicing the array:",array[0:10])

print("Broadcasting the array:",array+1000)



print(df.info())
print(df.head())
print(df.tail())

# Data types
# ○ Null values
# ○ Duplicate values

print("total null values: ",df.isnull().sum())
print("total dulicate values: ",df.duplicated().sum())

# Handle missing values.
# ● Remove duplicate rows.
# ● Replace invalid values like:
# ○ inf
# ○ null
# ○ 0 where necessary

print("Drop The dulicate Values:",df.drop_duplicates())
print("Replace the null Values:",df.fillna(0))

print(df)

# ● Total confirmed cases
# ● Total deaths
# ● Total recovered cases
# ● WHO region wise analysis
# ● Highest active cases
# ● Top 10 affected regions
# Use:
# ● groupby()
# ● sorting
# ● filtering
# ● aggregation functions

print(df.columns)

# Index(['Country/Region', 'Confirmed', 'Deaths', 'Recovered', 'Active',
#        'New cases', 'New deaths', 'New recovered', 'Deaths / 100 Cases',
#        'Recovered / 100 Cases', 'Deaths / 100 Recovered',
#        'Confirmed last week', '1 week change', '1 week % increase',
#        'WHO Region'],
#       dtype='object')

total_cofirmed_case=df['Confirmed'].sum()
print("Total confirmed cases:",total_cofirmed_case)

total_deaths=df['Deaths'].sum()
print("TOTAL Deaths: ",total_deaths)

total_recover_cases=df['Recovered'].sum()
print("Total Recover Cases: ",total_recover_cases)

who_region_analysis=df.groupby('WHO Region')['Confirmed'].sum()
print(who_region_analysis)

high_active_case=df.sort_values(by='Active',ascending=False).head(1)
print(high_active_case)

top_affected=df.sort_values(by='Confirmed',ascending=False).head(10)
print(top_affected)


# Line graph for confirmed cases

# ● Bar chart for WHO region wise deaths
# ● Histogram for active cases
# ● Pie chart for recovered cases by region ---> 
# ● Scatter plot between confirmed and deaths
# ● Heatmap for correlation analysis -->  




sns.lineplot(x=df['Confirmed'],y=df['Deaths'])
plt.show()

sns.barplot(x=df['WHO Region'],y=df['Deaths'])
plt.show()

sns.histplot(x=df['Active'])
plt.show()

sns.pie(df.groupby('WHO Region')).plot.pie(y='Recovered',autopct='%1.1f%%')
plt.show()

sns.scatterplot(x=df['Confirmed'],y=df['Deaths'])
plt.show()

