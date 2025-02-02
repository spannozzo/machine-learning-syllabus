# -*- coding: utf-8 -*-
"""numpy_pandas_exercises_with_solutions.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1-oznL4nwwACaUP8Iii3CiEpDCi_OphsG

### This notebook contains solutions for practice exercises for Part 1 of Python libraries: 
#### 1) Numpy
#### 2) Pandas

# Numpy
"""

# Import Numpy
import numpy as np

"""#### Exercise 1: Create an array of 64 values starting with 10 and ending with 15 and assign it to x

#### **Remember**: The third parameter to linspace is the number of values to obtain from the real line interval starting from 10 to 15 in this case.
"""

# Exercise 1 solution:
x = np.linspace(10,15,64)
x

"""#### Exercise 2: Reshape x into a 3-Dimensional Array"""

# Exercise 2 solution:

# Find the shape of x
print(x.shape)

# Do reshaping to a 3 D array
x = x.reshape(4,4,4)

# Print the new shape
print(x.shape)

"""
#### Exercise 3: Get the slice with first row of x (Numpy array slicing) """

# Exercise 3 solution

# First row
print(x[:1,])

# Second row
print(x[1,])

# First 2 rows
print(x[:2,])

"""# Pandas

##### Note: Basics can be found [link here](https://colab.research.google.com/drive/1qm3w99JlIe7wOJikRrb37kJMJYDyqqCR)

#### Loading libraries and dataset
"""

import pandas as pd

# Loading the titanic dataset from internet
df = pd.read_csv("https://raw.githubusercontent.com/mwaskom/seaborn-data/master/titanic.csv") 

print(df)

"""## Practice section 1: Knowing your data

#### Exercise 1: Getting the first 10 rows of the dataset
"""

#Solution
df.head(10)

"""#### Exercise 2: What is the number of observations in the dataset ?"""

print(df.shape[0])
df.info()

"""#### Exercise 3: What is the number of columns in the dataset?

"""

# Exercise 3 solution
print(df.shape[1])

"""#### Exercise 4: What are the names of columns ?"""

# Exercise 4 solution
df.columns

"""#### Exercise 5: How is the dataset indexed ?"""

# Exercise 5 solution
df.index



"""#### Exercise 6: How many people survived?"""

# Exercise 6 solution
total_survived = df.survived.sum()
total_survived

"""#### Exercise 7: Print unique towns in Embark town field ?"""

# Exercise 7 solution
embark_town_list = df['embark_town'].unique()
embark_town_list

"""#### Exercise 8: Find the data type of age field ?"""

# Exercise 8 solution
df.age.dtype

"""#### Exercise 9: Find the distribution of values in the alive field ?"""

# Exercise 9 solution
df.alive.value_counts()

"""#### Exercise 10: What is the town with most passengers ?"""

# Exercise 10 solution
# Top town name
df.embark_town.value_counts().head(1).index[0]

# Top 3 
df.embark_town.value_counts().head(3)

"""#### Exercise 11: Summarise the dataframe"""

# Exercise 11 solution
df.describe()

"""#### Exercise 12: Summarise all the columns"""

# Exercise 12 solution
# Summarise all the columns. Notice: By default, only the numeric columns are returned.
df.describe(include = "all")

"""#### Exercise 13: Summarize only the survived column"""

# Exercise 13 solution
df.survived.describe()

"""#### Exercise 14: What is the mean age of passengers?"""

# Exercise 14 solution
round(df.age.mean())

"""#### Exercise 15: What is the age with least occurrence?"""

# Exercise 15 solution
df.age.value_counts().tail()

"""## Practice section 2: Filtering and Sorting

#### Loading the nations dataset
"""

# Loading the titanic dataset from internet
df = pd.read_csv("https://raw.githubusercontent.com/vamsivarma/datasets/master/data_science/pandas/nations.csv") 

#print(df)

df.info()

"""#### Exercise 1: Sort the dataset by country name"""

# Exercise 1 solution
df.country.sort_values()

# OR

df.sort_values(by = "country")

"""#### Exercise 2: Country with highest population"""

# Exercise 2 solution

# Country name with highest population
df.sort_values(by = "population", ascending = False).head(1)

# Top 5 country names by population
df.sort_values(by = "population", ascending = False).head(100)['country'].unique()

"""#### Exercise 3: Find the number of times China is there in the country coulumn in the dataset"""

china_records = df[df.country == "China"]

len(china_records)

"""#### Exercise 4: View only the columns country, year, life_expect, birth_rate and assign them to a dataframe called filtered_df"""

# Exercise 4 solution
# Filter only giving the column names
filtered_df = df[['country', 'year', 'life_expect', 'birth_rate']]
filtered_df

"""#### Exercise 5: Sort the dataset by life_expect and then by birth_rate"""

filtered_df.sort_values(['life_expect', 'birth_rate'], ascending = False)

"""#### Exercise 6: Filter the top 5 countries which have life expectancy more than 75"""

filtered_df = df[df.life_expect > 75]

# Get the top 5 country names
filtered_df['country'].unique()[:5]

"""#### Exercise 7: Find the country names which start with G"""

filtered_df = df[df.country.str.startswith('G')]

# Get the country names
filtered_df['country'].unique()

"""#### Exercise 8: Select the first 7 columns"""

df.iloc[: , 0:7]

"""#### Exercise 9: Select all columns except the last 3."""

df.iloc[: , :-3]

"""#### Set the column country as the index of dataframe"""

df.set_index('country', inplace=True)

"""#### Exercise 10: Find the Life_Expect, GDP_PERCAP from India and Italy"""

df.loc[["India", "Italy"], ["life_expect", "gdp_percap", "year"]]

"""#### Exercise 11: Select the rows 3 to 7 and the columns 3 to 6"""

df.iloc[2:7, 2:6]

"""#### Exercise 12: Select every row after the fourth row and all columns

"""

df.iloc[4:, :]

"""#### Exercise 13: Select every row up to the 4th row and all columns"""

df.iloc[:4, :]

"""#### Exercise 14: Select the 3rd column up to the 7th column"""

df.iloc[:, 2:7]

"""#### Exercise 15: Select rows where life_expect is greater than 50 or less than 70 """

#Select rows where df.deaths is greater than 500 or less than 50¶
df[(df["life_expect"] > 50) | (df["life_expect"] < 70)]

"""### Practice section 3: Grouping

#### Exercise 1: Find the mean of life_expect by region
"""

df.groupby(['region']).life_expect.mean()

"""#### Exercise 2: Find the mean, median min and max values for life_expect grouped by region"""

df.groupby('region').life_expect.agg(['mean', 'min', 'max', 'median'])

"""#### Exercise 3: Find the mean, median min and max values for life_expect grouped by region and year"""

df.groupby(['region','year']).life_expect.agg(['mean', 'min', 'max', 'median'])

"""### Practice section 4: Apply

#### Exercise 1: Add a new column, "life_expect_range" to the dataset and if a row has life_expect more than 70, the value will of that column will be Good, if the life_expect is between 50 and 70 then the value will be Normal, if the life_expect is less than 50 then the value is Low
"""

def life_expect_range(x):
    if x >= 70:
      return 'Good'
    elif x > 50:
      return 'Normal'
    else:
      return 'Low'

df['life_expect_range'] = df['life_expect'].apply(life_expect_range)
df.head(50)

"""#### Useful references
https://github.com/guipsamora/pandas_exercises - Includes a lot of practice exercises for Pandas
"""

