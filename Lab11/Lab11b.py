# Prolog
# Author:  Sophie Nguyen
# Email:  nnguyen177@student.gsu.edu
# Section: 034

import pandas as pd

file_name = input()

# TODO: Read in file_name as a dataframe
df = pd.read_csv(file_name, delimiter="\t")

# TODO: Output rows by descending Final scores
finals_scores = df["Final"]
df = df.sort_values(by=["Final"], ascending=False)
print(df[["Lname", "Fname", "Final"]].to_string(index=False))

print("\nMax Scores:")

# TODO: Output the max scores of each assignment
max_scores = df.max(numeric_only=True)
print(max_scores.to_string())

print("\nMedian Scores:")

# TODO: Output the median scores of each assignment
medians = df.median(numeric_only=True)
print(medians.to_string())

print("\nAverage Scores:")

# TODO: Output the average scores of each assignment.
averages = df.mean(numeric_only=True)
print(averages.to_string())

print("\nStandard Deviation:")

# TODO: Output the standard devation of each assignment.
std_devs = df.std(numeric_only=True)
print(std_devs.to_string())
