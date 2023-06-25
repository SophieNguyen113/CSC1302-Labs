# Prolog
# Author:  Sophie Nguyen
# Email:  nnguyen177@student.gsu.edu
# Section: 034

import matplotlib.pyplot as plt
import pandas as pd

# Read input file name from user
file = input("Enter CSV file name: ")

# Read in the CSV file as a dataframe
df = pd.read_csv(file)

# Print the average of flight delays and flight cancellations
avg_delays = df["Delayed"].mean()
avg_cancellations = df["Cancelled"].mean()
print(f'Average delays:{avg_delays: .2f}')
print(f'Average cancellations:{avg_cancellations: .2f}')

# Create a lineplot of flight delays vs months
plt.plot(df["Month"], df["Delayed"], label="Delays")

# In the same figure, create a lineplot of flight cancellations vs months
plt.plot(df["Month"], df["Cancelled"], label="Cancellations")

# Add axis labels, title, and legend
plt.xlabel("Months", fontsize=10)
plt.ylabel("Number of Flights", fontsize=10)
plt.title("Flight Status at LAX", fontsize=14)
plt.legend()

# Save figure as output_fig.png
plt.savefig("output_fig.png")