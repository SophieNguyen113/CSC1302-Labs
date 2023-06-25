# Prolog
# Author:  Sophie Nguyen
# Email:  nnguyen177@student.gsu.edu
# Section: 034

import matplotlib.pyplot as plt
import pandas as pd

file1 = input("Enter CSV file 1 name: ")
file2 = input("Enter CSV file 2 name: ")

# Read CSV files as dataframes
df_july = pd.read_csv(file1)
df_december = pd.read_csv(file2)

# Print each dataframe
print("JULY DATAFRAME:")
print(df_july)
print("DECEMBER DATAFRAME:")
print(df_december)

# Create subplots
fig, ax = plt.subplots(1, 2)

# Plot July data
ax[0].scatter(df_july['Gross Potential'], df_july['Capacity'])
ax[0].set_xlabel('Gross Potential')
ax[0].set_ylabel('Capacity')
ax[0].set_title('July 2002')

# Plot December data
ax[1].scatter(df_december['Gross Potential'], df_december['Capacity'])
ax[1].set_xlabel('Gross Potential')
ax[1].set_title('December 2002')

# Set main title
fig.suptitle('Capacity vs. Gross Potential')

# Save figure
plt.savefig('subplots.png')
