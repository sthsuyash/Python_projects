'''
A linear relationship is a statistical term that is nothing but the relationship between two variables. 
A linear relationship shows how well two variables x and y are related to each other. 
'''

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv(
    'https://raw.githubusercontent.com/amankharwal/Website-data/master/Instagram.csv', encoding='latin1')
data = data.dropna()  # drop rows with missing values
# print(data.head())  # print first 5 rows

plt.figure(figsize=(10, 8))
plt.style.use('fivethirtyeight')
plt.title('Relation between Profile visits and Follows')
sns.regplot(x="Profile Visits", y="Follows", data=data)
plt.show()
