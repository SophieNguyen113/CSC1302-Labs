# Prolog
# Author:  Sophie Nguyen
# Email:  nnguyen177@student.gsu.edu
# Section: 034

from sklearn.cluster import KMeans
import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
mammalSleep = pd.read_csv('msleep.csv')

# Clean the data
mammalSleep = mammalSleep.dropna()

# Create a dataframe with the columns sleep_total and sleep_cycle
X = mammalSleep[['sleep_total', 'sleep_cycle']]

# Initialize a k-means clustering model with 4 clusters and random_state = 0
km = KMeans(n_clusters=4, random_state=0)

# Fit the model
mammalSleepKm = km.fit(X)

# Find the centroids of the clusters
mammalSleepCentroids = km.cluster_centers_
print(mammalSleepCentroids)

# Predict the cluster for each data point in mammal_sleep
mammalSleep['cluster'] = km.predict(X)

plt.figure(figsize=(6, 6))

# Graph the clusters
for cluster in set(mammalSleep['cluster']):
    plt.plot(mammalSleep[mammalSleep['cluster'] == cluster]['sleep_total'],
             mammalSleep[mammalSleep['cluster'] == cluster]['sleep_cycle'], '.')

plt.xlabel('Total sleep', fontsize=14)
plt.ylabel('Length of sleep cycle',fontsize=14)
plt.savefig('msleep_clusters.png')

WCSS = []
k = [1,2,3,4,5]
for j in k:
    km = KMeans(n_clusters=j)
    mammalSleepKmWCSS = km.fit(X)
    intermediateWCSS = mammalSleepKmWCSS.inertia_
    WCSS.append(round(intermediateWCSS,1))
    
print(WCSS)
