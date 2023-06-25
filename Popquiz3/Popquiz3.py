# Prolog
# Author:  Sophie Nguyen
# Email:  nnguyen177@student.gsu.edu
# Section: 034

'''
    Pop Quiz 3 - Homework:
        Clean any 1 of the given files.
    
    I chose 'peaceful_20_5_2020.csv' file.
'''

import pandas as pd

# Load the dataset.
df = pd.read_csv('peaceful_20_5_2020.csv')

print('This is the information of the dataset BEFORE the cleaning part.')
print()
print(df.info())
print()
print(df.describe())
print()

df_copy = df.copy()

'''
    Filter these 2 columns (favorited and retweeted) to check if they contain 'True' values. 
    If they only contain 'False' values, then they would become unused columns.
'''

filtered1 = df_copy[df_copy['favorited'].isin([True])]
filtered2 = df_copy[df_copy['retweeted'].isin([True])]

count1 = filtered1['favorited'].value_counts()
count2 = filtered2['retweeted'].value_counts()

print('The numbers of True values in favorited column is:')
print(count1)
print('The numbers of True values in retweeted column is:')
print(count2)
print()

'''
    Since the numbers of 'True' values in both columns are 0, which means they only contain 'False' values.
    I would remove these 2 unused columns.
'''

print(f'favorited and retweeted columns would be removed.')
print()

# Remove unused columns.
df = df.drop(['Unnamed: 0', 'text', 'favorited', 'statusSource', 'retweeted'], axis=1)
# Fill missing values with the mean of the columns.
df = df.fillna(df.mean())
# Remove duplicates.
df= df.drop_duplicates()
# Reset the index.
df = df.reset_index(drop=True)

print('This is the information of the dataset AFTER the cleaning part.')
print()
print(df.info())
print()
print(df.describe())
print()

