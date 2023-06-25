# Prolog
# Author:  Sophie Nguyen
# Email:  nnguyen177@student.gsu.edu
# Section: 034

import pandas as pd

# Read in hmeq.csv with the first 100 rows
hmeq = pd.read_csv('hmeq.csv').head(100)

# Create a new data frame with the rows with missing values dropped
hmeqDelete = hmeqDelete = hmeq.dropna()

# Create a new data frame with the missing values filled in by the mean of the column
hmeqReplace = hmeq.fillna(hmeq.mean())

# Print the means of the columns for each new data frame
print("Means for hmeqDelete are ", hmeqDelete.mean())

print("Means for hmeqReplace are ", hmeqReplace.mean())