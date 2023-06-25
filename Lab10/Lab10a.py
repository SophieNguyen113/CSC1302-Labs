# Prolog
# Author:  Sophie Nguyen
# Email:  nnguyen177@student.gsu.edu
# Section: 034

import pandas as pd

data = {
    'Points': [876, 789, 863, 673, 741, 812, 756, 788, 694, 701, 804, 690],
    'Ranking': [1, 2, 2, 3, 3, 4, 1, 1, 2, 4, 1, 2],
    'Team': ['red', 'red', 'blue', 'green', 'yellow', 'red', 'blue', 'green', 'yellow', 'yellow', 'red', 'blue'],
    'year': [2014, 2015, 2014, 2015, 2014, 2015, 2016, 2017, 2016, 2014, 2015, 2017],
    'MVP': ['Kevin', 'Kevin', 'mike', 'john', 'parth', 'mark', 'Aron', 'neil', 'edward', 'max', 'neil', 'john']
}

df = pd.DataFrame(data)

df1 = df.groupby('year').agg({'Points': sum})

print(df1)